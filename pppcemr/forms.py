# from .models import Encounter, Assessment, Diagnosis, Note, Treatment, Lab
from .models import *
from django import forms
# import autocomplete_light

# from dal import autocomplete

from django.contrib.admin.widgets import ForeignKeyRawIdWidget

class EncounterModelForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['encounter_owner','encounter_type']



class EncounterEditModelForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['encounter_owner', 'encounter_type', 'is_open', 'room', 'EM_level']

class EncounterBillModelForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['EM_level']

class EncounterCloseModelForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = []

class AssessmentModelForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['diagnosis']

class AssessmentCloseModelForm(forms.ModelForm):
    close_comment = forms.CharField(max_length = 300, required = False)
    class Meta:
        model = Assessment
        fields = []

class EditPMFSHModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['birth_history', 'past_medical_history', 'family_history', 'social_history']

class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['results', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(NoteModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class HPIModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['results', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(HPIModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class FUModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['results', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(FUModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"


class NewTreatmentModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['treatment_option', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(NewTreatmentModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class TreatmentCloseModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['is_open', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(TreatmentCloseModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class LabModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['results', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(LabModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class InHouseLabModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['results', 'next_page', 'assessments']
    def __init__(self, *args, **kwargs):
        super(InHouseLabModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class VitalsModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['chief_complaint', 'weight_lb', 'weight_oz', 'height', 'temperature', 'temperature_location', 
                'HR', 'RR', 'Systolic_BP',  'Diastolic_BP', 'BP_location', 'assessments']
    def __init__(self, *args, **kwargs):
        super(VitalsModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class PEModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['PE_constitutional', 'PE_head_and_face', 'PE_eyes', 'PE_ears', 'PE_nose_mouth_and_throat',
                  'PE_neck', 'PE_chest_and_breast', 'PE_respiratory', 'PE_heart', 'PE_pulses_vascular',
                  'PE_gastrointestinal','PE_GU', 'PE_musculoskeletal', 'PE_skin_and_nodes',
                  'PE_neurologic', 'PE_psyche', 'assessments']
    def __init__(self, *args, **kwargs):
        super(PEModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class PFSHModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['birth_history', 'surgical_and_hospital_history', 'past_medical_history',
                  'family_history', 'social_history', 'assessments']
    def __init__(self, *args, **kwargs):
        super(PFSHModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"


class PrescriptionModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['drug', 'drug_admin_option', 'assessments']
    def __init__(self, *args, **kwargs):
        super(PrescriptionModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class AllergyModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['allergic_reaction_symptoms', 'assessments']
    def __init__(self, *args, **kwargs):
        super(AllergyModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class VaccineModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['vaccine_lot_number','vaccine_site', 'assessments']
    def __init__(self, *args, **kwargs):
        super(VaccineModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class FollowUpModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['results', 'assessments']
    def __init__(self, *args, **kwargs):
        super(FollowUpModelForm, self).__init__(*args, **kwargs)
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class PrescriptionDoseModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['calculated_dose', 'dose_unit',  'calculated_dose',
                  'dose_unit', 'route', 'frequency', 'duration',
                  'dispense_amount', 'dispense_unit', 'drug_package',
                  'pharmacist_instruction','patient_instruction', 'assessments']
    def __init__(self, *args, **kwargs):
        super(PrescriptionDoseModelForm, self).__init__(*args, **kwargs)
        self.fields['drug_package'].required = True
        self.fields['assessments'].widget.attrs['style'] = "width: 400px;"

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'next_page': forms.HiddenInput()}
        fields = ['subject', 'body', 'owner', 'owner_group', 'next_page']

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient_users_list', 'recipient_groups_list', 'subject', 'body', ]


class AddWorkplanModelForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['workplan']

class ChooseReportForm(forms.Form):
    report = forms.ModelChoiceField(queryset=Report.objects.all())

class UploadAttachmentForm(forms.ModelForm):
    class Meta:
        model = FileAttachment
        fields = ['name','file_attachment']