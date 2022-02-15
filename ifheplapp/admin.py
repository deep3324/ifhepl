from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ifheplapp.models import AssociatePartner, Attendance, Contact,  Gallery, HealthCard, Jobs, KisanCard, Membership, Notice, Order, Slider, Transaction
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
admin.site.register(AssociatePartner)
admin.site.register(Transaction)
admin.site.register(Order)


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
    list_display = ("name", "card_number", "reference_number",
                    "submitted_on", "employeename", "created",)
    readonly_fields = ['order_id', 'razorpay_signature', 'transaction_date',
                       'razorpay_payment_id', 'payment_status', 'payment_mode']
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
            'fields': ('approve', 'reject', 'underprocess', 'created', 'card_number',)
        }),
        ('Payment Update', {
            'fields': (('order_id'), ('transaction_date'), ('payment_status'), ('payment_mode'), ('razorpay_signature', 'razorpay_payment_id'), ('paid', 'order_details'))
        }),
    )


class KisanCardResource(resources.ModelResource):
    class Meta:
        model = KisanCard


@admin.register(KisanCard)
class KisanCardAdmin(ImportExportModelAdmin):
    resource_class = KisanCardResource
    list_display = ("name", "card_number", "reference_number",
                    "submitted_on", "employeename", "created",)
    readonly_fields = ['order_id', 'razorpay_signature', 'transaction_date',
                       'razorpay_payment_id', 'payment_status', 'payment_mode']
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
            'fields': ('approve', 'reject', 'underprocess', 'created', 'card_number',)
        }),
        ('Payment Update', {
            'fields': (('order_id'), ('transaction_date'), ('payment_status'), ('payment_mode'), ('razorpay_signature', 'razorpay_payment_id'), ('paid', 'order_details'))
        }),
    )


class HealthCardResource(resources.ModelResource):
    class Meta:
        model = HealthCard


@admin.register(HealthCard)
class HealthCardAdmin(ImportExportModelAdmin):
    resource_class = HealthCardResource
    list_display = ("name", "card_number", "reference_number",
                    "submitted_on", "employeename", "created",)
    readonly_fields = ['order_id', 'razorpay_signature', 'transaction_date',
                       'razorpay_payment_id', 'payment_status', 'payment_mode']
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
            'fields': ('approve', 'reject', 'underprocess', 'created', 'card_number',)
        }),
        ('Payment Update', {
            'fields': (('order_id'), ('transaction_date'), ('payment_status'), ('payment_mode'), ('razorpay_signature', 'razorpay_payment_id'), ('paid', 'order_details'))
        }),
    )
