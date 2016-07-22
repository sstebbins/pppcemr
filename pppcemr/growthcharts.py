import csv
from django.conf import settings

if settings.USE_SI:
    weight_conversion_multiplier = 1
    height_conversion_multiplier = 1
else:
    weight_conversion_multiplier = 2.2
    height_conversion_multiplier = 1/2.54

third_percentile_weight_male = []
third_percentile_weight_female = []
fifth_percentile_weight_male = []
fifth_percentile_weight_female = []
tenth_percentile_weight_male = []
tenth_percentile_weight_female = []
twenty_fifth_percentile_weight_male = []
twenty_fifth_percentile_weight_female = []
fiftieth_percentile_weight_male = []
fiftieth_percentile_weight_female = []
seventy_fifth_percentile_weight_male = []
seventy_fifth_percentile_weight_female = []
ninetieth_percentile_weight_male = []
ninetieth_percentile_weight_female = []
ninety_fifth_percentile_weight_male = []
ninety_fifth_percentile_weight_female = []
ninety_seventh_percentile_weight_male = []
ninety_seventh_percentile_weight_female = []
L_weight_male = []
L_weight_female = []
M_weight_male = []
M_weight_female = []
S_weight_male = []
S_weight_female = []

third_percentile_height_male = []
third_percentile_height_female = []
fifth_percentile_height_male = []
fifth_percentile_height_female = []
tenth_percentile_height_male = []
tenth_percentile_height_female = []
twenty_fifth_percentile_height_male = []
twenty_fifth_percentile_height_female = []
fiftieth_percentile_height_male = []
fiftieth_percentile_height_female = []
seventy_fifth_percentile_height_male = []
seventy_fifth_percentile_height_female = []
ninetieth_percentile_height_male = []
ninetieth_percentile_height_female = []
ninety_fifth_percentile_height_male = []
ninety_fifth_percentile_height_female = []
ninety_seventh_percentile_height_male = []
ninety_seventh_percentile_height_female = []
L_height_male = []
L_height_female = []
M_height_male = []
M_height_female = []
S_height_male = []
S_height_female = []

third_percentile_bmi_male = []
third_percentile_bmi_female = []
fifth_percentile_bmi_male = []
fifth_percentile_bmi_female = []
tenth_percentile_bmi_male = []
tenth_percentile_bmi_female = []
twenty_fifth_percentile_bmi_male = []
twenty_fifth_percentile_bmi_female = []
fiftieth_percentile_bmi_male = []
fiftieth_percentile_bmi_female = []
seventy_fifth_percentile_bmi_male = []
seventy_fifth_percentile_bmi_female = []
ninetieth_percentile_bmi_male = []
ninetieth_percentile_bmi_female = []
ninety_fifth_percentile_bmi_male = []
ninety_fifth_percentile_bmi_female = []
ninety_seventh_percentile_bmi_male = []
ninety_seventh_percentile_bmi_female = []
L_bmi_male = []
L_bmi_female = []
M_bmi_male = []
M_bmi_female = []
S_bmi_male = []
S_bmi_female = []


## UNCOMMENT BELOW TO USE CDC DATA FOR <2Y

# data = list(csv.reader(open('pppcemr/static/wtageinf.csv')))

# for index, row in enumerate(data):
#     if index > 0:
#         if row[0] == '1':
#             if float(row[1]) <= 24:
#                 third_percentile_weight_male.append([float(row[1])/12,float(row[5])*weight_conversion_multiplier])
#                 fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[6]) * weight_conversion_multiplier])
#                 tenth_percentile_weight_male.append([float(row[1]) / 12, float(row[7]) * weight_conversion_multiplier])
#                 twenty_fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[8]) * weight_conversion_multiplier])
#                 fiftieth_percentile_weight_male.append([float(row[1]) / 12, float(row[9]) * weight_conversion_multiplier])
#                 seventy_fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[10]) * weight_conversion_multiplier])
#                 ninetieth_percentile_weight_male.append([float(row[1]) / 12, float(row[11]) * weight_conversion_multiplier])
#                 ninety_fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[12]) * weight_conversion_multiplier])
#                 ninety_seventh_percentile_weight_male.append([float(row[1]) / 12, float(row[13]) * weight_conversion_multiplier])
#         else:
#             if float(row[1]) <= 24:
#                 third_percentile_weight_female.append([float(row[1]) / 12, float(row[5]) * weight_conversion_multiplier])
#                 fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[6]) * weight_conversion_multiplier])
#                 tenth_percentile_weight_female.append([float(row[1]) / 12, float(row[7]) * weight_conversion_multiplier])
#                 twenty_fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[8]) * weight_conversion_multiplier])
#                 fiftieth_percentile_weight_female.append([float(row[1]) / 12, float(row[9]) * weight_conversion_multiplier])
#                 seventy_fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[10]) * weight_conversion_multiplier])
#                 ninetieth_percentile_weight_female.append([float(row[1]) / 12, float(row[11]) * weight_conversion_multiplier])
#                 ninety_fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[12]) * weight_conversion_multiplier])
#                 ninety_seventh_percentile_weight_female.append([float(row[1]) / 12, float(row[13]) * weight_conversion_multiplier])

