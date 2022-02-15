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
    list_display = ('name', 'emmloyeeid', "job_location", "current_month_health_card_created",
                    "current_month_kisan_card_created", "current_month_membership_card_created", "can_accept_cash")
    fieldsets = (
        ('Employee Details', {
            'fields': (('user', 'emmloyeeid'), ('name', 'gender'), ('email', 'phone_number'), ("designation", "job_location"), ("dob", "bloodgroup"), ("image", "Address"), "can_accept_cash")
        }),
        ('Current Month Card Created', {
            'fields': (('current_month_health_card_created', 'current_month_kisan_card_created', 'current_month_membership_card_created',),)
        }),
        ('Previous Month Card Created', {
            'fields': (('previous_month_health_card_created', 'previous_month_kisan_card_created', 'previous_month_membership_card_created',),),
        }),
        ('Total Card Created', {
            'fields': (('total_health_card_created', 'total_kisan_card_created', 'total_membership_card_created'),),
        }),
    )
