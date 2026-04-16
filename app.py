# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import csv
import os

saleslist = []
datelist = []
regionlist = []

def readfile (csvreader):

    for row in csvreader:

        if row[0] == "product":
            continue

        product = row[0]
        price = row[1]
        quantity = row[2]
        date = row[3]
        region = row[4]

        actualprice = price[1:]
        sales = int(quantity) * float(actualprice)
        if product == "pink morsel":
            saleslist.append(sales)
            datelist.append(date)
            regionlist.append(region)







dir = os.path.dirname(__file__)

with open(os.path.join(dir, 'data' ,'daily_sales_data_0.csv')) as csv_file1, open(os.path.join(dir, 'data' ,'daily_sales_data_1.csv')) as csv_file2, open(os.path.join(dir, 'data' ,'daily_sales_data_2.csv')) as csv_file3:
    csv_reader1 = csv.reader(csv_file1, delimiter=',')
    csv_reader2 = csv.reader(csv_file2, delimiter=',')
    csv_reader3 = csv.reader(csv_file3, delimiter=',')


    print("Product: Pink Morsels")
    print("Sales       date       region")
    readfile(csv_reader1)
    readfile(csv_reader2)
    readfile(csv_reader3)


app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Date": datelist,
    "Sales": saleslist,
    "Region": regionlist
})

fig = px.line(df, x="Date", y="Sales", color="Region")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
