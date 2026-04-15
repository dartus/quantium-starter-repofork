import csv
import os

def readfile (csvreader):

    for row in csvreader:

        if row[1] == "price":
            continue

        product = row[0]
        price = row[1]
        quantity = row[2]
        date = row[3]
        region = row[4]

        actualprice = price[1:]
        sales = int(quantity) * float(actualprice)
        if product == "pink morsel":
            print("$",sales, ", " ,date, ", " ,region)







dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'daily_sales_data_0.csv')) as csv_file1, open(os.path.join(dir, 'daily_sales_data_1.csv')) as csv_file2, open(os.path.join(dir, 'daily_sales_data_2.csv')) as csv_file3:
    csv_reader1 = csv.reader(csv_file1, delimiter=',')
    csv_reader2 = csv.reader(csv_file2, delimiter=',')
    csv_reader3 = csv.reader(csv_file3, delimiter=',')


    readfile(csv_reader1)
    readfile(csv_reader2)
    readfile(csv_reader3)


    
    


    # for row in csv_reader1:

    #     if row[1] == "price":
    #         continue

    #     product = row[0]
    #     price = row[1]
    #     quantity = row[2]
    #     date = row[3]
    #     region = row[4]

    #     actualprice = price[1:]
    #     sales = int(quantity) * float(actualprice)
    #     if product == "pink morsel":
    #         print("$",sales, ", " ,date, ", " ,region)

    # for row in csv_reader2:

    #     if row[1] == "price":
    #         continue

    #     product = row[0]
    #     price = row[1]
    #     quantity = row[2]
    #     date = row[3]
    #     region = row[4]

    #     actualprice = price[1:]
    #     sales = int(quantity) * float(actualprice)
    #     if product == "pink morsel":
    #         print("$",sales, ", " ,date, ", " ,region)

    # for row in csv_reader1:

    #     if row[1] == "price":
    #         continue

    #     product = row[0]
    #     price = row[1]
    #     quantity = row[2]
    #     date = row[3]
    #     region = row[4]

    #     actualprice = price[1:]
    #     sales = int(quantity) * float(actualprice)
    #     if product == "pink morsel":
    #         print("$",sales, ", " ,date, ", " ,region)