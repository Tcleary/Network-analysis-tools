import csv

#have the user input a file
filename = input('Enter file name: ')

# set up empty dictionary
mydict = {}

#Process the file
with open(filename) as r:
    reader = csv.reader(r)  
    # skip header row
    next(reader, None)
    # process data rows
    for rows in reader:   
        k = rows[1] #sets key value according to fields in Column B
        v = rows[0] #sets values according to fields in Column A

        #lables the key, this can be changed for other purposes
        workshop = k 
       
        # create/get key in/from dict if needed, prepopulate value with empty list
        key = mydict.setdefault(workshop,[])

        # append data to list
        key.append(v)

#print (mydict)
#Printing the dictionaries in a csv so each key has a different line
with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value])

print("File has been created")