import csv

with open('Street_Tree_Inventory_-_Active_Records.csv') as f:
  csv_reader = csv.reader(f, delimiter=',')
  next(csv_reader, None) # skip the first 
  tree_data = []
  site_data = []
  location_data = []
  for row in csv_reader:
    tree = 'INSERT INTO tree (species, mature_size, functional_type, diameter, tree_condition, date_inventoried) \n VALUES (\'' + row[6] + '\', \'' + row[7] + '\', \'' + row[8] + '\', ' + str(round(float(row[9]), 1)) + ', \'' + row[10] + '\', \'' + row[5].replace('/', '-')[:-12] + '\');' + '\n'
    site = 'INSERT INTO site (size, width, wires, improvement, site_type) \n VALUES (\'' + row[12] + '\', ' + str(round(float(row[13]), 1)) + ', \'' + row[14]  + '\', \'' + row[15] + '\', \'' + row[11] + '\'); \n'
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