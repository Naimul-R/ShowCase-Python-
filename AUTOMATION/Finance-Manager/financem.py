import csv 

month = "July"

def finance_manager(file):
    sum = 0 
    transiction = []
    
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            # Get name, amount and currency 
            name = row[4]
            amount = float(row[7])
            date = row[1]
            
            transiction = (date, name, amount)
            sum += amount
            
            