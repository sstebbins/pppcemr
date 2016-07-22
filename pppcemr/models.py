from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from datetime import date
from django.core.urlresolvers import reverse
from django.db.models import F
from django.db.models import Q
from datetime import datetime, timedelta
import re
import math
from .growthcharts import *
from django.conf import settings
import random, string

def get_percentile_from_z_score(z_score):
    return round(.5 * (math.erf(z_score / 2 ** .5) + 1) * 100,1)

class Employee(models.Model):
    user = models.OneToOneField(User)
    color = models.CharField(max_length=100)
    def __str__(self):
        return '%s' %(self.user)
    def get_open_tasks(self):
        return self.user.task_owners.all().filter(is_open = True)
    def get_open_messages(self):
        return Message.objects.filter(recipient = self.user).filter(is_open=True)


class EmployeeGroup(models.Model):
    group = models.OneToOneField(Group)
    color = models.CharField(max_length=100)
    def __str__(self):
        return '%s' %(self.group)
    def get_open_tasks(self):
        return self.group.task_set.all().filter(is_open = True)

class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField('birthdate')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_history = models.TextField(null=True, blank=True)
    past_medical_history = models.TextField(null=True, blank=True)
    family_history = models.TextField(null=True, blank=True)
    social_history = models.TextField(null=True, blank=True)
    def get_age_in_months(self):
        print('finding age in months')
        return (timezone.now().date() - self.birthdate).total_seconds()/2635200
    def get_last_weight_kg(self):
        treatment_set = Treatment.objects.filter(patient=self).exclude(weight_kg = None).order_by('-id')[:1]
        if treatment_set.count()>0:
            treatment = treatment_set.first()
            return float(treatment.weight_kg)
        else:
            return 0
    def get_last_weight_and_percentile(self):
        treatment_set = Treatment.objects.filter(patient=self).exclude(weight_kg = None).order_by('-id')[:1]
        if treatment_set.count()>0:
            treatment = treatment_set.first()
            result_string = ''
            if settings.USE_SI:
                result_string = '%skg' % (treatment.weight_kg)
            else:
                if treatment.weight_lb:
                    result_string =  '%slb ' % (treatment.weight_lb)
                if treatment.weight_oz:
                    result_string += '%soz' % (treatment.weight_oz)
                result_string += '(%skg)' % (treatment.weight_kg)
            result_string += ' (%s%%) on %s' % (treatment.get_weight_percentile(), treatment.date.strftime('%Y-%m-%d'))
            return result_string
        else:
            return "no weigths recorded"
    def get_last_height_and_percentile(self):
        treatment_set = Treatment.objects.filter(patient=self).exclude(height_cm = None).order_by('-id')[:1]
        if treatment_set.count()>0:
            treatment = treatment_set.first()
            result_string = ''
            if settings.USE_SI:
                result_string = '%cm' % (treatment.height_cm)
            else:
                result_string =  '%sin ' % (treatment.height)
            result_string += ' (%s%%) on %s' % (treatment.get_height_percentile(), treatment.date.strftime('%Y-%m-%d'))
            return result_string
        else:
            return "no heights recorded"
    def get_last_bmi_and_percentile(self):
        treatment_set = Treatment.objects.filter(patient=self).exclude(height_cm = None).exclude(weight_kg = None).order_by('-id')[:1]
        if treatment_set.count()>0:
            treatment = treatment_set.first()
            result_string = 'BMI: %s' % round((treatment.weight_kg/((treatment.height_cm/100)**2)),2)
            result_string += ' (%s%%) on %s' % (treatment.get_bmi_percentile(), treatment.date.strftime('%Y-%m-%d'))
            return result_string
        else:
            return "no heights recorded"
    def get_weights(self):
        return Treatment.objects.filter(patient=self).exclude(weight_kg = None)
    def get_heights(self):
        return Treatment.objects.filter(patient=self).exclude(height_cm = None)
    def get_weights_and_heights(self):
        return Treatment.objects.filter(patient=self).exclude(height_cm = None).exclude(weight_kg = None)
    def __str__(self):
        return '%s, %s (%s) (%s)' % (self.last_name, self.first_name, self.birthdate, self.gender)
    def close_autoclose_assessments(self):
        assessment_set = Assessment.objects.filter(patient=self).filter(auto_close = True)
        for assessment in assessment_set:
            assessment.is_open = False
            assessment.date_closed = timezone.now()
            assessment.save()
        return True
    def get_all_open_medications(self):
        return Treatment.objects.filter(patient=self).filter(is_open = True).filter(treatment_option__type__iexact = 'RX')
    def get_all_open_allergies(self):
        return Treatment.objects.filter(patient=self).filter(is_open=True).filter(treatment_option__type__iexact='AL')

