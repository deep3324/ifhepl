from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from jobApplications.models import job_application

# Register your models here.
# admin.site.register(jobUser)

class JobApplyResource(resources.ModelResource):
    class Meta:
        model = job_application

@admin.register(job_application)
class JobApplyAdmin(ImportExportModelAdmin):
    resource_class = JobApplyResource
    list_display = ("name", "mobile_number",
                    "submitted_on", "reference_number","paid")
    readonly_fields = ['order_id','razorpay_signature','transaction_date','razorpay_payment_id','payment_status','payment_mode']
    fieldsets = (
        ('Personal Details', {
            'fields': ('user', ('reference_number', 'name'), ('dob', 'email'), ('aadhar_no','pan_no'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),('applied_for','employee_profile')),
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': (('village', 'po'), ('ps', 'block'), ('district', 'state'), 'pin_code'),
        }),
        ('Matriculation (10th)', {
            'classes': ('collapse',),
            'fields': (('matriculation_board_university', 'matriculation_school_institute'), ('matriculation_passing_year', 'matriculation_roll_number'), ('matriculation_marks_gpa', 'matriculation_percentage'),),
        }),
        ('Intermediate (12th)', {
            'classes': ('collapse',),
            'fields': (('intermediate_board_university', 'intermediate_school_institute'), ('intermediate_passing_year', 'intermediate_roll_number'), ('intermediate_marks_gpa', 'intermediate_percentage'),),
        }),
        ('Graduation', {
            'classes': ('collapse',),
            'fields': (('graduation_board_university', 'graduation_school_institute'), ('graduation_passing_year', 'graduation_roll_number'), ('graduation_marks_gpa', 'graduation_percentage'),),
        }),
        ('Higher Qualification', {
            'classes': ('collapse',),
            'fields': (('higher_qualification_board_university', 'higher_qualification_school_institute'), ('higher_qualification_passing_year', 'higher_qualification_roll_number'), ('higher_qualification_marks_gpa', 'higher_qualification_percentage'),),
        }),
        ('Extra Qualification', {
            'classes': ('collapse',),
            'fields': (('extra_qualification_board_university', 'extra_qualification_school_institute'), ('extra_qualification_passing_year', 'extra_qualification_roll_number'), ('extra_qualification_marks_gpa', 'extra_qualification_percentage'),),
        }),
        ('Document Upload', {
            'classes': ('collapse',),
            'fields': (('sign'), ('photo'),),
        }),
        ('Submitted On', {
            'fields': ('submitted_on',)
        }),
        ('Job Update', {
            'fields': (('completed','accept', 'reject'),)
        }),
        ('Payment Update', {
            'fields': (('order_id'),('transaction_date'),('payment_status'),('payment_mode'),('razorpay_signature','razorpay_payment_id'), 'paid')
        }),

    )
