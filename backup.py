#Name: Erifeoluwa Jamgbadi
#Student Number: 2018117950
#python code for data quality assignment

#importing dataset 
import pandas as pd

dataset = pd.read_csv('data/dataset.csv', header = None)

#giving the headings from the file, feature_names.txt
with open('data/feature_names.txt') as file:
    datasetNames = file.readlines()
    #datasetNames = datasetNames.replace('\n', ' ')
    

dataset.columns = datasetNames

#this separates into numeric data, which ends up being using .describe()
#this is to swap the rows and columns, so that the heading is going down using .T
continuousDataset = dataset.describe().T

#giving the column index as featurename
continuousDataset.index.name = " FEATURENAME"

#get the percentage of missing values
nullValues = dataset.isnull().sum()/len(dataset)*100
continuousDataset['% Miss'] = nullValues

#to get the card data
cardinality = dataset.nunique()
continuousDataset['Card.'] = cardinality

#change the orders of the columns
column_names = ["count", "% Miss", "Card.", "min", "25%", "mean", "50%", "75%", "max", "std"]
continuousDataset = continuousDataset.reindex(columns=column_names)

#change the names of the columns
continuousDataset.rename(columns={'count': 'Count', 'min': 'Min', '25%': '1st Qrt.', 'mean': 'Mean', '50%': 'Median', '75%': '3rd Qrt.', 'max': 'Max', 'std': 'Std Dev.'}, inplace=True)
continuousDataset

#this is to read the continuous data to a csv file
continuousDataset.to_csv('C18387973CONT.csv')



------------------------------------------------------------------------

#to get the list of objects, which is categorical data in a list
#to swap the names of the columns to rows
#to get the headings for categorical data
categoricalDataset = dataset.select_dtypes(include=['object']).copy().describe().T

#giving the column index as featurename
categoricalDataset.index.name = " FEATURENAME"

#get the percentage of missing values
nullValues = dataset.isnull().sum()/len(dataset)*100
categoricalDataset['% Miss'] = nullValues

#this is to get the mode percentage using the mode frequency
categoricalDataset['Mode %'] = categoricalDataset['freq'].div(len(dataset))*100
#categoricalDataset['Mode %'] = ModeFreq

#change the orders of the columns
column_names = ["count", "% Miss", "unique", "top", "freq", "Mode %", "2nd Mode", "2nd Mode Freq.", "2nd Mode %"]
categoricalDataset = categoricalDataset.reindex(columns=column_names)

#change the names of the columns
categoricalDataset.rename(columns={'count': 'Count', "unique": "Card", "top": "Mode", 'freq': 'Mode Freq.'}, inplace=True)

# this is to get the 2nd mode
#i put it in a list
data = []

data.extend(dataset['id\n'].value_counts()[1:2].index.tolist())  #tr16242, 1
data.extend(dataset['workclass\n'].value_counts()[1:2].index.tolist()) #Selmodef-emp-not-inc, 2406
data.extend(dataset['education\n'].value_counts()[1:2].index.tolist())  #some-college, 6938
data.extend(dataset['marital-status\n'].value_counts()[1:2].index.tolist()) # Never-married, 10167
data.extend(dataset['occupation\n'].value_counts()[1:2].index.tolist()) # Craft-repair, 3887
data.extend(dataset['relationship\n'].value_counts()[1:2].index.tolist()) #Not-in-family, 7904
data.extend(dataset['race\n'].value_counts()[1:2].index.tolist()) # Black, 2965
data.extend(dataset['sex\n'].value_counts()[1:2].index.tolist()) # Female, 10235
data.extend(dataset['native-country\n'].value_counts()[1:2].index.tolist()) #Mexico, 607
data.extend(dataset['target'].value_counts()[1:2].index.tolist()) #>50K, 7434
#added the index from the list to the position in the 2nd mode column
categoricalDataset.loc['id\n', '2nd Mode'] = data[0]
categoricalDataset.loc['workclass\n', '2nd Mode'] = data[1]
categoricalDataset.loc['education\n', '2nd Mode'] = data[2]
categoricalDataset.loc['marital-status\n', '2nd Mode'] = data[3]
categoricalDataset.loc['occupation\n', '2nd Mode'] = data[4]
categoricalDataset.loc['relationship\n', '2nd Mode'] = data[5]
categoricalDataset.loc['race\n', '2nd Mode'] = data[6]
categoricalDataset.loc['sex\n', '2nd Mode'] = data[7]
categoricalDataset.loc['native-country\n', '2nd Mode'] = data[8]
categoricalDataset.loc['target', '2nd Mode'] = data[9]

# to check up the 2nd mode frequent item
categoricalDataset.at['id\n', '2nd Mode Freq.'] = dataset['id\n'].value_counts()[1:2]  #tr16242, 1
categoricalDataset.at['workclass\n', '2nd Mode Freq.'] = dataset['workclass\n'].value_counts()[1:2] #Selmodef-emp-not-inc, 2406
categoricalDataset.at['education\n', '2nd Mode Freq.'] = dataset['education\n'].value_counts()[1:2]  #some-college, 6938
categoricalDataset.at['marital-status\n', '2nd Mode Freq.'] = dataset['marital-status\n'].value_counts()[1:2] # Never-married, 10167
categoricalDataset.at['occupation\n', '2nd Mode Freq.'] = dataset['occupation\n'].value_counts()[1:2] # Craft-repair, 3887
categoricalDataset.at['relationship\n', '2nd Mode Freq.'] = dataset['relationship\n'].value_counts()[1:2] #Not-in-family, 7904
categoricalDataset.at['race\n', '2nd Mode Freq.'] = dataset['race\n'].value_counts()[1:2] # Black, 2965
categoricalDataset.at['sex\n', '2nd Mode Freq.'] = dataset['sex\n'].value_counts()[1:2] # Female, 10235
categoricalDataset.at['native-country\n', '2nd Mode Freq.'] = dataset['native-country\n'].value_counts()[1:2] #Mexico, 607
categoricalDataset.at['target', '2nd Mode Freq.'] = dataset['target'].value_counts()[1:2] #>50K, 7434

#to get the 2nd mode percent using the 2nd mode frequency
categoricalDataset['2nd Mode %'] = categoricalDataset['2nd Mode Freq.'].div(len(dataset))*100
categoricalDataset

#this is to read the continuous data to a csv file
categoricalDataset.to_csv('C18387973CAT.csv')





