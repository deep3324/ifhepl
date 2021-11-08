from ifheplapp.models import Attendance, Contact,  Gallery, HealthCard, Jobs, KisanCard, Membership, JobApply, Notice, Slider
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User

admin.site.register(Notice)
admin.site.register(Gallery)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Jobs)
admin.site.unregister(User)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs


class AttendanceResource(resources.ModelResource):
    class Meta:
        model = Attendance

@admin.register(Attendance)
class AttendanceAdmin(ImportExportModelAdmin):
    resource_class = AttendanceResource
    list_display = ("employeeID", "employeeName", "location",
                    "image", "uploaded_at",)


class MembershipResource(resources.ModelResource):
    class Meta:
        model = Membership

@admin.register(Membership)
class MembershipAdmin(ImportExportModelAdmin):
    resource_class = MembershipResource
    list_display = ("name", "mobile_number", "submitted_on",
                    "card_number", "reference_number","employeename",)
    fieldsets = (
        ('Employee Details', {
            'fields': (('employeeID', 'employeename'),)
        }),
        ('Personal Details', {
            'fields': (('reference_number', 'name'), ('dob', 'email'), ('idtype', 'id_proof'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),)
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': (('village', 'po'), ('ps', 'block'), ('district', 'state'), 'pin_code'),
        }),
        ('Document Upload', {
            'classes': ('collapse',),
            'fields': (('id_proof_document'), ('photo'),),
        }),
        ('Card Update', {
            'fields': ('approve', 'reject', 'underprocess', 'card_number',)
        }),
    )

class KisanCardResource(resources.ModelResource):
    class Meta:
        model = KisanCard

@admin.register(KisanCard)
class KisanCardAdmin(ImportExportModelAdmin):
    resource_class = KisanCardResource
    list_display = ("name", "mobile_number", "submitted_on",
                    "card_number", "reference_number","employeename",)
    fieldsets = (
        ('Employee Details', {
            'fields': (('employeeID', 'employeename'),)
        }),
        ('Personal Details', {
            'fields': (('reference_number', 'name'), ('dob', 'email'), ('idtype', 'id_proof'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),)
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': (('village', 'po'), ('ps', 'block'), ('district', 'state'), 'pin_code'),
        }),
        ('Document Upload', {
            'classes': ('collapse',),
            'fields': (('id_proof_document'), ('photo'),),
        }),
        ('Card Update', {
            'fields': ('approve', 'reject', 'underprocess', 'card_number',)
        }),

    )

class HealthCardResource(resources.ModelResource):
    class Meta:
        model = HealthCard

@admin.register(HealthCard)
class HealthCardAdmin(ImportExportModelAdmin):
    resource_class = HealthCardResource
    list_display = ("name", "mobile_number", "submitted_on",
                    "card_number", "reference_number","employeename",)
    fieldsets = (
        ('Employee Details', {
            'fields': (('employeeID', 'employeename'),)
        }),
        ('Personal Details', {
            'fields': (('reference_number', 'name'), ('dob', 'email'), ('idtype', 'id_proof'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),)
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': (('village', 'po'), ('ps', 'block'), ('district', 'state'), 'pin_code'),
        }),
        ('Document Upload', {
            'classes': ('collapse',),
            'fields': (('id_proof_document'), ('photo'),),
        }),
        ('Card Update', {
            'fields': ('approve', 'reject', 'underprocess', 'card_number',)
        }),

    )

class JobApplyResource(resources.ModelResource):
    class Meta:
        model = JobApply

@admin.register(JobApply)
class JobApplyAdmin(ImportExportModelAdmin):
    resource_class = JobApplyResource
    list_display = ("name", "mobile_number",
                    "submitted_on", "reference_number",)
    fieldsets = (
        ('Personal Details', {
            'fields': (('reference_number', 'name'), ('dob', 'email'), ('idtype', 'id_proof'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),)
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
            'fields': ('approve', 'reject',)
        }),

    )
