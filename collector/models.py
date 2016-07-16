from django.db import models


class DataPoint(models.Model):
    """
    Stores client info with datetime, type, and value of data point collected
    """

    node_name = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    data_type = models.CharField(max_length=100)
    data_value = models.FloatField()

    def __str__(self):
        return 'DataPoint for {}. {} = {}'.format(self.node_name, self.data_type, self.data_value)
