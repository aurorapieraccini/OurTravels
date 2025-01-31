import sys

filename = sys.argv[1]
with open(filename, 'r', encoding='UTF-8') as file:
    for line in file.readlines()[0:30]:
        parts = line.split('\t')
        print('geonameid = %s country = %s city = %s ' % (parts[0], parts[8], parts[1]))
        print('latitude = %s longitude = %s ' % (parts[4], parts[5]))
        print('elevation = %s population = %s ' % (parts[15], parts[14]))
        print('modification_date = %s ' % (parts[18]))