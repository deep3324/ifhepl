from django.contrib import admin

from EmployeeProfile.models import EmployeeProfile
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class EmployeeProfileResource(resources.ModelResource):
    class Meta:
        model = EmployeeProfile
        import_id_fields = ('id', )

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(ImportExportModelAdmin):
    resource_class = EmployeeProfileResource
    list_display = ('name', 'emmloyeeid', 'email', 
                  "designation", "job_location",)