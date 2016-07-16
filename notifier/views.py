from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from notifier.models import Alert


class AlertListView(ListView):
    template_name = 'alerts_list.html'
    model = Alert


class NewAlertView(CreateView):
    template_name = 'create_or_update_alert.html'
    model = Alert
    fields = [
        'node_name', 'data_type', 'max_value', 'min_value', 'active'
    ]

    def get_success_url(self):
        return reverse('alerts-list')


class EditAlertView(UpdateView):
    template_name = 'create_or_update_alert.html'
    model = Alert
    fields = [
        'node_name', 'data_type', 'max_value', 'min_value', 'active'
    ]

    def get_success_url(self):
        return reverse('alerts-list')
