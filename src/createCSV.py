import csv

def createCSV(business_data):
    print("Writing CSV")
    padding="      "
    header=[' index ',' category ',' name ',' street ',' city ',' zip ',' phone ',' fax ',' website ',' about ',' contact ']
    with open('./csv_files/businessCSV.csv','w',newline='')as f:
        writer=csv.writer(f,delimiter=',',escapechar=' ',quoting=csv.QUOTE_NONE)
        writer.writerow(header)
        #writer.writerow(space)
        for bus in business_data:
            writer.writerow(bus)
    
    print("CSV complete")
