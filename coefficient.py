import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
            
                           
    return {"x" :marks_in_percentage, "y" :days_present}
    
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation coefficient for Marks In Percentage v/s Days Present ",correlation[0,1])
    

def setup():
    data_path ="./present.csv"
    
    datasource = getDataSource(data_path)
    
    findCorrelation(datasource)
    

setup()