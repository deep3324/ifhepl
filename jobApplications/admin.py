from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from jobApplications.models import jobUser, job_application

# Register your models here.
# admin.site.register(jobUser)

class JobUserResource(resources.ModelResource):
    class Meta:
        model = jobUser

@admin.register(jobUser)
class JobApplyAdmin(ImportExportModelAdmin):
    resource_class = JobUserResource
    list_display = ("username","email",)

class JobApplyResource(resources.ModelResource):
    class Meta:
        model = job_application

@admin.register(job_application)
class JobApplyAdmin(ImportExportModelAdmin):
    resource_class = JobApplyResource
    list_display = ("name", "mobile_number",
                    "submitted_on", "reference_number",)
    fieldsets = (
        ('Personal Details', {
            'fields': ('user', ('reference_number', 'name'), ('dob', 'email'), ('aadhar_no','pan_no'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),)
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': (('village', 'po'), ('ps', 'block'), ('district', 'state'), 'pin_code'),
        }),
        ('Matriculation (10th)', {
            'classes': ('collapse',),
            'fields': (('board_10', 'school_10'), ('passing_10', 'roll_10'), ('mark_10', 'percentage_10'),),
        }),
        ('Intermediate (10th)', {
            'classes': ('collapse',),
            'fields': (('board_12', 'school_12'), ('passing_12', 'roll_12'), ('mark_12', 'percentage_12'),),
        }),
        ('Graduation Degree', {
            'classes': ('collapse',),
            'fields': (('univ_graduation', 'insti_graduation'), ('passing_graduation', 'roll_graduation'), ('mark_graduation', 'percentage_graduation'),),
        }),
        ('Master Degree', {
            'classes': ('collapse',),
            'fields': (('univ_master', 'insti_master'), ('passing_master', 'roll_master'), ('mark_master', 'percentage_master'),),
        }),
        ('Document Upload', {
            'classes': ('collapse',),
            'fields': (('edudoc'), ('imgs', 'sign'),),
        }),
        ('Submitted On', {
            'fields': ('submitted_on',)
        }),
        ('Job Update', {
            'fields': (('submitted','accept', 'reject'),)
        }),

    )
