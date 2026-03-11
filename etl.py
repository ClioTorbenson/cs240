import csv

with open('Street_Tree_Inventory_-_Active_Records.csv') as f:
  csv_reader = csv.reader(f, delimiter=',')
  next(csv_reader, None) # skip the first 
  tree_data = []
  site_data = []
  location_data = []
  for row in csv_reader:
    tree = 'INSERT INTO tree (species, mature_size, functional_type, diameter, tree_condition, date_inventoried) VALUES (\'' + row[6].replace('\'', '\'\'') + '\', \'' + row[7] + '\', \'' + row[8] + '\', ' + str(round(float(row[9]), 1)) + ', \'' + row[10] + '\', \'' + row[5].replace('/', '-')[:-12] + '\');' + '\n'
    site = 'INSERT INTO site (size, width, wires, improvement, site_type) VALUES (\'' + row[12] + '\', ' + str(round(float(row[13]), 1)) + ', \'' + row[14]  + '\', \'' + row[15] + '\', \'' + row[11] + '\'); \n'
    location = 'INSERT INTO location VALUES (\'' + row[4] + '\', \'' + row[3] + '\'' + '); \n'
    tree_data.append(tree)
    site_data.append(site)
    location_data.append(location)
with open('tree-data.sql', 'w') as fil:
    print('USE tree; \n', file=fil)
    fil.writelines(tree_data)
with open('site-data.sql', 'w') as fil:
    print('USE tree; \n', file=fil)
    fil.writelines(site_data)
with open('location-data.sql', 'w') as fil:
    print('USE tree; \n', file =fil)
    fil.writelines(location_data)

# used oregon bird database for this data
import urllib.request
from zipfile import ZipFile
import csv
import random
import ssl
import certifi

certifi_context = ssl.create_default_context(cafile=certifi.where())

# import Oregon bird species dataset from CornellLab and save to current directory
file_path = 'birds.zip'
url = 'https://da-st-us-swap.s3.amazonaws.com/2023_updates/summaries/OR_CSV.zip'

response = urllib.request.urlopen(url, context=certifi_context)
bird_file = response.read()

with open(file_path, 'wb') as file:
    file.write(bird_file)

# extract csv from zip file
with ZipFile(file_path, 'r') as zObject:
    zObject.extract('OR_regional_status_2023.csv')
zObject.close()

bird_species = []

with open('OR_regional_status_2023.csv') as data:
    csv_reader = csv.reader(data, delimiter=',')
    for lines in csv_reader:
        if lines[0] != 'state_name':
            # only columns common_name and scientific_name are needed
            bird_species.append(lines[2:4])

num_birds = 100000
bird_data = []
for i in range(num_birds):
    species = bird_species[random.randint(0, len(bird_species) - 1)]
    birds = 'INSERT INTO bird (bird_name, species) VALUES (\'' + species[0].replace('\'', '\'\'') + '\', \'' + species[1].replace('\'', '\'\'') + '\');\n'
    bird_data.append(birds)
with open('bird-data.sql', 'w') as fil:
    print('USE tree; \n', file =fil)
    fil.writelines(bird_data)

# each bird can have up to 3 nests in different trees
nests_in_data = []
for i in range(num_birds):
    mult_trees = random.randint(1, 3) # determines if the bird will nest in one or more trees
    if mult_trees > 1:
       for _ in range(mult_trees):
            tree_id = random.randint(1, 252206)
            year_created = random.randint(2016, 2026)
            nests_string = 'INSERT INTO nests_in VALUES (' + str(i + 1) + ', ' + str(tree_id) + ', ' + str(year_created) + '); \n'
            nests_in_data.append(nests_string)
    else:
        year_created = random.randint(2016, 2026)
        tree_id = random.randint(1, 252206)
        nests_string = 'INSERT INTO nests_in VALUES (' + str(i + 1) + ', ' + str(tree_id) + ', ' + str(year_created) + '); \n'
        nests_in_data.append(nests_string)
with open('nests_in-data.sql', 'w') as fil:
   print('USE tree; \n', file = fil)
   fil.writelines(nests_in_data)