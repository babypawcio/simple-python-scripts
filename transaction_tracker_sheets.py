import csv
import gspread 
import time

MONTH = str(input("wprowadz nazwe miesiaca, za ktory chcesz rozliczenie: "))

file=f"millenium_{MONTH}.csv"

transactions = []

def milleniumFin(file):

    with open(file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[1]
            name = row[3]
            reciver = row[6]
            amount = row[7]
            nominal = row[10]
            transaction = [date, name, reciver, amount, nominal]
            print(transaction)

            transactions.append(transaction)
        
        return transactions


sa = gspread.service_account()
sh = sa.open("Personal Finances")


wks = sh.worksheet(f"{MONTH}")

rows = milleniumFin(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[2]])
    time.sleep(2)

wks.insert_row([1, 2, 3], 10)