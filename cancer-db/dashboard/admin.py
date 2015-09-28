from __future__ import unicode_literals

from import_export.admin import ImportExportMixin, ExportActionModelAdmin

from django.contrib import admin
from .models import Patient, Cancer, Symptom, Treatment, Test, FollowUp, Questionnaire


class PatientAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['sex', 'location','created_by','updated_by','tagged']

class CancerAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['diagnosis','cancer_type','admission_date', 'discharge_date','department','tagged']

class SymptomAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['pain_VAS', 'night_pain','stay_in_bed','duration']

class TreatmentAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['tagged']

class TestAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['tagged']

class FollowUpAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['tagged']

class QuestionnaireAdmin(ImportExportMixin, admin.ModelAdmin):
    	list_filter = ['tagged']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Cancer, CancerAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(FollowUp, FollowUpAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)

