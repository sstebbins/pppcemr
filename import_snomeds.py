import csv
from pppcemr.models import *


dataReader = csv.reader(open('der2_Refset_ICD10CM_US_20150901/tls_Icd10cmHumanReadableMap_US1000124_20150901.tsv'), delimiter='\t')

for row in dataReader:
    snomed, created = Snomed.objects.get_or_create(name=row[6], code=row[5])
    if created:
        snomed.icd_equivalents = '%s' %(row[11])
        str = 'Created: %s, added %s' % (snomed, row[11])
    else:
        snomed.icd_equivalents = '%s, %s' %(snomed.icd_equivalents, row[11])
        str = 'Added %s to %s' % (row[11], snomed)
    snomed.save()
    print(str)
    