data = list(csv.reader(open('pppcemr/static/who_boy_wt_age.csv'))) # WHO data

for index, row in enumerate(data):
    if index > 0:
        if float(row[0]) <= 24:
            L_weight_male.append([int(row[0]), float(row[1])])
            M_weight_male.append([int(row[0]), float(row[2])])
            S_weight_male.append([int(row[0]), float(row[3])])
            third_percentile_weight_male.append([float(row[0])/12,float(row[4])*weight_conversion_multiplier])
            fifth_percentile_weight_male.append([float(row[0]) / 12, float(row[5]) * weight_conversion_multiplier])
            tenth_percentile_weight_male.append([float(row[0]) / 12, float(row[6]) * weight_conversion_multiplier])
            twenty_fifth_percentile_weight_male.append([float(row[0]) / 12, float(row[7]) * weight_conversion_multiplier])
            fiftieth_percentile_weight_male.append([float(row[0]) / 12, float(row[8]) * weight_conversion_multiplier])
            seventy_fifth_percentile_weight_male.append([float(row[0]) / 12, float(row[9]) * weight_conversion_multiplier])
            ninetieth_percentile_weight_male.append([float(row[0]) / 12, float(row[10]) * weight_conversion_multiplier])
            ninety_fifth_percentile_weight_male.append([float(row[0]) / 12, float(row[11]) * weight_conversion_multiplier])
            ninety_seventh_percentile_weight_male.append([float(row[0]) / 12, float(row[12]) * weight_conversion_multiplier])


data = list(csv.reader(open('pppcemr/static/who_girl_wt_age.csv'))) # WHO data
for index, row in enumerate(data):
    if index > 0:
        if float(row[0]) <= 24:
            L_weight_female.append([int(row[0]), float(row[1])])
            M_weight_female.append([int(row[0]), float(row[2])])
            S_weight_female.append([int(row[0]), float(row[3])])
            third_percentile_weight_female.append([float(row[0]) / 12, float(row[4]) * weight_conversion_multiplier])
            fifth_percentile_weight_female.append([float(row[0]) / 12, float(row[5]) * weight_conversion_multiplier])
            tenth_percentile_weight_female.append([float(row[0]) / 12, float(row[6]) * weight_conversion_multiplier])
            twenty_fifth_percentile_weight_female.append([float(row[0]) / 12, float(row[7]) * weight_conversion_multiplier])
            fiftieth_percentile_weight_female.append([float(row[0]) / 12, float(row[8]) * weight_conversion_multiplier])
            seventy_fifth_percentile_weight_female.append([float(row[0]) / 12, float(row[9]) * weight_conversion_multiplier])
            ninetieth_percentile_weight_female.append([float(row[0]) / 12, float(row[10]) * weight_conversion_multiplier])
            ninety_fifth_percentile_weight_female.append([float(row[0]) / 12, float(row[11]) * weight_conversion_multiplier])
            ninety_seventh_percentile_weight_female.append([float(row[0]) / 12, float(row[12]) * weight_conversion_multiplier])


data = list(csv.reader(open('pppcemr/static/wtage.csv'))) # CDC data

