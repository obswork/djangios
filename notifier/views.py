from django.views.generic import ListView
from notifier.models import Alert


class AlertListView(ListView):
    template_name = 'alerts_list.html'
    model = Alert
