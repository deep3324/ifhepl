from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from vendorApplication.models import vendorApplication

# Register your models here.
# admin.site.register(jobUser)

class vendorResource(resources.ModelResource):
    class Meta:
        model = vendorApplication

@admin.register(vendorApplication)
class vendorAdmin(ImportExportModelAdmin):
    resource_class = vendorResource
    list_display = ("name", "mobile_number",
                    "submitted_on", "reference_number","paid")
    readonly_fields = ['order_id','razorpay_signature','transaction_date','razorpay_payment_id','payment_status','payment_mode']
    fieldsets = (
        ('Personal Details', {
            'fields': ('VendorID', ('reference_number', 'name'), ('dob', 'email'), ('idtype','id_proof'), ('father_Husband_name', 'mother_name'), ('category', 'disability'), ('mobile_number', 'alt_mobile_no'),)
        }),
        ('Address', {
            'classes': ('collapse',),
            'fields': (('village', 'po'), ('ps', 'block'), ('district', 'state'), 'pin_code'),
        }),
        ('Document Upload', {
            'classes': ('collapse',),
            'fields': (('id_proof_document'), ('photo'),('signature'),),
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