for index, row in enumerate(data):
    if index > 0:
        if row[0] == '1':
            L_weight_male.append([int(float(row[1])), float(row[2])])
            M_weight_male.append([int(float(row[1])), float(row[3])])
            S_weight_male.append([int(float(row[1])), float(row[4])])
            third_percentile_weight_male.append([float(row[1])/12,float(row[5])*weight_conversion_multiplier])
            fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[6]) * weight_conversion_multiplier])
            tenth_percentile_weight_male.append([float(row[1]) / 12, float(row[7]) * weight_conversion_multiplier])
            twenty_fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[8]) * weight_conversion_multiplier])
            fiftieth_percentile_weight_male.append([float(row[1]) / 12, float(row[9]) * weight_conversion_multiplier])
            seventy_fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[10]) * weight_conversion_multiplier])
            ninetieth_percentile_weight_male.append([float(row[1]) / 12, float(row[11]) * weight_conversion_multiplier])
            ninety_fifth_percentile_weight_male.append([float(row[1]) / 12, float(row[12]) * weight_conversion_multiplier])
            ninety_seventh_percentile_weight_male.append([float(row[1]) / 12, float(row[13]) * weight_conversion_multiplier])
        else:
            L_weight_female.append([int(float(row[1])), float(row[2])])
            M_weight_female.append([int(float(row[1])), float(row[3])])
            S_weight_female.append([int(float(row[1])), float(row[4])])
            third_percentile_weight_female.append([float(row[1]) / 12, float(row[5]) * weight_conversion_multiplier])
            fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[6]) * weight_conversion_multiplier])
            tenth_percentile_weight_female.append([float(row[1]) / 12, float(row[7]) * weight_conversion_multiplier])
            twenty_fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[8]) * weight_conversion_multiplier])
            fiftieth_percentile_weight_female.append([float(row[1]) / 12, float(row[9]) * weight_conversion_multiplier])
            seventy_fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[10]) * weight_conversion_multiplier])
            ninetieth_percentile_weight_female.append([float(row[1]) / 12, float(row[11]) * weight_conversion_multiplier])
            ninety_fifth_percentile_weight_female.append([float(row[1]) / 12, float(row[12]) * weight_conversion_multiplier])
            ninety_seventh_percentile_weight_female.append([float(row[1]) / 12, float(row[13]) * weight_conversion_multiplier])


# Height for age
data = list(csv.reader(open('pppcemr/static/WHO_boy_len_age.csv'))) # WHO data

for index, row in enumerate(data):
    if index > 0:
        if float(row[0]) <= 24:
            L_height_male.append([int(row[0]), float(row[1])])
            M_height_male.append([int(row[0]), float(row[2])])
            S_height_male.append([int(row[0]), float(row[3])])
            third_percentile_height_male.append([float(row[0])/12,float(row[4])*height_conversion_multiplier])
            fifth_percentile_height_male.append([float(row[0]) / 12, float(row[5]) * height_conversion_multiplier])
            tenth_percentile_height_male.append([float(row[0]) / 12, float(row[6]) * height_conversion_multiplier])
            twenty_fifth_percentile_height_male.append([float(row[0]) / 12, float(row[7]) * height_conversion_multiplier])
            fiftieth_percentile_height_male.append([float(row[0]) / 12, float(row[8]) * height_conversion_multiplier])
            seventy_fifth_percentile_height_male.append([float(row[0]) / 12, float(row[9]) * height_conversion_multiplier])
            ninetieth_percentile_height_male.append([float(row[0]) / 12, float(row[10]) * height_conversion_multiplier])
            ninety_fifth_percentile_height_male.append([float(row[0]) / 12, float(row[11]) * height_conversion_multiplier])
            ninety_seventh_percentile_height_male.append([float(row[0]) / 12, float(row[12]) * height_conversion_multiplier])

data = list(csv.reader(open('pppcemr/static/who_girl_len_age.csv'))) # WHO data
for index, row in enumerate(data):
    if index > 0:
        if float(row[0]) <= 24:
            L_height_female.append([int(row[0]), float(row[1])])
            M_height_female.append([int(row[0]), float(row[2])])
            S_height_female.append([int(row[0]), float(row[3])])
            third_percentile_height_female.append([float(row[0]) / 12, float(row[4]) * height_conversion_multiplier])
            fifth_percentile_height_female.append([float(row[0]) / 12, float(row[5]) * height_conversion_multiplier])
            tenth_percentile_height_female.append([float(row[0]) / 12, float(row[6]) * height_conversion_multiplier])
            twenty_fifth_percentile_height_female.append([float(row[0]) / 12, float(row[7]) * height_conversion_multiplier])
            fiftieth_percentile_height_female.append([float(row[0]) / 12, float(row[8]) * height_conversion_multiplier])
            seventy_fifth_percentile_height_female.append([float(row[0]) / 12, float(row[9]) * height_conversion_multiplier])
            ninetieth_percentile_height_female.append([float(row[0]) / 12, float(row[10]) * height_conversion_multiplier])
            ninety_fifth_percentile_height_female.append([float(row[0]) / 12, float(row[11]) * height_conversion_multiplier])
            ninety_seventh_percentile_height_female.append([float(row[0]) / 12, float(row[12]) * height_conversion_multiplier])

data = list(csv.reader(open('pppcemr/static/statage.csv'))) # CDC data

