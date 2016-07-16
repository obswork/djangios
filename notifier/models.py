from django.db import models


class Alert(models.Model):
    """
    Allow user to set min OR max threshold for a node's data_value to reach before
    an alert is triggered.
    """
    node_name = models.CharField(max_length=250, blank=True)
    data_type = models.CharField(max_length=100)
    min_value = models.FloatField(null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)

    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.max_value is None and self.min_value is None:
            raise models.exceptions.ValidationError('Either min or max value is required for an alert')
        super(Alert, self).save(*args, **kwargs)
