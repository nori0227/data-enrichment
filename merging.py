from math import comb
from operator import ne
import pandas as pd 

########################
### load in the data 
########################

sparcs = pd.read_csv('Datasets/csv_files/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
sparcs

neighborhood_atlas = pd.read_csv('Datasets/csv_files/NY_2015_ADI_9 Digit Zip Code_v3.1.csv')
neighborhood_atlas 

# list columns
list(sparcs)
list(neighborhood_atlas)

# remove all special characters and whitespace ' ' from column names
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
list(sparcs.columns)

neighborhood_atlas.columns=neighborhood_atlas.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex
list(neighborhood_atlas)

#change all column names to lower case
sparcs.columns= sparcs.columns.str.lower()
list(sparcs.columns)
neighborhood_atlas.columns= neighborhood_atlas.columns.str.lower()
list(neighborhood_atlas.columns)

#dropping rows with missing values
sparcs.dropna(inplace=True) 
sparcs
sparcs.shape #get a count of rows and columns

neighborhood_atlas.dropna(inplace=True)
neighborhood_atlas
neighborhood_atlas.shape #get a count of rows and columns


#storing first three letter as username
neighborhood_atlas['zip_code'] = neighborhood_atlas['zipid'].str.slice(1, 4)
neighborhood_atlas['zip_code']

# droping zipid columns
neighborhood_atlas.drop(['zipid'], axis=1, inplace=True) 
neighborhood_atlas.columns

##########
list(sparcs.columns)
sparcs_small= sparcs[['health_service_area', 'hospital_county', 'operating_certificate_number', 'zip_code_3_digits']]
print(sparcs_small.head (5).to_markdown())
print(sparcs_small.head (15).to_markdown())
sparcs_small.shape

sparcs_small_nodups= sparcs_small.drop_duplicates(subset=['operating_certificate_number'])
sparcs_small_nodups


list(neighborhood_atlas.columns)
neighborhood_atlas_small= neighborhood_atlas[['type','zip_code', 'adi_staternk']]
print(neighborhood_atlas_small.head (15).to_markdown())
neighborhood_atlas_small.shape

#####below we are going to take the neighborhood_atlas table and enrich it with the zipcode of sparcs table
combined_zip= neighborhood_atlas_small.merge(sparcs_small_nodups, how='left', left_on='zip_code', right_on='zip_code_3_digits')
combined_zip.columns

####save enriched file to a a new .csv
combined_zip.to_csv('Datasets/csv_files/combined_zip.csv')
combined_zip.shape

