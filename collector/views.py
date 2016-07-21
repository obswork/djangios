from django.views.generic import TemplateView, View
from collector.models import DataPoint
from django.forms.models import modelform_factory
from django.http.response import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse


class StatusView(TemplateView):
    # TODO: refactor as ListView --> and then into DRF ModelViewSet
    template_name = 'status.html'

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)

        # to optimize db queries - first find the unique node/data_type pairs
        nodes_and_data_types = DataPoint.objects.all().values('node_name', 'data_type').distinct()

        # dict of node--data-type--data-value to return to the the template
        data_status = {}

        # for each distinct node--data-type pair query the db for the latest DatePoint instance (status)
        for node_and_data_type in nodes_and_data_types:
            # node_name and data_type to filter query by
            node_name = node_and_data_type['node_name']
            data_type = node_and_data_type['data_type']

            # retrive/set dict w/ key:val = node_name: {} and
            # store in data_point_map var
            data_point_map = data_status.setdefault(node_name, dict())
            # for each data_type, for each node, store the latest value
            data_point_map[data_type] = DataPoint.objects.filter(
                node_name=node_name, data_type=data_type
            ).latest('datetime')

        context['data_status'] = data_status

        return context


class RecordApiView(View):

    def post(self, request, *args, **kwargs):
        # check if the secret keys match
        if request.META.get('HTTP_AUTH_SECRET') != 'iamasecretkey':
            return HttpResponseForbidden('Auth key incorrect!')

        # modelform_factory creates modelform subclass of given model, editable fields limited by fields kwarg
        form_class = modelform_factory(DataPoint, fields=['node_name', 'data_type', 'data_value'])
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse()
        else:
            return HttpResponseBadRequest()