class Office(models.Model):
    name = models.CharField(max_length=50)
    def get_open_user_tasks(self):
        office_tasks = Task.objects.filter(encounter__room__office_id=self.pk).filter(is_open=True)
        return office_tasks
    def get_open_user_tasks_count(self, user):
        count = Task.objects.filter(encounter__room__office_id=self.pk).filter(is_open=True).filter(owner=user).count()
        return count
    def get_encounters_in_waiting_room(self):
        return Encounter.objects.filter(room__type__icontains = 'W').filter(is_open = True)
    def __str__(self):
        return self.name

class Room(models.Model):
    EXAM = 'E'
    CHART = 'C'
    TELEPHONE = 'T'
    WAITING = 'W'
    ROOM_TYPE_CHOICES = (
        (EXAM,'Exam Room'),
        (CHART,'Chart Room'),
        (TELEPHONE,'Telephone Room'),
        (WAITING,'Waiting Room'),
    )
    name = models.CharField(max_length=20)
    office = models.ForeignKey(Office)
    type = models.CharField(max_length=1,choices = ROOM_TYPE_CHOICES)
    def __str__(self):
        return '%s %s' % (self.office.name, self.name)



class Workplan(models.Model):
    name = models.CharField(max_length=300)
    is_well = models.BooleanField(default=True)
    min_age_months = models.FloatField(null=True, blank=True)
    max_age_months = models.FloatField(null=True, blank=True)
    def __str__(self):
        return '%s' % (self.name)

class EncounterType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    is_well = models.BooleanField(default=False)
    is_direct = models.BooleanField(default=True)
    is_billed = models.BooleanField(default=True)
    default_workplan = models.ForeignKey(Workplan, null=True, blank=True)
    def __str__(self):
        return '%s' % (self.name)

