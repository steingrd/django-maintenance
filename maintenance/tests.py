from django.test import TestCase
from django.http import HttpRequest
from django.conf import settings

from datetime import datetime, timedelta

from middleware import MaintenanceMiddleware
from models import Maintenance, MaintenanceFilter

class MaintenanceMiddlewareTest(TestCase):
    
    def _create_request(self, path):
         request = HttpRequest()
         request.META = {
            'SERVER_NAME': 'testserver',
            'SERVER_PORT': 80
         }
         request.path = request.path_info = "/%s" % path
         return request
         
    def _create_maintenance_now(self):
        maintenance = Maintenance()
        maintenance.start_time = datetime.now() - timedelta(3600)
        maintenance.end_time = datetime.now() + timedelta(3600)
        return maintenance
        
    def _create_maintenance_yesterday(self):
        maintenance = Maintenance()
        maintenance.start_time = datetime.now() - timedelta(1, 3600)
        maintenance.end_time = datetime.now() - timedelta(1)
        return maintenance

    def test_should_always_allow_admin(self):
        request = self._create_request('admin/')
        middleware = MaintenanceMiddleware()
        
        maintenance = self._create_maintenance_now()
        maintenance.enabled = True
        maintenance.description = "Testing admin request"
        maintenance.save()
        response = middleware.process_request(request)
        
        self.assertEquals(None, response)

    def test_should_return_none_on_empty_database(self):
        request = self._create_request('testing/')
        middleware = MaintenanceMiddleware()
        
        self.assertEquals(0, Maintenance.objects.all().count())
        self.assertEquals(None, middleware.process_request(request))
    
    def test_should_return_none_on_enabled_and_inactive_object(self):
        request = self._create_request('testing/')
        middleware = MaintenanceMiddleware()
        
        maintenance = self._create_maintenance_yesterday()
        maintenance.enabled = True
        maintenance.description = "Testing inactive object"
        maintenance.save()
        response = middleware.process_request(request)
        
        self.assertEquals(1, Maintenance.objects.all().count())
        self.assertEquals(None, response)
    
    def test_should_return_none_on_enable_and_active_if_filter_misses(self):
        request = self._create_request('testing/')
        middleware = MaintenanceMiddleware()
        
        maintenance = self._create_maintenance_now()
        maintenance.enabled = True
        maintenance.description = "Testing enabled and filtered object"
        maintenance.save()
        filter = MaintenanceFilter()
        filter.maintenance = maintenance
        filter.path = '/blog/'
        filter.save()
        response = middleware.process_request(request)

        self.assertEquals(1, Maintenance.objects.all()[0].maintenancefilter_set.count())
        self.assertEquals(1, Maintenance.objects.all().count())
        self.assertEquals(None, response)
    
    def test_should_return_none_on_disabled_and_active_object(self):
        request = self._create_request('testing/')
        middleware = MaintenanceMiddleware()
        
        maintenance = self._create_maintenance_now()
        maintenance.enabled = False
        maintenance.description = "Testing disabled object"
        maintenance.save()
        response = middleware.process_request(request)
        
        self.assertEquals(1, Maintenance.objects.all().count())
        self.assertEquals(None, response)
    
    def test_should_interrupt_on_enabled_and_active_object(self):
        request = self._create_request('testing/')
        middleware = MaintenanceMiddleware()
        
        maintenance = self._create_maintenance_now()
        maintenance.enabled = True
        maintenance.description = "Testing enabled object"
        maintenance.save()
        response = middleware.process_request(request)
        
        self.assertEquals(1, Maintenance.objects.all().count())
        self.assertNotEquals(None, response)

        
        
