from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin, GroupAdmin


from .models import *

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class EmployeeGroupInline(admin.StackedInline):
    model = EmployeeGroup
    can_delete = False
    verbose_name_plural = 'employee group'

class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )
    
class GroupAdmin(GroupAdmin):
    inlines = (EmployeeGroupInline, )
    
class EncountersInline(admin.StackedInline):
    model= Encounter

class TreatmentsInline(admin.StackedInline):
    model = Treatment
    fieldsets = [
        (None, {'fields': ['treatment_option', 'description', 'results']}),
    ]
    raw_id_fields = ('treatment_option','drug', 'drug_package','drug_admin_option', 'patient', 'encounter', 'assessments')
    
class AssessmentsInline(admin.StackedInline):
    model=Assessment
    raw_id_fields = ('diagnosis', 'encounters')

class WorkplanStepAddAssessmentInline(admin.StackedInline):
    model = WorkplanStepAddAssessment
    raw_id_fields = ('diagnosis', )

class WorkplanStepAddTreatmentInline(admin.StackedInline):
    model = WorkplanStepAddTreatment
    raw_id_fields = ('treatment_option', )

class WorkplanStepAddTaskInline(admin.StackedInline):
    model = WorkplanStepAddTask

class CPTcodesInline(admin.StackedInline):
    model = CPTcode
    verbose_name = 'CPT code'
    fields = ['code']

class SavedTextResponseInline(admin.StackedInline):
    model = SavedTextResponse
    fields = ['text', 'user']

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name']}),
        (None, {'fields': ['last_name']}),
        (None, {'fields': ['birthdate']}),
        (None, {'fields': ['gender']}),
    ]
    search_fields = ['^first_name', '^last_name','^birthdate']
    inlines = [EncountersInline, AssessmentsInline]

class RoomsInline(admin.StackedInline):
    model = Room

class OfficeAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = [RoomsInline]
    
class DiagnosisAdmin(admin.ModelAdmin):
    fields = ('icd_code', 'description', 'user_description', 'default_snomed', 'auto_close')
    search_fields = ['icd_code', 'description', 'user_description']
    inlines = [TreatmentsInline,]
    raw_id_fields = ['default_snomed']

class SnomedAdmin(admin.ModelAdmin):
    fields = ('name', 'code', 'icd_equivalents')
    search_fields = ['name', 'code', 'icd_equivalents']

class EncounterAdmin(admin.ModelAdmin):
    raw_id_fields = ('patient',)


class EncounterTypeAdmin(admin.ModelAdmin):
    fields = ('name','is_well','is_direct','is_billed','default_workplan')

class StandardPhysicalResultsAdmin(admin.ModelAdmin):
    fields = ('name','PE_constitutional','PE_head_and_face','PE_eyes',
                  'PE_ears', 'PE_nose_mouth_and_throat', 'PE_neck',
                  'PE_chest_and_breast', 'PE_respiratory', 'PE_heart',
                  'PE_pulses_vascular', 'PE_gastrointestinal','PE_GU',
                  'PE_musculoskeletal', 'PE_skin_and_nodes',
                  'PE_neurologic','PE_psyche')

class DrugAdmin(admin.ModelAdmin):
    readonly_fields =('trade_name', 'generic_name', 'product_id',
                  'product_ndc', 'dosage_form', 'route',
                  'concentration_numerator',
                  'concentration_denominator', 'dea')
    fields = ('trade_name', 'generic_name', 'product_id',
                  'product_ndc', 'dosage_form', 'route',
                  'concentration_numerator',
                  'concentration_denominator', 'dea')
    search_fields = ['trade_name','generic_name','product_ndc', 'dosage_form']


class DrugPackageAdmin(admin.ModelAdmin):
    readonly_fields = ('package_name','package_ndc','product_ndc','product_id')
    fields = ('package_name','package_ndc','product_ndc','product_id')
    search_fields = ['package_name','package_ndc','product_ndc', 'product_id']


class DrugAdminOptionAdmin(admin.ModelAdmin):
    fields = ('name', 'frequency', 'dose','patient_instruction','pharmacist_instruction',
              'multiply_by_weight','dose_per_day','duration_days')
    search_fields = ['name']


class TreatmentOptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name', 'type','default_result']}),
        ('Drug Options', {'classes': ('collapse',),'fields':['drugs', 'drug_admins']}),
        ('Vaccine Options', {'classes': ('collapse',),'fields':['vaccine_manufacturer']}),
        ('Allergy Options', {'classes':('collapse',),'fields':['drug_allergy_cross_reactions']}),
    ]
    search_fields = ['name','type']
    raw_id_fields = ['drugs', 'drug_admins']
    inlines = [CPTcodesInline, SavedTextResponseInline]


class PracticePreferencesAdmin(admin.ModelAdmin):
    fields = ('encounter_summary_report','group_to_receive_new_lab_tasks','group_to_receive_new_office_tasks' )

class WorkplanAdmin(admin.ModelAdmin):
    fields = ('name', 'is_well','min_age_months','max_age_months')
    inlines = [WorkplanStepAddAssessmentInline, WorkplanStepAddTreatmentInline, WorkplanStepAddTaskInline]

class ReportAdmin(admin.ModelAdmin):
    fields = ('name','type','report_template')

class MessageAdmin(admin.ModelAdmin):
    fields = ('subject', 'body','recipient', 'recipient_users_list','recipient_groups_list','sender')



admin.site.register(Patient, PatientAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Snomed, SnomedAdmin)
admin.site.register(Encounter, EncounterAdmin)
admin.site.register(EncounterType, EncounterTypeAdmin)
admin.site.register(StandardPhysicalResults, StandardPhysicalResultsAdmin)
admin.site.register(TreatmentOption, TreatmentOptionAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(DrugAdminOption,DrugAdminOptionAdmin)
admin.site.register(DrugPackage, DrugPackageAdmin)
#admin.site.register(DrugAdminOption, DrugAdminOptionAdmin)
# admin.site.register(LabType, LabTypeAdmin)
# admin.site.register(InHouseLabType, InHouseLabTypeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(PracticePreferences,PracticePreferencesAdmin)
admin.site.register(Workplan, WorkplanAdmin)
admin.site.register(Report,ReportAdmin)
admin.site.register(Message, MessageAdmin)