class Encounter(models.Model):
    EM_CHOICES = (
        ('0','No sick bill'),
        ('1','Level 1'),
        ('2','Level 2'),
        ('3','Level 3'),
        ('4','Level 4'),
        ('5','Level 5'),
        )
    EM_level = models.CharField(max_length=1, choices=EM_CHOICES, null=True, blank=True)
    patient = models.ForeignKey(Patient)
    encounter_owner = models.ForeignKey(User)
    room = models.ForeignKey(Room, null=True, blank=True)
    office = models.ForeignKey(Office, null=True, blank=True)
    encounter_type = models.ForeignKey(EncounterType)
    encounter_date = models.DateTimeField('date and time of encounter')
    is_open = models.BooleanField(default=True)
    is_billed = models.BooleanField(default=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    workplan = models.ForeignKey(Workplan, null=True, blank=True)
    final_summary = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['-encounter_date']
    def get_absolute_url(self):
        return reverse('encounter_detail', kwargs={'pk':str(self.id)})
    def __str__(self):
        if self.is_open:
            return '%s %s %s' % (self.encounter_date.strftime('%Y-%m-%d'), self.patient, self.encounter_type)
        else:
            return '(CLOSED) %s %s %s ' % (self.encounter_date.strftime('%Y-%m-%d'), self.patient, self.encounter_type)
    def close(self):
        self.is_open = False
        self.date_closed = timezone.now()
    def apply_correct_well_workplan(self):
        print('Attempting to find correct well workplan:')
        self.workplan = Workplan.objects.filter(is_well = True).filter(min_age_months__lt = self.patient.get_age_in_months()).filter(max_age_months__gt = self.patient.get_age_in_months()).first()
        print(self.workplan)
    def get_previous_open_assessments(self):
        return self.patient.assessment_set.all().filter(Q(date_closed = None) | Q(date_closed__gt = self.encounter_date)).filter(assessment_date__lt = (self.encounter_date))
    def get_previous_closed_assessments(self):
        return self.patient.assessment_set.all().exclude(
            date_closed__gt=self.encounter_date+timedelta(days=1)).filter(
            assessment_date__lt=(self.encounter_date))



class Snomed(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=100)
    icd_equivalents = models.CharField(max_length=500)
    def __str__(self):
        return '%s %s' % (self.code, self.name)

class Diagnosis(models.Model):
    class Meta:
        verbose_name_plural = "diagnoses"
    icd_code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    user_description = models.CharField(max_length=200, null=True, blank=True)
    date_last_used = models.DateTimeField('date last used', null=True, blank=True)
    default_snomed = models.ForeignKey(Snomed, null=True, blank=True)
    auto_close = models.BooleanField(default=False)
    def __str__(self):
        return '%s %s' % (self.icd_code, self.description)

class Assessment(models.Model):
    patient = models.ForeignKey(Patient)
    encounters = models.ManyToManyField(Encounter)
    diagnosis = models.ForeignKey(Diagnosis)
    snomed = models.ForeignKey(Snomed, null=True, blank=True)
    assessment_date = models.DateTimeField('date and time of assessment')
    is_open = models.BooleanField(default=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    auto_close = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, blank=True)
    class Meta:
        ordering = ['-assessment_date']
    def __str__(self):
        if self.is_open:
            return '%s: %s' % (self.assessment_date.strftime('%Y-%m-%d'), self.diagnosis)
        else:
            return '(CLOSED) %s: %s ' % (self.assessment_date.strftime('%Y-%m-%d'), self.diagnosis)

class Drug(models.Model):
    trade_name = models.CharField(max_length=500)
    generic_name = models.CharField(max_length=500)
    product_id = models.CharField(max_length=100)
    product_ndc = models.CharField(max_length=25)
    dosage_form = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    concentration_numerator = models.CharField(max_length=25)
    concentration_denominator = models.CharField(max_length=25)
    dea = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return '%s (%s) %s%s %s %s' % (self.trade_name, self.generic_name, self.concentration_numerator,
                                 self.concentration_denominator, self.dosage_form, self.route)
    def get_concentration_denominator_float(self):
        return float(re.findall(r'\d+', self.concentration_denominator)[0])
    def get_concentration_numerator_float(self):
        return float(self.concentration_numerator)
    def get_concentration_numerator_unit(self):
        return re.sub('\d+','', self.concentration_denominator).split('/')[0]
    def get_concentration_denominator_unit(self):
        unit = re.sub('\d+','', self.concentration_denominator).split('/')[1]
        if len(unit)<1:
            unit = self.dosage_form
        return unit


class DrugAdminOption(models.Model):
    name = models.CharField(max_length=20)
    FREQUENCY_CHOICES = (
        ('Daily','Daily'),
        ('Daily PRN','Daily PRN'),
        ('BID','BID'),
        ('BID PRN','BID PRN'),
        ('TID','TID'),
        ('TID PRN','TID PRN'),
        ('QID', 'QID'),
        ('QID PRN', 'QID PRN'),
        ('Q2H', 'Q2H'),
        ('Q2H PRN', 'Q2H PRN'),
        ('Q4H', 'Q4H'),
        ('Q4H PRN', 'Q4H PRN'),
        ('Q6H', 'Q6H'),
        ('Q6H PRN', 'Q6H PRN'),
        ('Q8H', 'Q8H'),
        ('Q8H PRN', 'Q8H PRN'),
        ('Q12H', 'Q12H'),
        ('Q12H PRN', 'Q12H PRN'),
        ('ASDIR', 'As Directed'),
        )
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    dose = models.FloatField(default=0)
    patient_instruction = models.CharField(max_length=100, null=True, blank=True)
    pharmacist_instruction = models.CharField(max_length=100, null=True, blank=True)
    multiply_by_weight = models.BooleanField(default=True)
    dose_per_day = models.BooleanField(default=True)
    duration_days = models.IntegerField(default=0)
    def __str__(self):
        return '%s' % (self.name)

class TreatmentOption(models.Model):
    name = models.CharField(max_length=100)
    default_result = models.TextField(null=True, blank=True)
    NOTE = 'NT'
    LAB = 'LB'
    IN_HOUSE_LAB = 'IL'
    VITALS = 'VI'
    PRESCRIPTION = 'RX'
    PROCEDURE = 'PR'
    TEST = 'TS'
    HPI = 'HP'
    PHYSICAL_EXAM = 'PE'
    PFSH = 'PF'
    FOLLOW_UP = 'FU'
    VACCINE = 'VA'
    ALLERGY = 'AL'
    TREATMENT_TYPE_CHOICES = (
        (NOTE, 'Note'),
        (LAB, 'Lab'),
        (IN_HOUSE_LAB, 'In House Lab'),
        (VITALS, 'Vital Signs'),
        (PRESCRIPTION, 'Drug Prescription'),
        (PROCEDURE, 'Procedure'),
        (TEST, 'Test'),
        (HPI, 'HPI and ROS'),
        (PHYSICAL_EXAM, 'Physical Exam'),
        (PFSH,'PFSH'),
        (FOLLOW_UP, 'Follow-up Instructions'),
        (VACCINE, 'Vaccine / Immunization'),
        (ALLERGY, 'Drug Allergy'),
        )
    type = models.CharField(max_length=2, choices= TREATMENT_TYPE_CHOICES, default=NOTE)
    date_last_used = models.DateTimeField('date last used', null=True, blank=True)
    # Drug Options
    drugs = models.ManyToManyField(Drug, blank=True)
    drug_admins = models.ManyToManyField(DrugAdminOption, blank=True)
    # Vaccine Options
    vaccine_manufacturer = models.CharField(max_length=20, null=True, blank=True)
    # Drug Allergy options
    drug_allergy_cross_reactions = models.CharField(max_length=500, null=True, blank=True,
                                                    help_text = 'Other medications that will react - separate with spaces')
    class Meta:
        verbose_name = "treatment option"
    def __str__(self):
        if self.type in self.ALLERGY:
            return 'Allergy: %s' % (self.name)
        else:
            return '%s' % (self.name)
    def is_physical(self):
        if self.type in self.PHYSICAL_EXAM:
            return True
        else:
            return False
    def is_prescription(self):
        if self.type in self.PRESCRIPTION:
            return True
        else:
            return False

class SavedTextResponse(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    treatment_option = models.ForeignKey(TreatmentOption)
    def __str__(self):
        return '%s' % self.text


class StandardPhysicalResults(models.Model):
    name = models.CharField(max_length=100)
    PE_constitutional = models.CharField(max_length=200, null=True, blank=True)
    PE_head_and_face = models.CharField(max_length=200, null=True, blank=True)
    PE_eyes = models.CharField(max_length=200, null=True, blank=True)
    PE_ears = models.CharField(max_length=200, null=True, blank=True)
    PE_nose_mouth_and_throat = models.CharField(max_length=200, null=True, blank=True)
    PE_neck = models.CharField(max_length=200, null=True, blank=True)
    PE_chest_and_breast = models.CharField(max_length=200, null=True, blank=True)
    PE_respiratory = models.CharField(max_length=200, null=True, blank=True)
    PE_heart = models.CharField(max_length=200, null=True, blank=True)
    PE_pulses_vascular = models.CharField(max_length=200, null=True, blank=True)
    PE_gastrointestinal = models.CharField(max_length=200, null=True, blank=True)
    PE_GU = models.CharField(max_length=200, null=True, blank=True)
    PE_musculoskeletal = models.CharField(max_length=200, null=True, blank=True)
    PE_skin_and_nodes = models.CharField(max_length=200, null=True, blank=True)
    PE_neurologic = models.CharField(max_length=200, null=True, blank=True)
    PE_psyche = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Standard physical results"
    def __str__(self):
        return '%s' % (self.name)


class DrugPackage(models.Model):
    product_id = models.CharField(max_length=100)
    product_ndc = models.CharField(max_length=25)
    package_ndc = models.CharField(max_length=25)
    package_name = models.CharField(max_length=500)
    def __str__(self):
        return '%s' % (self.package_name)


    
class Treatment(models.Model):
    treatment_option = models.ForeignKey(TreatmentOption)
    description = models.CharField(max_length=100)
    results = models.TextField(null=True, blank=True)
    patient = models.ForeignKey(Patient, null=True, blank=True)
    encounter = models.ForeignKey(Encounter, null=True, blank=True)
    assessments = models.ManyToManyField(Assessment, blank=True)
    # For diagnosis treatment lists
    diagnosis = models.ForeignKey(Diagnosis, null=True, blank=True)
    date = models.DateTimeField('date and time of treatment', null=True, blank=True)
    is_open = models.BooleanField(default=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    next_page = models.URLField(null=True, blank=True)
    # Vitals
    chief_complaint = models.TextField(null=True, blank=True)
    weight_lb = models.FloatField(null=True, blank=True, help_text="lb")
    weight_oz = models.FloatField(null=True, blank=True, help_text="oz")
    weight_kg = models.FloatField(null=True, blank=True, help_text="kg")
    height = models.FloatField(null=True, blank=True, help_text="in")
    height_cm = models.FloatField(null=True, blank=True, help_text="cm")
    temperature = models.FloatField(null=True, blank=True, help_text="F")
    temperature_location = models.CharField(max_length=20, null=True, blank=True)
    HR = models.IntegerField(null=True, blank=True, help_text = "BPM")
    RR = models.IntegerField(null=True, blank=True, help_text = "breaths per min")
    Systolic_BP = models.IntegerField(null=True, blank=True, help_text = "mmHg")
    Diastolic_BP = models.IntegerField(null=True, blank=True, help_text = "mmHg")
    BP_location = models.CharField(max_length=20,null=True, blank=True, help_text = "LA, RA, etc")
    # Physical Exam
    standard_PE_results = models.ForeignKey(StandardPhysicalResults, null=True, blank=True)
    PE_constitutional = models.CharField(max_length=200, null=True, blank=True)
    PE_head_and_face = models.CharField(max_length=200, null=True, blank=True)
    PE_eyes = models.CharField(max_length=200, null=True, blank=True)
    PE_ears = models.CharField(max_length=200, null=True, blank=True)
    PE_nose_mouth_and_throat = models.CharField(max_length=200, null=True, blank=True)
    PE_neck = models.CharField(max_length=200, null=True, blank=True)
    PE_chest_and_breast = models.CharField(max_length=200, null=True, blank=True)
    PE_respiratory = models.CharField(max_length=200, null=True, blank=True)
    PE_heart = models.CharField(max_length=200, null=True, blank=True)
    PE_pulses_vascular = models.CharField(max_length=200, null=True, blank=True)
    PE_gastrointestinal = models.CharField(max_length=200, null=True, blank=True)
    PE_GU = models.CharField(max_length=200, null=True, blank=True)
    PE_musculoskeletal = models.CharField(max_length=200, null=True, blank=True)
    PE_skin_and_nodes = models.CharField(max_length=200, null=True, blank=True)
    PE_neurologic = models.CharField(max_length=200, null=True, blank=True)
    PE_psyche = models.CharField(max_length=200, null=True, blank=True)
    # PFSH
    birth_history = models.TextField(null=True, blank=True)
    surgical_and_hospital_history = models.TextField(null=True, blank=True)
    past_medical_history = models.TextField(null=True, blank=True)
    family_history = models.TextField(null=True, blank=True)
    social_history = models.TextField(null=True, blank=True)
    # Prescription
    drug = models.ForeignKey(Drug, null=True, blank=True)
    drug_package = models.ForeignKey(DrugPackage, null=True, blank=True)
    drug_admin_option = models.ForeignKey(DrugAdminOption, null=True, blank=True)
    calculated_dose = models.FloatField(null=True, blank=True)
    dose_unit = models.CharField(max_length=10, null=True, blank=True)
    route = models.CharField(max_length=30, null=True, blank=True)
    frequency = models.CharField(max_length=20, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, help_text = "(days)")
    dispense_amount = models.FloatField(null=True, blank=True)
    dispense_unit = models.CharField(max_length=20, null=True, blank=True)
    patient_instruction = models.CharField(max_length=100, null=True, blank=True)
    pharmacist_instruction = models.CharField(max_length=100, null=True, blank=True)
    # Vaccine
    vaccine_lot_number = models.CharField(max_length = 20, null=True, blank=True)
    vaccine_site = models.CharField(max_length = 20, null=True, blank=True)
    # Drug Allergy
    allergic_reaction_symptoms = models.CharField(max_length = 100, null=True, blank=True)
    class Meta:
        ordering = ['-date']
    def __str__(self):
        if self.treatment_option.type in self.treatment_option.PHYSICAL_EXAM:
            self.description = ('Physical exam: \n'
                                         'Constitutional: %s \n'
                                         'Head & Face: %s \n'
                                         'Eyes: %s \n'
                                         'Ears: %s \n'
                                         'Nose, Mouth, and Throat: %s \n'
                                         'Neck: %s \n'
                                         'Chest and Breast: %s \n'
                                         'Respiratory: %s \n'
                                         'Heart: %s \n'
                                         'Pulses & Vascular: %s \n'
                                         'Gastrointestinal: %s \n'
                                         'GU: %s \n'
                                         'Musculoskeletal: %s \n'
                                         'Skin and Nodes: %s \n'
                                         'Neurologic: %s \n'
                                         'Psyche: %s \n'
                                         % (
                                self.PE_constitutional,
                                self.PE_head_and_face,
                                self.PE_eyes,
                                self.PE_ears,
                                self.PE_nose_mouth_and_throat,
                                self.PE_neck,
                                self.PE_chest_and_breast,
                                self.PE_respiratory,
                                self.PE_heart,
                                self.PE_pulses_vascular,
                                self.PE_gastrointestinal,
                                self.PE_GU,
                                self.PE_musculoskeletal,
                                self.PE_skin_and_nodes,
                                self.PE_neurologic,
                                self.PE_psyche,
                                ))
        elif self.treatment_option.type in self.treatment_option.VITALS:
            description = 'Vitals:\n'
            if self.chief_complaint:
                description += 'CC: %s; ' % self.chief_complaint
            if self.weight_kg:
                description +='Wt: %skg; ' % self.weight_kg
            if self.height:
                description +='Ht: %sin (%scm); ' % (self.height, self.height_cm)
            if self.temperature:
                description +='T: %s (%s); '%(self.temperature, self.temperature_location)
            if self.HR:
                description +='HR:(%s); ' % self.HR
            if self.Systolic_BP:
                description +='BP: %s/%s mmHg' % (self.Systolic_BP, self.Diastolic_BP)
            self.description = description
        elif self.treatment_option.type in self.treatment_option.PRESCRIPTION:
            if self.drug:
                self.description = '%s (%s) (%s%s) %s %s %s %s x %s days \n Dispense: %s%s (%s)' % (self.drug.trade_name,
                                                        self.drug.generic_name,
                                                        self.drug.concentration_numerator,
                                                        self.drug.concentration_denominator,
                                                        self.calculated_dose, self.dose_unit,
                                                        self.drug.route,
                                                        self.drug_admin_option.frequency,
                                                        self.duration, self.dispense_amount,
                                                        self.dispense_unit, self.drug_package)
            else:
                self.description = '*** %s' % (self.treatment_option.name)
            if self.pharmacist_instruction:
                self.description = '%s \n Pharmacist: %s' % (self.description, self.pharmacist_instruction)
            if self.patient_instruction:
                self.description = '%s \n Patient: %s' % (self.description, self.patient_instruction)
        elif self.treatment_option.type in self.treatment_option.VACCINE:
            self.description = '%s' % self.treatment_option.name
        elif self.treatment_option.type in self.treatment_option.ALLERGY:
            self.description = 'Allergy: %s' % self.treatment_option.name
        else:
            self.description = '%s:\n %s' % (self.treatment_option.name, self.results)
        if not self.date: # for use when used in treatment option lists under a diagnosis
            return '%s' % (self.description)
        if self.is_open:
            return '%s: %s' % (timezone.localtime(self.date).strftime('%Y-%m-%d'), self.description)
        else:
            return '(CLOSED) %s: %s ' % (timezone.localtime(self.date).strftime('%Y-%m-%d'), self.description)
    def has_no_assessment(self):
        if self.assessments.all().count()== 0:
            return True
        else:
            return False
    def has_no_open_assessment(self):
        if self.assessments.all().filter(is_open = True).count() == 0:
            return True
        else:
            return False
    def get_admins_per_day(self):
        admins_per_day = 1 #default
        if self.drug_admin_option.frequency== 'BID':
            admins_per_day = 2
        elif self.drug_admin_option.frequency== 'TID':
            admins_per_day = 3
        return admins_per_day
    def compute_dose(self):
        if self.treatment_option.type in self.treatment_option.PRESCRIPTION:
            dose =self.drug_admin_option.dose*self.drug.get_concentration_denominator_float()/self.drug.get_concentration_numerator_float()
            if self.drug_admin_option.dose_per_day:
                dose = dose/self.get_admins_per_day()
            if self.drug_admin_option.multiply_by_weight:
                dose = dose*self.patient.get_last_weight_kg()
            return round(dose,1)
        else:
            return "N/A"
    def get_weight_percentile(self):
        age_months= int((self.date.date() - self.patient.birthdate).total_seconds()/2635200)
        if self.patient.gender == 'M':
            L_weight = L_weight_male
            M_weight = M_weight_male
            S_weight = S_weight_male
        else:
            L_weight = L_weight_female
            M_weight = M_weight_female
            S_weight = S_weight_female
        if self.weight_kg and age_months <= 240:
            L = next(c for c in L_weight if c[0]==age_months)[1]
            M = next(c for c in M_weight if c[0]==age_months)[1]
            S = next(c for c in S_weight if c[0]==age_months)[1]
            Z = (((self.weight_kg/M)**L)-1)/(L*S)
            percentile = get_percentile_from_z_score(Z)
            return percentile
        else:
            return "N/A"
    def get_height_percentile(self):
        age_months= int((self.date.date() - self.patient.birthdate).total_seconds()/2635200)
        if self.patient.gender == 'M':
            L_height = L_height_male
            M_height = M_height_male
            S_height = S_height_male
        else:
            L_height = L_height_female
            M_height = M_height_female
            S_height = S_height_female
        if self.height_cm and age_months <= 240:
            L = next(c for c in L_height if c[0]==age_months)[1]
            M = next(c for c in M_height if c[0]==age_months)[1]
            S = next(c for c in S_height if c[0]==age_months)[1]
            Z = (((self.height_cm/M)**L)-1)/(L*S)
            percentile = get_percentile_from_z_score(Z)
            return percentile
        else:
            return "N/A"
    def get_bmi_percentile(self):
        age_months= int((self.date.date() - self.patient.birthdate).total_seconds()/2635200)
        if self.patient.gender == 'M':
            L_bmi = L_bmi_male
            M_bmi = M_bmi_male
            S_bmi = S_bmi_male
        else:
            L_bmi = L_bmi_female
            M_bmi = M_bmi_female
            S_bmi = S_bmi_female
        if self.height_cm and self.weight_kg and age_months <= 240 and age_months >=24:
            bmi = self.weight_kg/((self.height_cm/100)**2)
            L = next(c for c in L_bmi if c[0]==age_months)[1]
            M = next(c for c in M_bmi if c[0]==age_months)[1]
            S = next(c for c in S_bmi if c[0]==age_months)[1]
            Z = (((bmi/M)**L)-1)/(L*S)
            percentile = get_percentile_from_z_score(Z)
            return percentile
        else:
            return "N/A"
    def get_cpt_codes(self):
        return CPTcode.objects.filter(treatment_option = self.treatment_option)

        
class CPTcode(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    treatment_option = models.ForeignKey(TreatmentOption, null=True, blank=True)
    class Meta:
        verbose_name_plural = "CPT code"
    def __str__(self):
        return '%s' % self.code

class Task(models.Model):
    subject = models.CharField(max_length=300)
    body = models.TextField(null=True, blank=True)
    patient = models.ForeignKey(Patient)
    encounter = models.ForeignKey(Encounter, null=True, blank=True)
    assessment = models.ForeignKey(Assessment, null=True, blank=True)
    treatment = models.ForeignKey(Treatment, null=True, blank=True)
    date = models.DateTimeField('date and time of task')
    is_open = models.BooleanField(default=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True, related_name='task_owners')
    owner_group = models.ForeignKey(Group, null=True, blank=True)
    sender = models.ForeignKey(User, null=True, blank=True, related_name='task_senders')
    next_page = models.URLField(null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        if self.is_open:
            return '%s' % (self.subject)
        else:
            return '(CLOSED) %s' % (self.subject)

class Message(models.Model):
    subject = models.CharField(max_length=300)
    body = models.TextField(null=True, blank=True)
    patient = models.ForeignKey(Patient, null=True, blank=True)
    encounter = models.ForeignKey(Encounter, null=True, blank=True)
    assessment = models.ForeignKey(Assessment, null=True, blank=True)
    treatment = models.ForeignKey(Treatment, null=True, blank=True)
    date = models.DateTimeField('date and time of message')
    is_open = models.BooleanField(default=True)
    date_closed = models.DateTimeField(null=True, blank=True)
    recipient = models.ForeignKey(User, null=True, blank=True, related_name='message_recipients')
    recipient_users_list = models.ManyToManyField(User, blank=True)
    recipient_groups_list = models.ManyToManyField(Group, blank=True)
    sender = models.ForeignKey(User, null=True, blank=True, related_name='message_senders')
    class Meta:
        ordering = ['-date']
    def __str__(self):
        if self.is_open:
            return '%s (%s): %s (%s)' % (self.sender, self.sender.get_full_name(), self.subject, timezone.localtime(self.date).strftime('%Y-%m-%d %I:%M %p'))
        else:
            return '(CLOSED) %s (%s): %s (%s)' % (self.sender, self.sender.get_full_name(), self.subject, timezone.localtime(self.date).strftime('%Y-%m-%d %I:%M %p'))



class WorkplanStepAddAssessment(models.Model):
    diagnosis = models.ForeignKey(Diagnosis)
    workplan = models.ForeignKey(Workplan)
    def __str__(self):
        return 'Add Assessment: %s' % (self.diagnosis)

class WorkplanStepAddTreatment(models.Model):
    treatment_option = models.ForeignKey(TreatmentOption)
    workplan = models.ForeignKey(Workplan)
    def __str__(self):
        return 'Add Treatment: %s' % (self.treatment_option)

class WorkplanStepAddTask(models.Model):
    subject = models.CharField(max_length=300)
    body = models.TextField(null=True, blank=True)
    encounter_owner_task = models.BooleanField(default=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    owner_group = models.ForeignKey(Group, null=True, blank=True)
    workplan = models.ForeignKey(Workplan)
    def __str__(self):
        return 'Add Task: %s' % (self.subject)

class Report(models.Model):
    name = models.CharField(max_length=100)
    PRACTICE_REPORT = 'PR'
    OFFICE_REPORT = 'OF'
    PATIENT_REPORT = 'PA'
    ENCOUNTER_REPORT = 'ER'
    ASSESSMENT_REPORT = 'AR'
    TREATMENT_REPORT = 'TR'
    USER_REPORT = 'UR'
    REPORT_CHOICES = (
        (PRACTICE_REPORT, 'Practice Report'),
        (OFFICE_REPORT, 'Office Report'),
        (PATIENT_REPORT, 'Patient Report'),
        (ENCOUNTER_REPORT, 'Encounter Report'),
        (ASSESSMENT_REPORT, 'Assessment Report'),
        (TREATMENT_REPORT, 'Treatment Report'),
        (USER_REPORT, 'User Report'),
        )
    type = models.CharField(max_length=2, choices= REPORT_CHOICES, default=PATIENT_REPORT)
    report_template = models.TextField(null=True, blank=True)
    def __str__(self):
        if self.type in self.ENCOUNTER_REPORT:
            return 'Encounter Report: %s' % (self.name)
        else:
            return 'Report: %s' % (self.name)

class PracticePreferences(models.Model):
    group_to_receive_new_lab_tasks = models.ForeignKey(Group, related_name='lab_task_owners')
    group_to_receive_new_office_tasks = models.ForeignKey(Group, related_name='office_task_owners')
    encounter_summary_report = models.ForeignKey(Report, related_name = 'encounter_summary_report')
    class Meta:
        verbose_name_plural = "Practice preferences"
    def __str__(self):
        return 'Practice Preferences'


def attachment_directory_path(instance, filename):
    alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
    randomstring = ''.join(random.choice(alphanumeric) for i in range(20))
    return '{0}/{1}'.format(randomstring, filename)

class FileAttachment(models.Model):
    name = models.CharField(max_length=100)
    treatment = models.ForeignKey(Treatment)
    date = models.DateTimeField('date and time of upload')
    file_attachment = models.FileField(upload_to=attachment_directory_path)
    def __str__(self):
        return '%s: %s' % (timezone.localtime(self.date).strftime('%Y-%m-%d'), self.name)