import csv
from pppcemr.models import *


dataReader = csv.reader(open('ndc_database_2016_02_21/product.txt'), delimiter='\t')

for row in dataReader:
    drug = Drug()
    drug.product_id = row[0]
    drug.product_ndc = row[1]
    drug.trade_name = row[3] + row [4]
    drug.generic_name = row[5]
    drug.dosage_form = row[6]
    drug.route = row[7]
    drug.concentration_numerator = row[14]
    drug.concentration_denominator = row[15]
    drug.dea = row[17]
    drug.save()
    
