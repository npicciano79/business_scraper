import csv



def createTempCSV():
    #check if cleaned file exists, if so remove previous cleaned file
    
    #creates csv with removed index and headers 
    with open('./csv_files/businessCSV.csv','r')as infile:
        reader=csv.reader(infile)
        next(reader,None) #skip header
        with open('./csv_files/businessCSV_cleaned.csv','w',newline='')as outfile:
            writer=csv.writer(outfile,delimiter=',',escapechar='',quoting=csv.QUOTE_NONE)
            for row in reader:
                writer.writerow((row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))


