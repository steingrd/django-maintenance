from django.http import HttpResponseServerError
from django.shortcuts import render_to_response
from datetime import datetime
from models import Maintenance



class MaintenanceMiddleware(object):
    
    def process_request(self, request):
        if request.path.startswith("/admin"):
            return None
        
        now = datetime.now()
        objects = Maintenance.objects.filter(start_time__lt=now, end_time__gt=now, enabled=True)
        
        if objects.count() > 0:
            maintenance = objects[0]
            if maintenance.maintenancefilter_set.count() > 0:
                for filter in maintenance.maintenancefilter_set.all():
                    if request.path.startswith(filter.path):
                        abort_request = True
                        break
                else:
                    # filters specified, but none matched the request
                    abort_request = False
            else:
                # no filters specified, means we abort the request 
                abort_request = True
                
            if abort_request:
                context = {'maintenance': maintenance}
                return render_to_response('maintenance/downtime.html', context)
        
        return None