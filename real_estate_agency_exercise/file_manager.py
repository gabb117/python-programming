#file manager

from constants import NAME_FILE
from person import Person
from house import House

def load_houses(d):
    try:
        csv_file = open(NAME_FILE,'r')
        for line in csv_file:
            line_info = line.rstrip('\n').split(',')
            owner_parts = line_info[11].split(";")
            p = Person(owner_parts[0], owner_parts[1], owner_parts[2], owner_parts[3])
            h = House(line_info[0],float(line_info[1]),int(line_info[2]),float(line_info[3]),line_info[4],line_info[5],line_info[6],line_info[7],line_info[8],line_info[9],line_info[10],p)
            d[line_info[0]] = h

        csv_file.close()
        print("\t>>>" + str(len(d)) + " Management houses<<<")

    except FileNotFoundError:
        print("\t>>>No house under management<<<")

    except Exception as error:
        print("\tError: " , error)
        

def save_house(d):
    csv_file = open(NAME_FILE,'w')
    all_the_keys = d.keys()
    for keys in all_the_keys:
        line = d[keys].get_all_info()
        csv_file.write(line+'\n')

    csv_file.close()