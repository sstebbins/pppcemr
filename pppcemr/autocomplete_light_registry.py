import autocomplete_light.shortcuts as al
#from .models import Diagnosis, Patient, LabType
from .models import *
from django.contrib.auth.models import User, Group
# This will generate a DiagnosisAutocomplete class
al.register(Diagnosis,
    # Just like in ModelAdmin.search_fields
    search_fields=['^icd_code', 'description', 'user_description'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Enter Search Terms',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    order_by = '-date_last_used',
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)

al.register(Patient,
    # Just like in ModelAdmin.search_fields
    search_fields=['^first_name', '^last_name', 'birthdate'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Enter Search Terms',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)

al.register(TreatmentOption,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Enter Search Terms',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    order_by = '-date_last_used',
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)

al.register(StandardPhysicalResults,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Enter Search Terms',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)
# 
# al.register(InHouseLabType,
#     # Just like in ModelAdmin.search_fields
#     search_fields=['test_name'],
#     attrs={
#         # This will set the input placeholder attribute:
#         'placeholder': 'Enter Search Terms',
#         # This will set the yourlabs.Autocomplete.minimumCharacters
#         # options, the naming conversion is handled by jQuery
#         'data-autocomplete-minimum-characters': 1,
#     },
#     # This will set the data-widget-maximum-values attribute on the
#     # widget container element, and will be set to
#     # yourlabs.Widget.maximumValues (jQuery handles the naming
#     # conversion).
#     widget_attrs={
#         'data-widget-maximum-values': 4,
#         # Enable modern-style widget !
#         'class': 'modern-style',
#     },
# )

al.register(User,
    # Just like in ModelAdmin.search_fields
    search_fields=['username', 'first_name', 'last_name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Enter Search Terms',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 4,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)
