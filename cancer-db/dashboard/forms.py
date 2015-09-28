from django import forms
from models import Patient, Cancer, Symptom, Treatment, Test, FollowUp, Questionnaire  # STC
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.utils.safestring import mark_safe
from django.contrib.admin import widgets     
from django.contrib.auth.models import Group
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError                   
from parsley.decorators import parsleyfy

import selectable.forms as selectable
from selectable.forms import AutoCompleteWidget

#from .lookups import InvestigatorLookup,CellmodelLookup, ShrnaLookup, ExperimentTitleLookup, ProjectLookup

from functools import partial, wraps
from django.forms.formsets import formset_factory



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('id','username')


class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('created_by','created_date','updated_by','updated_date','approvalStatus','download_by','download_date')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('created_by','created_date','updated_by','updated_date','approvalStatus','download_by','download_date','DB_ID','name','EMR_id')

class CancerForm(forms.ModelForm):
    class Meta:
        model = Cancer
        exclude = ('created_by','created_date','updated_by','updated_date','approvalStatus','download_by','download_date','patient','DB_ID')                

class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        exclude = ('created_by','created_date','updated_by','updated_date','approvalStatus','download_by','download_date','patient','DB_ID')

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        exclude = ('approvalStatus','created_by','created_date','updated_by','updated_date','download_by','download_date','patient','DB_ID')

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ('approvalStatus','created_by','created_date','updated_by','updated_date','download_by','download_date','patient','DB_ID')

class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        exclude = ('approvalStatus','created_by','created_date','updated_by','updated_date','download_by','download_date','patient','DB_ID')

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        exclude = ('approvalStatus','created_by','created_date','updated_by','updated_date','download_by','download_date','patient','DB_ID')





