from import_export import resources
from .models import *
 
class EmployerResource(resources.ModelResource):
    class Meta:
        model = Employer


class HrInfoResource(resources.ModelResource):
    class Meta:
        model = Employer
        
class JobResource(resources.ModelResource):
    class Meta:
        model = Employer        