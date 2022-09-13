
# data-enrichment

# loaded in the data from Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv
# loaded in the data from NY_2015_ADI_9 Digit Zip Code_v3.1.csv

# removed all white spaces from columns

# changed all columns to lower case

# dropped rows with missing values

# stored the first three letter as username and made the 9 digit zip code into a 3 digit zip code in the neighborhood_atlas table

# dropped the zipid columns in the neighborhood_atlas table

# removed duplicates rows from operating_certificate_number column

# created a small dataset column for both table

# merged the neighborhood_atlas_small table with zipcode of the sparcs_small table columns

# saved enriched file to a new combined_zip.csv under Datasets/csv_files