for index, row in enumerate(data):
    if index > 0:
        if row[0] == '1':
            L_height_male.append([int(float(row[1])), float(row[2])])
            M_height_male.append([int(float(row[1])), float(row[3])])
            S_height_male.append([int(float(row[1])), float(row[4])])
            third_percentile_height_male.append([float(row[1])/12,float(row[5])*height_conversion_multiplier])
            fifth_percentile_height_male.append([float(row[1]) / 12, float(row[6]) * height_conversion_multiplier])
            tenth_percentile_height_male.append([float(row[1]) / 12, float(row[7]) * height_conversion_multiplier])
            twenty_fifth_percentile_height_male.append([float(row[1]) / 12, float(row[8]) * height_conversion_multiplier])
            fiftieth_percentile_height_male.append([float(row[1]) / 12, float(row[9]) * height_conversion_multiplier])
            seventy_fifth_percentile_height_male.append([float(row[1]) / 12, float(row[10]) * height_conversion_multiplier])
            ninetieth_percentile_height_male.append([float(row[1]) / 12, float(row[11]) * height_conversion_multiplier])
            ninety_fifth_percentile_height_male.append([float(row[1]) / 12, float(row[12]) * height_conversion_multiplier])
            ninety_seventh_percentile_height_male.append([float(row[1]) / 12, float(row[13]) * height_conversion_multiplier])
        else:
            L_height_female.append([int(float(row[1])), float(row[2])])
            M_height_female.append([int(float(row[1])), float(row[3])])
            S_height_female.append([int(float(row[1])), float(row[4])])
            third_percentile_height_female.append([float(row[1]) / 12, float(row[5]) * height_conversion_multiplier])
            fifth_percentile_height_female.append([float(row[1]) / 12, float(row[6]) * height_conversion_multiplier])
            tenth_percentile_height_female.append([float(row[1]) / 12, float(row[7]) * height_conversion_multiplier])
            twenty_fifth_percentile_height_female.append([float(row[1]) / 12, float(row[8]) * height_conversion_multiplier])
            fiftieth_percentile_height_female.append([float(row[1]) / 12, float(row[9]) * height_conversion_multiplier])
            seventy_fifth_percentile_height_female.append([float(row[1]) / 12, float(row[10]) * height_conversion_multiplier])
            ninetieth_percentile_height_female.append([float(row[1]) / 12, float(row[11]) * height_conversion_multiplier])
            ninety_fifth_percentile_height_female.append([float(row[1]) / 12, float(row[12]) * height_conversion_multiplier])
            ninety_seventh_percentile_height_female.append([float(row[1]) / 12, float(row[13]) * height_conversion_multiplier])

data = list(csv.reader(open('pppcemr/static/bmiagerev.csv'))) # CDC data

for index, row in enumerate(data):
    if index > 0:
        if row[0] == '1':
            L_bmi_male.append([int(float(row[1])), float(row[2])])
            M_bmi_male.append([int(float(row[1])), float(row[3])])
            S_bmi_male.append([int(float(row[1])), float(row[4])])
            third_percentile_bmi_male.append([float(row[1])/12,float(row[5])])
            fifth_percentile_bmi_male.append([float(row[1]) / 12, float(row[6])])
            tenth_percentile_bmi_male.append([float(row[1]) / 12, float(row[7])])
            twenty_fifth_percentile_bmi_male.append([float(row[1]) / 12, float(row[8])])
            fiftieth_percentile_bmi_male.append([float(row[1]) / 12, float(row[9])])
            seventy_fifth_percentile_bmi_male.append([float(row[1]) / 12, float(row[10])])
            ninetieth_percentile_bmi_male.append([float(row[1]) / 12, float(row[11])])
            ninety_fifth_percentile_bmi_male.append([float(row[1]) / 12, float(row[12])])
            ninety_seventh_percentile_bmi_male.append([float(row[1]) / 12, float(row[13])])
        else:
            L_bmi_female.append([int(float(row[1])), float(row[2])])
            M_bmi_female.append([int(float(row[1])), float(row[3])])
            S_bmi_female.append([int(float(row[1])), float(row[4])])
            third_percentile_bmi_female.append([float(row[1]) / 12, float(row[5])])
            fifth_percentile_bmi_female.append([float(row[1]) / 12, float(row[6])])
            tenth_percentile_bmi_female.append([float(row[1]) / 12, float(row[7])])
            twenty_fifth_percentile_bmi_female.append([float(row[1]) / 12, float(row[8])])
            fiftieth_percentile_bmi_female.append([float(row[1]) / 12, float(row[9])])
            seventy_fifth_percentile_bmi_female.append([float(row[1]) / 12, float(row[10])])
            ninetieth_percentile_bmi_female.append([float(row[1]) / 12, float(row[11])])
            ninety_fifth_percentile_bmi_female.append([float(row[1]) / 12, float(row[12])])
            ninety_seventh_percentile_bmi_female.append([float(row[1]) / 12, float(row[13])])
