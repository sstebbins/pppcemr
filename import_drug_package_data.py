import csv
from pppcemr.models import *


dataReader = csv.reader(open('ndc_database_2016_02_21/package.txt'), delimiter='\t')

for row in dataReader:
    package = DrugPackage()
    package.product_id = row[0]
    package.product_ndc = row[1]
    package.package_ndc = row[2]
    package.package_name = row[3]
    package.save()
