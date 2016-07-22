from  .models import Diagnosis

import csv

dataReader = csv.reader(open('icd10csv.txt'), delimiter='|')

for row in dataReader:
	diagnosis = Diagnosis()
	diagnosis.icd_code = row[0]
	diagnosis.description = row[1]
	diagnosis.save()
	
