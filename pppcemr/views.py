from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.core import serializers
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import redirect
import json
import re
from django.db.models import Q
from django.contrib import messages

from django import forms
from django.template import Template, Context

from .forms import *

from .models import *

from .growthcharts import *

def apply_default_snomeds_to_diagnoses():
    for diagnosis in Diagnosis.objects.all().iterator():
        snomed = Snomed.objects.filter(icd_equivalents__icontains = diagnosis.icd_code).first()
        if not snomed:
            snomed = Snomed.objects.filter(icd_equivalents__icontains = diagnosis.icd_code.split('.')[0]).first()
        diagnosis.default_snomed = snomed
        diagnosis.save()
        result_string = "%s default snomed: %s" % (diagnosis, diagnosis.default_snomed)
        print(result_string)


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def get_patient(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        entry_query = get_query(q, ['first_name', 'last_name','birthdate'])
        patients = Patient.objects.filter(entry_query).order_by('last_name')[:20]
        results = []
        for patient in patients:
            patient_json = {}
            patient_json['id']= patient.pk
            patient_json['label']= patient.__str__()
            patient_json['value']= patient.__str__()
            results.append(patient_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_diagnosis(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        entry_query = get_query(q, ['icd_code', 'description','user_description'])
        diagnoses = Diagnosis.objects.filter(entry_query).order_by('-date_last_used')[:20]
        results = []
        for diagnosis in diagnoses:
            diagnosis_json = {}
            diagnosis_json['id']= diagnosis.pk
            diagnosis_json['label']= diagnosis.__str__()
            diagnosis_json['value']= diagnosis.__str__()
            results.append(diagnosis_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_snomed(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        entry_query = get_query(q, ['name', 'code','icd_equivalents'])
        snomeds = Snomed.objects.filter(entry_query).order_by('-name')[:20]
        results = []
        for snomed in snomeds:
            snomed_json = {}
            snomed_json['id']= snomed.pk
            snomed_json['label']= snomed.__str__()
            snomed_json['value']= snomed.__str__()
            results.append(snomed_json)
        data = json.dumps(results)
        print(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_treatment_option(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        entry_query = get_query(q, ['name'])
        treatment_options = TreatmentOption.objects.filter(entry_query).order_by('name')[:20]
        results = []
        for treatment_option in treatment_options:
            treatment_option_json = {}
            treatment_option_json['id']= treatment_option.pk
            treatment_option_json['label']= treatment_option.__str__()
            treatment_option_json['value']= treatment_option.__str__()
            results.append(treatment_option_json)
        data = json.dumps(results)
        print(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_standard_PE_results(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        entry_query = get_query(q, ['name'])
        physical_options = StandardPhysicalResults.objects.filter(entry_query).order_by('name')[:20]
        results = []
        for physical_option in physical_options:
            physical_option_json = {}
            physical_option_json['id']= physical_option.pk
            physical_option_json['label']= physical_option.__str__()
            physical_option_json['value']= physical_option.__str__()
            physical_option_json['PE_constitutional'] = physical_option.PE_constitutional
            physical_option_json['PE_head_and_face'] = physical_option.PE_head_and_face
            physical_option_json['PE_eyes'] = physical_option.PE_eyes
            physical_option_json['PE_ears'] = physical_option.PE_ears
            physical_option_json['PE_nose_mouth_and_throat'] = physical_option.PE_nose_mouth_and_throat
            physical_option_json['PE_neck'] = physical_option.PE_neck
            physical_option_json['PE_chest_and_breast'] = physical_option.PE_chest_and_breast
            physical_option_json['PE_respiratory'] = physical_option.PE_respiratory
            physical_option_json['PE_heart'] = physical_option.PE_heart
            physical_option_json['PE_pulses_vascular'] = physical_option.PE_pulses_vascular
            physical_option_json['PE_gastrointestinal'] = physical_option.PE_gastrointestinal
            physical_option_json['PE_GU'] = physical_option.PE_GU
            physical_option_json['PE_musculoskeletal'] = physical_option.PE_musculoskeletal
            physical_option_json['PE_skin_and_nodes'] = physical_option.PE_skin_and_nodes
            physical_option_json['PE_neurologic'] = physical_option.PE_neurologic
            physical_option_json['PE_psyche'] = physical_option.PE_psyche
            results.append(physical_option_json)
        data = json.dumps(results)
        print(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# def get_weights(request, pk):
#     patient = Patient.objects.get(pk=pk)
#     treatments = patient.get_weights()
#     results = []
#     data_list = []
#     for treatment in treatments:
#         age = (treatment.date.date() - patient.birthdate).total_seconds()/31622400
#         set = [age, treatment.total_weight]
#         data_list.append(set)
#     return JsonResponse(data_list, safe=False)

def get_weights(pk):
    patient = Patient.objects.get(pk=pk)
    treatments = patient.get_weights()
    data_list = []
    for treatment in treatments:
        age = (treatment.date.date() - patient.birthdate).total_seconds()/31622400
        set = [age, treatment.weight_kg*weight_conversion_multiplier]
        data_list.append(set)
    return data_list

def get_heights(pk):
    patient = Patient.objects.get(pk=pk)
    treatments = patient.get_heights()
    data_list = []
    for treatment in treatments:
        age = (treatment.date.date() - patient.birthdate).total_seconds()/31622400
        set = [age, treatment.height_cm*height_conversion_multiplier]
        data_list.append(set)
    return data_list

def get_bmis(pk):
    patient = Patient.objects.get(pk=pk)
    treatments = patient.get_weights_and_heights()
    data_list = []
    for treatment in treatments:
        age = (treatment.date.date() - patient.birthdate).total_seconds()/31622400
        set = [age, treatment.weight_kg/((treatment.height_cm/100)**2)]
        data_list.append(set)
    return data_list

def get_weight_for_length(pk):
    patient = Patient.objects.get(pk=pk)
    treatments = patient.get_weight_and_heights()
    data_list = []
    for treatment in treatments:
        set = [treatment.height_cm, treatment.weight_kg]
        data_list.append(set)
    return data_list

class IndexView(generic.ListView):
    template_name = 'pppcemr/index.html'
    context_object_name = 'office_list'
    def get_queryset(self):
        return Office.objects.order_by('name')

class OfficeView(generic.DetailView):
    model = Office
    template_name = 'pppcemr/office_detail.html'

class RoomView(generic.DetailView):
    model = Room
    template_name = 'pppcemr/room_detail.html'

class EncounterView(generic.DetailView):
    model = Encounter
    template_name = 'pppcemr/encounter_detail.html'
    def get_context_data(self,**kwargs):
        context = super(EncounterView, self).get_context_data(**kwargs)
        context['prior_treatments'] = Treatment.objects.filter(date__lt = Encounter.objects.get(pk=self.kwargs.get('pk')).encounter_date)
        return context

class PatientView(generic.DetailView):
    model = Patient
    template_name = 'pppcemr/patient_detail.html'

class WeightChartView(generic.DetailView):
    model = Patient
    template_name = 'pppcemr/growthchart_weight.html'
    def get_context_data(self, **kwargs):
        context = super(WeightChartView, self).get_context_data(**kwargs)
        context['weights'] = get_weights(self.kwargs.get('pk'))
        gender = Patient.objects.get(id=self.kwargs.get('pk')).gender
        context['gender'] = gender
        if settings.USE_SI:
            context['ylabel'] = 'kg'
        else:
            context['ylabel'] = 'lb'
        if gender == 'M':
            context['third_percentile'] = third_percentile_weight_male
            context['fifth_percentile'] = fifth_percentile_weight_male
            context['tenth_percentile'] = tenth_percentile_weight_male
            context['twenty_fifth_percentile'] = twenty_fifth_percentile_weight_male
            context['fiftieth_percentile'] = fiftieth_percentile_weight_male
            context['seventy_fifth_percentile'] = seventy_fifth_percentile_weight_male
            context['ninetieth_percentile'] = ninetieth_percentile_weight_male
            context['ninety_fifth_percentile'] = ninety_fifth_percentile_weight_male
            context['ninety_seventh_percentile'] = ninety_seventh_percentile_weight_male
        else:
            context['third_percentile'] = third_percentile_weight_female
            context['fifth_percentile'] = fifth_percentile_weight_female
            context['tenth_percentile'] = tenth_percentile_weight_female
            context['twenty_fifth_percentile'] = twenty_fifth_percentile_weight_female
            context['fiftieth_percentile'] = fiftieth_percentile_weight_female
            context['seventy_fifth_percentile'] = seventy_fifth_percentile_weight_female
            context['ninetieth_percentile'] = ninetieth_percentile_weight_female
            context['ninety_fifth_percentile'] = ninety_fifth_percentile_weight_female
            context['ninety_seventh_percentile'] = ninety_seventh_percentile_weight_female
        return context


class HeightChartView(generic.DetailView):
    model = Patient
    template_name = 'pppcemr/growthchart_height.html'
    def get_context_data(self, **kwargs):
        context = super(HeightChartView, self).get_context_data(**kwargs)
        context['heights'] = get_heights(self.kwargs.get('pk'))
        gender = Patient.objects.get(id=self.kwargs.get('pk')).gender
        context['gender'] = gender
        if settings.USE_SI:
            context['ylabel'] = 'cm'
        else:
            context['ylabel'] = 'in'
        if gender == 'M':
            context['third_percentile'] = third_percentile_height_male
            context['fifth_percentile'] = fifth_percentile_height_male
            context['tenth_percentile'] = tenth_percentile_height_male
            context['twenty_fifth_percentile'] = twenty_fifth_percentile_height_male
            context['fiftieth_percentile'] = fiftieth_percentile_height_male
            context['seventy_fifth_percentile'] = seventy_fifth_percentile_height_male
            context['ninetieth_percentile'] = ninetieth_percentile_height_male
            context['ninety_fifth_percentile'] = ninety_fifth_percentile_height_male
            context['ninety_seventh_percentile'] = ninety_seventh_percentile_height_male
        else:
            context['third_percentile'] = third_percentile_height_female
            context['fifth_percentile'] = fifth_percentile_height_female
            context['tenth_percentile'] = tenth_percentile_height_female
            context['twenty_fifth_percentile'] = twenty_fifth_percentile_height_female
            context['fiftieth_percentile'] = fiftieth_percentile_height_female
            context['seventy_fifth_percentile'] = seventy_fifth_percentile_height_female
            context['ninetieth_percentile'] = ninetieth_percentile_height_female
            context['ninety_fifth_percentile'] = ninety_fifth_percentile_height_female
            context['ninety_seventh_percentile'] = ninety_seventh_percentile_height_female
        return context


class BMIChartView(generic.DetailView):
    model = Patient
    template_name = 'pppcemr/growthchart_bmi.html'
    def get_context_data(self, **kwargs):
        context = super(BMIChartView, self).get_context_data(**kwargs)
        context['bmis'] = get_bmis(self.kwargs.get('pk'))
        gender = Patient.objects.get(id=self.kwargs.get('pk')).gender
        context['gender'] = gender
        context['ylabel'] = 'kg/m^2'
        if gender == 'M':
            context['third_percentile'] = third_percentile_bmi_male
            context['fifth_percentile'] = fifth_percentile_bmi_male
            context['tenth_percentile'] = tenth_percentile_bmi_male
            context['twenty_fifth_percentile'] = twenty_fifth_percentile_bmi_male
            context['fiftieth_percentile'] = fiftieth_percentile_bmi_male
            context['seventy_fifth_percentile'] = seventy_fifth_percentile_bmi_male
            context['ninetieth_percentile'] = ninetieth_percentile_bmi_male
            context['ninety_fifth_percentile'] = ninety_fifth_percentile_bmi_male
            context['ninety_seventh_percentile'] = ninety_seventh_percentile_bmi_male
        else:
            context['third_percentile'] = third_percentile_bmi_female
            context['fifth_percentile'] = fifth_percentile_bmi_female
            context['tenth_percentile'] = tenth_percentile_bmi_female
            context['twenty_fifth_percentile'] = twenty_fifth_percentile_bmi_female
            context['fiftieth_percentile'] = fiftieth_percentile_bmi_female
            context['seventy_fifth_percentile'] = seventy_fifth_percentile_bmi_female
            context['ninetieth_percentile'] = ninetieth_percentile_bmi_female
            context['ninety_fifth_percentile'] = ninety_fifth_percentile_bmi_female
            context['ninety_seventh_percentile'] = ninety_seventh_percentile_bmi_female
        return context

class AssessmentView(generic.DetailView):
    model = Assessment
    template_name = 'pppcemr/assessment_detail.html'
    def get_context_data(self, **kwargs):
        context = super(AssessmentView, self).get_context_data(**kwargs)
        context['current_encounter_id'] = self.kwargs.get('encounterid', None)
        if self.kwargs.get('encounterid', None):
            encounter = Encounter.objects.get(pk=self.kwargs.get('encounterid', None))
            assessment = Assessment.objects.get(pk=self.kwargs.get('pk',None))
            if (encounter.patient.pk == assessment.patient.pk):
                context['current_encounter'] = encounter
            else:
                errorstring = 'Different patients: Encounter patient: %s; Assessment patient: %s' % (encounter.patient, assessment.patient)
                raise Http404(errorstring)
        return context

class TreatmentView(generic.DetailView):
    model = Treatment
    template_name = 'pppcemr/treatment_detail.html'
    def get_context_data(self, **kwargs):
        context = super(TreatmentView, self).get_context_data(**kwargs)
        context['current_encounter_id'] = self.kwargs.get('encounterid', None)
        context['current_assessment_id'] = self.kwargs.get('assessmentid', None)
        treatment = Treatment.objects.get(pk=self.kwargs.get('pk', None))
        if self.kwargs.get('encounterid', None):
            encounter = Encounter.objects.get(pk=self.kwargs.get('encounterid', None))
            if (encounter.patient.pk == treatment.patient.pk):
                context['current_encounter'] = encounter
            else:
                raise Http404("Treatment and encounter must be on same patient.")
        if self.kwargs.get('assessmentid', None):
            assessment = Assessment.objects.get(pk=self.kwargs.get('assessmentid', None))
            if (encounter.patient.pk == treatment.patient.pk) and (assessment.patient.pk == treatment.patient.pk):
                context['current_assessment'] = assessment
            else:
                raise Http404("Treatment, assessment, and encounter must be on same patient.")
        return context
             
class TaskView(generic.DetailView):
    model = Task
    template_name = 'pppcemr/task_detail.html'
    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        context['current_encounter_id'] = self.kwargs.get('encounterid', None)
        context['current_assessment_id'] = self.kwargs.get('assessmentid', None)
        return context

class MessageView(generic.DetailView):
    model = Message
    template_name = 'pppcemr/message_detail.html'


def TaskList(request):
    return render(request, 'pppcemr/task_list.html', {
        'user' : request.user
    })

def MessageList(request):
    return render(request, 'pppcemr/message_list.html', {
        'user' : request.user
    })

class VaccinesView(generic.DetailView):
    model = Patient
    template_name = 'pppcemr/vaccines_detail.html'
    def get_context_data(self, **kwargs):
        context = super(VaccinesView, self).get_context_data(**kwargs)
        context['dtap_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(
            Q(treatment_option__name__icontains = 'tdap') | Q(treatment_option__name__icontains = 'dtap'))
        context['hepa_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'hepa')
        context['hepb_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'hepb')
        context['hib_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'hib')
        context['hpv_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'hpv')
        context['flu_list'] = Treatment.objects.filter(patient__pk=self.kwargs.get('pk')).filter(
            treatment_option__type__icontains='va').filter(
            Q(treatment_option__name__icontains='iiv') | Q(treatment_option__name__icontains='laiv'))
        context['mcv_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'mcv')
        context['menb_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'menb')
        context['mmr_list'] = Treatment.objects.filter(patient__pk=self.kwargs.get('pk')).filter(
            treatment_option__type__icontains='va').filter(treatment_option__name__icontains='mmr')
        context['pcv_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'pcv')
        context['ppsv_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'ppsv')
        context['polio_list'] = Treatment.objects.filter(patient__pk=self.kwargs.get('pk')).filter(
            treatment_option__type__icontains='va').filter(
            Q(treatment_option__name__icontains='polio') | Q(treatment_option__name__icontains='ipv'))
        context['rv_list'] = Treatment.objects.filter(patient__pk=self.kwargs.get('pk')).filter(
            treatment_option__type__icontains='va').filter(
            Q(treatment_option__name__icontains='rv') | Q(treatment_option__name__icontains='rotavirus'))
        context['var_list'] = Treatment.objects.filter(patient__pk = self.kwargs.get('pk')).filter(
            treatment_option__type__icontains = 'va').filter(treatment_option__name__icontains = 'var')
        return context


def new_encounter(request, pk): # pk here refers to room primary key
    if request.method == "POST":
        print(request)
        encounterform = EncounterModelForm(request.POST)
        if encounterform.is_valid() and request.POST.get('patient_pk',''):
            encounter = encounterform.save(commit=False)
            encounter.patient = Patient.objects.get(pk=request.POST.get('patient_pk',''))
            encounter.room = Room.objects.get(pk=pk)
            encounter.office = encounter.room.office
            encounter.encounter_date = timezone.now()
            encounter.save()
            encounter.patient.close_autoclose_assessments()
            return redirect('room_detail', pk=encounter.room.id)
    else:
        encounterform = EncounterModelForm()
    return render(request, 'pppcemr/encounter_add.html', {'form':encounterform})

def get_encounter(request,roomid,pk):
    encounter = Encounter.objects.get(pk=pk)
    encounter.room = Room.objects.get(pk=roomid)
    encounter.workplan = encounter.encounter_type.default_workplan
    encounter.save()
    print('Is encounter type well?')
    print(encounter.encounter_type.is_well)
    print('Encounter type:')
    if encounter.encounter_type.is_well:
        encounter.apply_correct_well_workplan()
    if encounter.workplan:
        apply_workplan(encounter)
    return redirect('room_detail', pk=roomid)


def lookup_patient(request):
    if request.method == "POST":
        if request.POST.get('patient_pk',''):
            patient = Patient.objects.get(pk=request.POST.get('patient_pk',''))
            return redirect('patient_detail', pk=patient.id)
    return render(request, 'pppcemr/lookup_patient.html', {})

def edit_encounter(request, pk): # pk refers to encounter key
    encounter = Encounter.objects.get(id=pk)
    if request.method == "POST":
        encounterform = EncounterEditModelForm(request.POST, instance=encounter)
        if encounterform.is_valid():
            encounter = encounterform.save(commit=False)
            encounter.save()
            return redirect('encounter_detail', pk=encounter.id)
    else:
        encounterform = EncounterEditModelForm(instance=encounter)
    return render(request, 'pppcemr/encounter_edit.html', {'form':encounterform})

def review_encounter(request, pk):
    encounter = Encounter.objects.get(id=pk)
    for assessment in encounter.assessment_set.all():
        if '?' in assessment.diagnosis.icd_code:
            if request.method == "POST":
                form = AssessmentModelForm(request.POST, instance=assessment)
                form.fields['diagnosis'].queryset = Diagnosis.objects.filter(icd_code__icontains = assessment.diagnosis.icd_code.split('?')[0]).exclude(icd_code__icontains = '?')
                form.fields['diagnosis'].help_text = 'Enter more specific diagnosis for : %s' % (assessment.diagnosis)
                if form.is_valid():
                    assessment = form.save()
                    return redirect('review_encounter', pk = encounter.id)
            else:
                form = AssessmentModelForm(instance=assessment)
                form.fields['diagnosis'].queryset = Diagnosis.objects.filter(icd_code__icontains = assessment.diagnosis.icd_code.split('?')[0]).exclude(icd_code__icontains = '?')
                form.fields['diagnosis'].help_text = 'Enter more specific diagnosis for: %s' % (assessment.diagnosis)
            return render(request, 'pppcemr/encounter_review.html', {'form':form, 'assesssment': assessment})
    for task in encounter.task_set.all():
        if task.is_open:
            messages.add_message(request, messages.WARNING, 'There are unfinished tasks. Complete these before closing encounter.')
            return redirect('encounter_detail', pk=encounter.id)
    # for treatment in encounter.treatment_set.all():
    #     if treatment.get_cpt_codes():
    #         if not treatment.assessments.all():
    #             messages.add_message(request, messages.WARNING, 'There are billed treatments not attached to assessments.  Add assessments to these treatments before closing encounter.')
    #             return redirect('encounter_detail', pk=encounter.id)
    if not encounter.EM_level:
        if request.method == "POST":
            form = EncounterBillModelForm(request.POST, instance=encounter)
            if form.is_valid():
                encounter = form.save()
                return redirect('review_encounter', pk = encounter.id)
        else:
            form = EncounterBillModelForm(instance=encounter)
        return render(request, 'pppcemr/encounter_edit.html', {'form':form})
    messages.add_message(request, messages.SUCCESS, 'Encounter successfully reviewed.')
    create_encounter_summary(encounter)
    return redirect('close_encounter', pk=encounter.id)

def close_encounter(request, pk): # pk refers to encounter key
    encounter = Encounter.objects.get(id=pk)
    if request.method == "POST":
        encounterform = EncounterCloseModelForm(request.POST, instance=encounter)
        if encounterform.is_valid():
            encounter = encounterform.save(commit=False)
            encounter.is_open = False
            encounter.date_closed = timezone.now()
            encounter.save()
            for treatment in encounter.treatment_set.all():
                if treatment.has_no_assessment():
                    if not ((treatment.treatment_option.type in treatment.treatment_option.ALLERGY)
                            or (treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION)):
                        treatment.is_open = False
                        treatment.save()
            return redirect('room_detail', pk=encounter.room.id)
    else:
        encounterform = EncounterCloseModelForm(instance=encounter)
    return render(request, 'pppcemr/encounter_close.html', {'form':encounterform, 'encounter': encounter})

def reopen_encounter(request, pk): # pk refers to encounter key
    encounter = Encounter.objects.get(id=pk)
    if request.method == "POST":
        encounterform = EncounterCloseModelForm(request.POST, instance=encounter)
        if encounterform.is_valid():
            encounter = encounterform.save(commit=False)
            encounter.is_open = True
            encounter.save()
            return redirect('encounter_detail', pk=encounter.id)
    else:
        encounterform = EncounterCloseModelForm(instance=encounter)
    return render(request, 'pppcemr/encounter_reopen.html', {'form':encounterform})

def edit_PMFSH(request,pk):
    encounter = Encounter.objects.get(id=pk)
    patient = Patient.objects.get(id=encounter.patient.pk)
    if request.method == "POST":
        form = EditPMFSHModelForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=True)
            return redirect('encounter_detail', pk=encounter.id)
    else:
        form = EditPMFSHModelForm(instance=patient)
    return render(request,'pppcemr/patient_edit.html',{'form':form} )

def new_assessment(request, pk):
    if request.method == "POST":
        if request.POST.get('diagnosis_pk',''):
            diagnosis = Diagnosis.objects.get(pk=request.POST.get('diagnosis_pk',''))
            assessment = Assessment()
            encounter = Encounter.objects.get(pk=pk)
            assessment.diagnosis = diagnosis
            assessment.snomed = diagnosis.default_snomed
            assessment.assessment_date = timezone.now()
            assessment.patient = encounter.patient
            assessment.owner = encounter.encounter_owner
            assessment.is_open = True
            assessment.auto_close = assessment.diagnosis.auto_close
            assessment.save()
            assessment.encounters.add(encounter)
            diagnosis.date_last_used = timezone.now()
            diagnosis.save()
            return redirect('encounter_assessment_detail', encounterid=pk, pk=assessment.id)
    return render(request, 'pppcemr/assessment_add.html', {'pk':pk})

def change_snomed(request, encounterid=None, pk=None):
    assessment = Assessment.objects.get(id=pk)
    if request.method == "POST":
        if request.POST.get('snomed_pk',''):
            snomed = Snomed.objects.get(pk=request.POST.get('snomed_pk',''))
            assessment = Assessment.objects.get(id=pk)
            assessment.snomed = snomed
            assessment.save()
            if request.POST.get('set_default',''):
                diagnosis = Diagnosis.objects.get(pk=assessment.diagnosis.pk)
                diagnosis.default_snomed=snomed
                diagnosis.save()
            return redirect('encounter_assessment_detail', encounterid=encounterid, pk=assessment.id)
    return render(request, 'pppcemr/snomed_change.html', {'assessment':assessment})

def close_assessment(request, encounterid=None, pk=None):
    assessment = Assessment.objects.get(id=pk)
    if request.method == "POST":
        assessmentcloseform = AssessmentCloseModelForm(request.POST, instance = assessment)
        if assessmentcloseform.is_valid():
            assessment = assessmentcloseform.save(commit=False)
            assessment.is_open = False
            assessment.date_closed = timezone.now()
            if assessmentcloseform.cleaned_data['close_comment']:
                treatment = Treatment()
                treatment.treatment_option = TreatmentOption.objects.get(type='NT')
                treatment.encounter = Encounter.objects.get(pk=encounterid)
                treatment.patient = Patient.objects.get(pk=assessment.patient.pk)
                treatment.results = assessmentcloseform.cleaned_data['close_comment']
                treatment.date = timezone.now()
                treatment.owner = treatment.encounter.encounter_owner
                treatment.save()
                treatment.assessments.add(assessment)
            assessment.save()
            if not assessment.is_open:
                for treatment in assessment.treatment_set.all():
                    if treatment.has_no_open_assessment():
                        treatment.is_open = False
                        treatment.save()
            # return redirect('encounter_detail', pk=encounterid)
            return redirect(reverse('encounter_detail', kwargs={'pk':encounterid})+'#encounter_assessments')
    else:
        assessmentcloseform = AssessmentCloseModelForm(instance=assessment)
    return render(request, 'pppcemr/assessment_close.html', {'form':assessmentcloseform})

def new_treatment(request, encounterid=None, assessmentid=None):
    if request.method == "POST":
        if request.POST.get('treatment_option_pk',''):
            treatment = Treatment()
            treatment.treatment_option = TreatmentOption.objects.get(pk=request.POST.get('treatment_option_pk',''))
            treatment.date = timezone.now()
            treatment.encounter = Encounter.objects.get(pk=encounterid)
            treatment.patient = treatment.encounter.patient
            treatment.owner = request.user
            treatment.save()
            if assessmentid:
                assessment = Assessment.objects.get(pk=assessmentid)
                assessment.encounters.add(Encounter.objects.get(pk=encounterid))
                treatment.assessments.add(assessment)
            treatment.description = '%s' % (treatment.treatment_option.name)
            treatment.is_open = True
            treatment.results = treatment.treatment_option.default_result
            treatment.save()
            process_new_treatment(treatment) # do stuff that's supposed to be run when a new treatment is made
            if treatment.treatment_option.type in (treatment.treatment_option.LAB, treatment.treatment_option.IN_HOUSE_LAB,
                                                   treatment.treatment_option.VITALS, treatment.treatment_option.TEST,
                                                   treatment.treatment_option.VACCINE):
                if assessmentid:
                    return redirect('encounter_assessment_detail', encounterid=encounterid, pk=assessmentid)
                else:
                    return redirect('encounter_detail', pk=treatment.encounter.id)
            else:
                if assessmentid:
                    return redirect('edit_treatment', encounterid=encounterid, assessmentid=assessmentid, pk=treatment.id)
                else:
                    return redirect('edit_encounter_treatment', encounterid=encounterid, pk = treatment.id)
    else:
        form = NewTreatmentModelForm()
    return render(request,'pppcemr/treatment_add.html', {'encounter':Encounter.objects.get(pk=encounterid) })


def edit_treatment(request, encounterid=None, assessmentid=None, pk=None):
    treatment = Treatment.objects.get(id=pk)
    if request.method == "POST":
        if treatment.treatment_option.type in treatment.treatment_option.NOTE:
            form = NoteModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.LAB:
            form = LabModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.IN_HOUSE_LAB:
            form = InHouseLabModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.VITALS:
            form = VitalsModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.PHYSICAL_EXAM:
            form = PEModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.HPI:
            form = HPIModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION:
            form = PrescriptionModelForm(request.POST, instance=treatment)
            form.fields['drug'].queryset = treatment.treatment_option.drugs.all()
            form.fields['drug'].required = True
            form.fields['drug_admin_option'].queryset = treatment.treatment_option.drug_admins.all()
            form.fields['drug_admin_option'].required = True
        if treatment.treatment_option.type in treatment.treatment_option.VACCINE:
            form = VaccineModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.FOLLOW_UP:
            form = FollowUpModelForm(request.POST, instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.ALLERGY:
            form = AllergyModelForm(request.POST, instance=treatment)
        form.fields['assessments'].queryset = Assessment.objects.filter(patient = treatment.patient)
        form.fields['assessments'].help_text = 'Hold ctrl or command to select multiple assessments'
        if form.is_valid():
            treatment=form.save(commit = True)
            if treatment.treatment_option.type in treatment.treatment_option.VITALS:
                if treatment.weight_oz:
                    treatment.weight_kg = round((treatment.weight_lb + treatment.weight_oz/16)/2.2,3)
                elif treatment.weight_lb:
                    treatment.weight_kg = round(treatment.weight_lb/2.2,3)
                if treatment.height:
                    treatment.height_cm = round(treatment.height*2.54,3)
            if treatment.treatment_option.type in treatment.treatment_option.PHYSICAL_EXAM:
                if treatment.standard_PE_results:
                    if not treatment.PE_constitutional:
                        treatment.PE_constitutional = treatment.standard_PE_results.PE_constitutional
                    if not treatment.PE_head_and_face:
                        treatment.PE_head_and_face = treatment.standard_PE_results.PE_head_and_face
                    if not treatment.PE_eyes:
                        treatment.PE_eyes = treatment.standard_PE_results.PE_eyes
                    if not treatment.PE_ears:
                        treatment.PE_ears =treatment.standard_PE_results.PE_ears
                    if not treatment.PE_nose_mouth_and_throat:
                        treatment.PE_nose_mouth_and_throat = treatment.standard_PE_results.PE_nose_mouth_and_throat
                    if not treatment.PE_neck:
                        treatment.PE_neck = treatment.standard_PE_results.PE_neck
                    if not treatment.PE_chest_and_breast:
                        treatment.PE_chest_and_breast = treatment.standard_PE_results.PE_chest_and_breast
                    if not treatment.PE_respiratory:
                        treatment.PE_respiratory = treatment.standard_PE_results.PE_respiratory
                    if not treatment.PE_heart:
                        treatment.PE_heart = treatment.standard_PE_results.PE_heart
                    if not treatment.PE_pulses_vascular:
                        treatment.PE_pulses_vascular = treatment.standard_PE_results.PE_pulses_vascular
                    if not treatment.PE_gastrointestinal:
                        treatment.PE_gastrointestinal = treatment.standard_PE_results.PE_gastrointestinal
                    if not treatment.PE_GU:
                        treatment.PE_GU = treatment.standard_PE_results.PE_GU
                    if not treatment.PE_musculoskeletal:
                        treatment.PE_musculoskeletal = treatment.standard_PE_results.PE_musculoskeletal
                    if not treatment.PE_skin_and_nodes:
                        treatment.PE_skin_and_nodes = treatment.standard_PE_results.PE_skin_and_nodes
                    if not treatment.PE_neurologic:
                        treatment.PE_neurologic = treatment.standard_PE_results.PE_neurologic
                    if not treatment.PE_psyche:
                        treatment.PE_psyche = treatment.standard_PE_results.PE_psyche
                treatment=form.save(commit = False)           
            encounter = Encounter.objects.get(pk=encounterid)
            treatment.encounter = encounter
            if treatment.patient.pk != treatment.encounter.patient.pk:
                return HttpResponse('ERROR: The patient for the treatment is different than the patient for the encounter. This is usually caused by a user manually modifying the page URL. Please use the "Back" button to return to the patient encounter to access the assessment list through the proper encounter.')
            treatment.date = timezone.now()
            treatment.owner = request.user
            treatment.save()
            for assessment in treatment.assessments.all():
                encounter.assessment_set.add(assessment)
            encounter.save()
            if assessmentid:
                if treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION:
                    return redirect('edit_dosage', encounterid=encounterid, assessmentid=assessmentid, pk=treatment.id)
                else:
                    return redirect('treatment_detail',encounterid=encounterid, assessmentid=assessmentid, pk=treatment.id)
            else:
                if treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION:
                    return redirect('edit_encounter_dosage', encounterid=encounterid, pk=treatment.id)
                else:
                    return redirect('encounter_treatment_detail', encounterid=encounterid, pk=treatment.id)
    else:
        if treatment.treatment_option.type in treatment.treatment_option.NOTE:
            form = NoteModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.LAB:
            form = LabModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.IN_HOUSE_LAB:
            form = InHouseLabModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.VITALS:
            form = VitalsModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.PHYSICAL_EXAM:
            form = PEModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.HPI:
            form = HPIModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION:
            form = PrescriptionModelForm(instance=treatment)
            form.fields['drug'].queryset = treatment.treatment_option.drugs.all()
            form.fields['drug'].required = True
            form.fields['drug_admin_option'].queryset = treatment.treatment_option.drug_admins.all()
            form.fields['drug_admin_option'].required = True
        if treatment.treatment_option.type in treatment.treatment_option.VACCINE:
            form = VaccineModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.FOLLOW_UP:
            form = FollowUpModelForm(instance=treatment)
        if treatment.treatment_option.type in treatment.treatment_option.ALLERGY:
            form = AllergyModelForm(instance=treatment)
        form.fields['assessments'].queryset = Assessment.objects.filter(patient = treatment.patient)
        form.fields['assessments'].help_text = 'Hold ctrl or command to select multiple assessments'
    saved_text_responses = SavedTextResponse.objects.filter(user = request.user).filter(treatment_option = treatment.treatment_option)
    return render(request, 'pppcemr/treatment_edit.html', {'form':form, 'treatment':treatment, 'saved_text_responses':saved_text_responses})

def edit_dosage(request, encounterid=None, assessmentid=None, pk=None):
    treatment = Treatment.objects.get(id=pk)
    if treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION:
        #treatment.calculated_dose = treatment.drug.concentration_numerator * treatment.drug_admin_option.dose
        treatment.calculated_dose = treatment.compute_dose()
        treatment.dose_unit = treatment.drug.get_concentration_denominator_unit()
        treatment.route = treatment.drug.route
        treatment.frequency = treatment.drug_admin_option.frequency
        treatment.duration = treatment.drug_admin_option.duration_days
        treatment.pharmacist_instruction  = treatment.drug_admin_option.pharmacist_instruction
        treatment.patient_instruction  = treatment.drug_admin_option.patient_instruction
        treatment.dispense_amount = treatment.calculated_dose*treatment.get_admins_per_day()*treatment.duration
        treatment.dispense_unit = treatment.dose_unit
        treatment.save()
        if request.method == "POST":
            form = PrescriptionDoseModelForm(request.POST, instance=treatment)
            form.fields['drug_package'].queryset = DrugPackage.objects.filter(product_id = treatment.drug.product_id)
            if form.is_valid():
                treatment=form.save()
                if assessmentid:
                    return redirect('treatment_detail',encounterid=encounterid, assessmentid=assessmentid, pk=treatment.id)
                else:
                    return redirect('encounter_treatment_detail', encounterid=encounterid, pk=treatment.id)
        else:
            form = PrescriptionDoseModelForm(instance=treatment)
            form.fields['drug_package'].queryset = DrugPackage.objects.filter(product_id = treatment.drug.product_id)
        return render(request, 'pppcemr/treatment_edit.html', {'form':form, 'treatment':treatment})
    else:
        return redirect(request.META.get('HTTP_REFERER'), '/')
    
def add_treatment(request, encounterid=None, assessmentid=None, pk=None):
    treatment = Treatment.objects.get(id=pk)
    treatment_option_old = treatment.treatment_option
    treatment.pk = None
    treatment.id = None
    treatment.save()
    treatment.diagnosis = None
    treatment.treatment_option = treatment_option_old
    treatment.date = timezone.now()
    treatment.encounter = Encounter.objects.get(pk=encounterid)
    treatment.patient = treatment.encounter.patient
    treatment.owner = request.user
    if assessmentid:
        treatment.assessments.add(Assessment.objects.get(id=assessmentid))
    treatment.is_open = True
    treatment.description = '%s: %s' % (treatment.treatment_option.name, treatment.results)
    treatment.save()
    process_new_treatment(treatment)
    if treatment.treatment_option.type in (treatment.treatment_option.LAB, treatment.treatment_option.IN_HOUSE_LAB,
                                           treatment.treatment_option.VITALS, treatment.treatment_option.TEST,
                                           treatment.treatment_option.VACCINE, treatment.treatment_option.NOTE,
                                           treatment.treatment_option.FOLLOW_UP):
        if assessmentid:
            return redirect('encounter_assessment_detail', encounterid=encounterid, pk=assessmentid)
        else:
            return redirect('encounter_detail', pk=treatment.encounter.id)
    else:
        if assessmentid:
            return redirect('edit_treatment', encounterid=encounterid, assessmentid=assessmentid, pk=treatment.id)
        else:
            return redirect('edit_encounter_treatment', encounterid=encounterid, pk=treatment.id)
    return redirect(request.META.get('HTTP_REFERER'), '/')

def close_treatment(request, encounterid=None, assessmentid=None, pk=None):
    treatment = Treatment.objects.get(id=pk)
    treatment.is_open = False
    treatment.date_closed = timezone.now()
    treatment.save()
    if assessmentid:
        anchor = '#a%s'% assessmentid
    elif treatment.treatment_option.type in treatment.treatment_option.PRESCRIPTION:
        anchor = '#medications'
    else:
        anchor = '#encounter_treatments'
    return redirect(request.META.get('HTTP_REFERER')+anchor, '/')

def reopen_treatment(request, encounterid=None, assessmentid=None, pk=None):
    treatment = Treatment.objects.get(id=pk)
    treatment.is_open = True
    treatment.save()
    return redirect(request.META.get('HTTP_REFERER'), '/')

def attach_file(request, encounterid = None, assessmentid = None, treatmentid = None):
    treatment = Treatment.objects.get(id=treatmentid)
    if request.method == 'POST':
        form = UploadAttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            #attachment = FileAttachment(name=file_attachment=request.FILES['file_attachment'], treatment=treatment)
            attachment.treatment = treatment
            attachment.date = timezone.now()
            attachment.save()
            if assessmentid:
                return redirect('treatment_detail',encounterid=encounterid, assessmentid=assessmentid, pk=treatment.id)
            else:
                return redirect('encounter_treatment_detail', encounterid=encounterid, pk=treatment.id)
    else:
        form = UploadAttachmentForm()
    return render(request, 'pppcemr/attach_file.html', {'form': form, 'treatment':treatment})

def new_task(request, encounterid=None, assessmentid=None, treatmentid=None):
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.date = timezone.now()
            if encounterid:
                task.encounter = Encounter.objects.get(pk=encounterid)
                task.patient = task.encounter.patient
            task.sender = request.user
            if treatmentid:
                task.treatment = Treatment.objects.get(pk=treatmentid)
            if task.owner:
                task.color = task.owner.employee.color
            if task.owner_group:
                if task.owner:
                    task.owner = None  # Owner group supersedes single owner.
                task.color = task.owner_group.employeegroup.color
            task.is_open = True
            task.save()
            if task.treatment:
                if assessmentid:
                    return redirect('treatment_detail', encounterid=encounterid, assessmentid=assessmentid, pk=treatmentid)
                return redirect('encounter_treatment_detail', encounterid=encounterid, pk=treatmentid)
            if task.encounter:
                return redirect('encounter_detail', pk=encounterid)
            return redirect('index')
    else:
        form = TaskModelForm()
    return render(request, 'pppcemr/task_edit.html', {'form':form})

def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.date = timezone.now()
            task.sender = request.user
            if task.owner:
                task.color = task.owner.employee.color
            if task.owner_group:
                if task.owner:
                    task.owner = None  # Owner group supersedes single owner.
                task.color = task.owner_group.employeegroup.color
            task.save()
            if task.treatment:
                if task.treatment.assessment:
                    return redirect('treatment_detail', encounterid=task.treatment.encounter.id, assessmentid=task.treatment.assessment.id, pk=task.treatment.id)
                return redirect('encounter_treatment_detail', encounterid=task.treatment.encounter.id, pk=task.treatment.id)
            if task.encounter:
                return redirect('encounter_detail', pk=task.encounter.id)
            return redirect('index')
    else:
        form = TaskModelForm(instance=task)
    return render(request, 'pppcemr/task_edit.html', {'form':form})

def close_task(request, pk=None):
    task = Task.objects.get(id=pk)
    task.is_open = False
    task.date_closed = timezone.now()
    task.save()
    return redirect(request.META.get('HTTP_REFERER')+'#tasks', '/')

def reopen_task(request, pk=None):
    task = Task.objects.get(id=pk)
    task.is_open = True
    task.save()
    return redirect(request.META.get('HTTP_REFERER'), '/')

def close_message(request, pk):
    message = Message.objects.get(id=pk)
    message.is_open = False
    message.date_closed = timezone.now()
    message.save()
    return redirect('message_list')

def reopen_message(request, pk):
    message = Message.objects.get(id=pk)
    message.is_open = True
    message.save()
    return redirect('message_list')

def send_message(request, encounterid=None, assessmentid=None, treatmentid=None):
    if request.method == "POST":
        form = MessageModelForm(request.POST)
        form.fields['recipient_users_list'].help_text = "Hold Ctrl or Command to select multiple."
        form.fields['recipient_groups_list'].help_text = "Hold Ctrl or Command to select multiple."
        if form.is_valid():
            for user in form.cleaned_data['recipient_users_list']:
                create_message(request,encounterid, assessmentid, treatmentid, user, form)
            for group in form.cleaned_data['recipient_groups_list']:
                for user in group.user_set.all():
                    create_message(request, encounterid, assessmentid, treatmentid, user, form)
            if treatmentid:
                if assessmentid:
                    return redirect('treatment_detail', encounterid=encounterid, assessmentid=assessmentid, pk=treatmentid)
                return redirect('encounter_treatment_detail', encounterid=encounterid, pk=treatmentid)
            if assessmentid:
                return redirect('encounter_assessment_detail', encounterid=encounterid, pk=assessmentid)
            if encounterid:
                return redirect('encounter_detail', pk=encounterid)
            return redirect('message_list')
    else:
        form = MessageModelForm()
        form.fields['recipient_users_list'].help_text = "Hold Ctrl or Command to select multiple."
        form.fields['recipient_groups_list'].help_text = "Hold Ctrl or Command to select multiple."
    return render(request, 'pppcemr/message_edit.html', {'form':form})

def reply_message(request,pk):
    message = Message.objects.get(id=pk)
    message.pk = None
    message.save()
    message.recipient = message.sender
    message.recipient_users_list.clear()
    message.recipient_users_list.add(message.sender)
    message.recipient_groups_list.clear()
    message.sender = request.user
    message.body = '\n---\nReply to: %s \n %s' % (message.recipient.get_full_name(), message.body)
    message.save()
    if message.encounter:
        encounterid = message.encounter.id
    else:
        encounterid = None
    if message.assessment:
        assessmentid = message.assessment.id
    else:
        assessmentid = None
    if message.treatment:
        treatmentid = message.treatment.id
    else:
        treatmentid = None
    if request.method == "POST":
        form = MessageModelForm(request.POST, instance=message)
        form.fields['recipient_users_list'].help_text = "Hold Ctrl or Command to select multiple."
        form.fields['recipient_groups_list'].help_text = "Hold Ctrl or Command to select multiple."
        if form.is_valid():
            for user in form.cleaned_data['recipient_users_list']:
                create_message(request, encounterid, assessmentid, treatmentid, user, form)
            for group in form.cleaned_data['recipient_groups_list']:
                for user in group.user_set.all():
                    create_message(request, encounterid, assessmentid, treatmentid, user, form)
            return redirect('message_detail', pk=pk)
    else:
        form = MessageModelForm(instance=message)
        form.fields['recipient_users_list'].help_text = "Hold Ctrl or Command to select multiple."
        form.fields['recipient_groups_list'].help_text = "Hold Ctrl or Command to select multiple."
    return render(request, 'pppcemr/message_edit.html', {'form':form})

def forward_message(request,pk):
    message = Message.objects.get(id=pk)
    original_sender = message.sender
    message.pk = None
    message.save()
    message.recipient_users_list.clear()
    message.recipient_groups_list.clear()
    message.sender = request.user
    message.body = '\n---\nForwarded Message: %s \n %s' % (original_sender.get_full_name(), message.body)
    message.save()
    if message.encounter:
        encounterid = message.encounter.id
    else:
        encounterid = None
    if message.assessment:
        assessmentid = message.assessment.id
    else:
        assessmentid = None
    if message.treatment:
        treatmentid = message.treatment.id
    else:
        treatmentid = None
    if request.method == "POST":
        form = MessageModelForm(request.POST, instance=message)
        form.fields['recipient_users_list'].help_text = "Hold Ctrl or Command to select multiple."
        if form.is_valid():
            for user in form.cleaned_data['recipient_users_list']:
                create_message(request, encounterid, assessmentid, treatmentid, user, form)
            for group in form.cleaned_data['recipient_groups_list']:
                for user in group.user_set.all():
                    create_message(request, encounterid, assessmentid, treatmentid, user, form)
            return redirect('message_detail', pk=pk)
    else:
        form = MessageModelForm(instance=message)
        form.fields['recipient_users_list'].help_text = "Hold Ctrl or Command to select multiple."
        form.fields['recipient_groups_list'].help_text = "Hold Ctrl or Command to select multiple."
    return render(request, 'pppcemr/message_edit.html', {'form':form})

def create_message(request, encounterid=None, assessmentid=None, treatmentid=None, user = None, form = None):
    message = form.save(commit=False)
    message.recipient = user
    message.date = timezone.now()
    if encounterid:
        message.encounter = Encounter.objects.get(pk=encounterid)
        message.patient = message.encounter.patient
    message.sender = request.user
    if assessmentid:
        message.assessment = Assessment.objects.get(pk=assessmentid)
        message.patient = message.assessment.patient
    if treatmentid:
        message.treatment = Treatment.objects.get(pk=treatmentid)
        message.patient = message.treatment.patient
    message.is_open = True
    message.save()
    form.save_m2m()
    # str = "Created message ID = %s for recipient %s, user list %s" % (
    # message.id, message.recipient, message.recipient_users_list.all())
    # print (str)
    message.id = None

def add_workplan(request, pk): # pk refers to encounter key
    encounter = Encounter.objects.get(id=pk)
    if request.method == "POST":
        encounterform = AddWorkplanModelForm(request.POST, instance=encounter)
        if encounterform.is_valid():
            encounter = encounterform.save(commit=False)
            encounter.save()
            apply_workplan(encounter)
            return redirect('encounter_detail', pk=encounter.id)
    else:
        encounterform = AddWorkplanModelForm(instance=encounter)
    return render(request, 'pppcemr/encounter_edit.html', {'form':encounterform})

def choose_encounter_report(request, encounterid):
    if request.method == "POST":
        form = ChooseReportForm(request.POST)
        form.fields['report'].queryset = Report.objects.filter(type = 'ER')
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data['report'].id)
            return redirect('view_encounter_report', encounterid = encounterid, pk =form.cleaned_data['report'].id )
    else:
        form = ChooseReportForm()
        form.fields['report'].queryset = Report.objects.filter(type = 'ER')
    return render(request, 'pppcemr/choose_report.html',{'form':form})


def view_encounter_report(request, encounterid, pk):
    encounter = Encounter.objects.get(pk = encounterid)
    report = Report.objects.get(pk=pk)
    encounter_template = Template(report.report_template)
    context = Context({'encounter':encounter,})
    return HttpResponse(encounter_template.render(context))


def create_encounter_summary(encounter):
    preferences = PracticePreferences.objects.get(pk=1)
    report = preferences.encounter_summary_report
    encounter_template = Template(report.report_template)
    context = Context({'encounter':encounter,})
    encounter.final_summary = encounter_template.render(context)
    encounter.save()


def view_encounter_summary(request,pk):
    encounter = Encounter.objects.get(pk = pk)
    return HttpResponse(encounter.final_summary)


def choose_treatment_report(request, treatmentid):
    if request.method == "POST":
        form = ChooseReportForm(request.POST)
        form.fields['report'].queryset = Report.objects.filter(type = 'TR')
        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data['report'].id)
            return redirect('view_treatment_report', treatmentid = treatmentid, pk =form.cleaned_data['report'].id )
    else:
        form = ChooseReportForm()
        form.fields['report'].queryset = Report.objects.filter(type = 'TR')
    return render(request, 'pppcemr/choose_report.html',{'form':form})

def view_treatment_report(request, treatmentid, pk):
    treatment = Treatment.objects.get(pk = treatmentid)
    report = Report.objects.get(pk=pk)
    encounter_template = Template(report.report_template)
    context = Context({'treatment':treatment,})
    return HttpResponse(encounter_template.render(context))



def apply_workplan(encounter):
    if encounter.workplan:
        for assessment_step in encounter.workplan.workplanstepaddassessment_set.all():
            assessment = Assessment()
            assessment.diagnosis = assessment_step.diagnosis
            assessment.assessment_date = timezone.now()
            assessment.patient = encounter.patient
            assessment.owner = encounter.encounter_owner
            assessment.is_open = True
            assessment.save()
            assessment.encounters.add(encounter)
        for treatment_step in encounter.workplan.workplanstepaddtreatment_set.all():
            treatment = Treatment()
            treatment.encounter = encounter
            treatment.patient = encounter.patient
            treatment.treatment_option = treatment_step.treatment_option
            treatment.date = timezone.now()
            treatment.owner = encounter.encounter_owner
            treatment.is_open = True
            treatment.save()
            process_new_treatment(treatment)
        for task_step in encounter.workplan.workplanstepaddtask_set.all():
            task = Task()
            task.encounter = encounter
            task.patient = encounter.patient
            task.subject = task_step.subject
            task.body = task_step.body
            task.date = timezone.now()
            if task_step.encounter_owner_task:
                task.owner = encounter.encounter_owner
                task.color = task.owner.employee.color
            elif task_step.owner_group:
                task.owner_group = task_step.owner_group
                task.color = task.owner_group.employeegroup.color
            else:
                task.owner = task_step.owner
                task.color = task.owner.employee.color
            task.save()


def generate_nurse_task(treatment, task_text):
    task = Task()
    task.patient = treatment.patient
    task.encounter = treatment.encounter
    task.treatment = treatment
    task.date = treatment.date
    task.is_open = True
    task.subject = task_text
    task.sender = treatment.owner
    preferences = PracticePreferences.objects.get(pk=1)
    task.owner_group = preferences.group_to_receive_new_lab_tasks
    task.color = task.owner_group.employeegroup.color
    task.save()

def generate_owner_task(treatment, task_text):
    task = Task()
    task.patient = treatment.patient
    task.encounter = treatment.encounter
    task.treatment = treatment
    task.date = treatment.date
    task.is_open = True
    task.subject = task_text
    task.sender = treatment.owner
    task.owner = treatment.owner
    task.color = task.owner.employee.color
    task.save()

def generate_office_task(treatment, task_text):
    task = Task()
    task.patient = treatment.patient
    task.encounter = treatment.encounter
    task.treatment = treatment
    task.date = treatment.date
    task.is_open = True
    task.subject = task_text
    task.sender = treatment.owner
    preferences = PracticePreferences.objects.get(pk=1)
    task.owner_group = preferences.group_to_receive_new_office_tasks
    task.color = task.owner_group.employeegroup.color
    task.save()

def process_new_treatment(treatment):
    treatment.description = treatment.treatment_option.name
    treatment.save()
    if treatment.treatment_option.type in treatment.treatment_option.LAB:
        generate_nurse_task(treatment, 'Order Lab: %s' % (treatment.description))
    elif treatment.treatment_option.type in treatment.treatment_option.IN_HOUSE_LAB:
        generate_nurse_task(treatment, 'Enter Results: %s' % (treatment.description))
    elif treatment.treatment_option.type in treatment.treatment_option.VITALS:
        generate_nurse_task(treatment, 'Enter Vitals')
    elif treatment.treatment_option.type in treatment.treatment_option.TEST:
        generate_nurse_task(treatment, 'Enter Test Results: %s' % (treatment.description))
    elif treatment.treatment_option.type in treatment.treatment_option.PHYSICAL_EXAM:
        generate_owner_task(treatment,'Enter Physical Exam')
    elif treatment.treatment_option.type in treatment.treatment_option.HPI:
        generate_owner_task(treatment,'Enter HPI')
    elif treatment.treatment_option.type in treatment.treatment_option.VACCINE:
        generate_nurse_task(treatment,'Administer Vaccine: %s' % (treatment.description))
    elif treatment.treatment_option.type in treatment.treatment_option.FOLLOW_UP:
        generate_office_task(treatment, 'Follow Up: %s' % (treatment.description))
    else:
        pass
    
# def add_breadcrumb_history(request):
#     history = request.path
# 
#     self.request.session['breadcrumb_history'] = history
# 
#     return history
