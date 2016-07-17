from django.views.generic import TemplateView
from collector.models import DataPoint


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
