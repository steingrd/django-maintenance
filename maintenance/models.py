from django.db import models


class Maintenance(models.Model):
    enabled = models.BooleanField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.start_time.isoformat()
        
class MaintenanceFilter(models.Model):
    maintenance = models.ForeignKey(Maintenance)
    path = models.CharField(max_length=128)