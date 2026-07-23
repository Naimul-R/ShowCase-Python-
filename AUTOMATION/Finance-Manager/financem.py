import csv 

FILE = ''

def finance_manager(file):
    sum = 0 
    transactions = []
    
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
            transactions.append(transiction)
    
    print(f"The transaction of this months is {sum}")
    print
    return transactions

print(finance_manager(FILE))