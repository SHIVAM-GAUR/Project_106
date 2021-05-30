import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    coffeeIn_ml = []
    sleepIn_hours = []
    
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            coffeeIn_ml.append(float(row["CoffeIn-ml"]))
            sleepIn_hours.append(float(row["sleepIn-hours"]))
            
                           
    return {"x" :coffeeIn_ml, "y" :sleepIn_hours}
    
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation coefficient for coffe consumed v/s sleep in hours ",correlation[0,1])
    

def setup():
    data_path ="./coffe.csv"
    
    datasource = getDataSource(data_path)
    
    findCorrelation(datasource)
    

setup()