import csv
import matplotlib.pyplot as plt
import datetime as dt
import statistics as st

dict = {}
dictInterval = {}
dictInterval_weekdays = {}
dictInterval_weekends = {}

filename = 'activity.csv'
with open (filename) as f :
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader :
        steps = row[0]
        if (steps != "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date,'%Y-%m-%d').day)
            interval =int(row[2])
            
            dict.setdefault(str(date), [])
            dict[str(date)].append (int(steps))
            
            dictInterval.setdefault(interval, [])
            dictInterval[interval].append(int(steps))
            
            #Determine Weekend and Weekdays
            #if (date2 % 7 == 0): <-- only prints out Sunday 
            if (date2 < 5):
                dictInterval_weekends.setdefault(interval, [])
                dictInterval_weekends[interval].append(int(steps))
                
            else:
                dictInterval_weekdays.setdefault(interval, [])
                dictInterval_weekdays[interval].append(int(steps))
        
listDate =[]
listTotal = []
listAve =[]

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))
    
#Part A
#Calculate the total number of steps taken per day  
print ("Below is the total numbers of steps taken each day")
for i in listTotal: 
    print(i)     
    
#Make a histogram of the total number of steps each day
fig = plt.figure (dpi =128, figsize = (10,6))
plt.hist(listTotal)
plt.title('Total Steps per day', fontsize = 24)
plt.xlabel('Steps per day', fontsize = 16)
plt.ylabel('Frequency', fontsize = 16)  
plt.yticks(range(0,25,5)) 
plt.show()

#Calculate the mean and median 
print("Mean: ",st.mean(listTotal))
print("Median: ", st.median(sorted(listTotal)))

#Part B
#Make a series plot the 5-minute interval
lst_keys = []
lst_values = []

for i in dictInterval.keys():
    lst_keys.append(i)
for i in dictInterval.values():
    lst_values.append(i)

fig = plt.figure (dpi = 128, figsize = (10,6))
plt.plot(lst_keys,lst_values, c='red')
plt.title ('Average Daily activity pattern', fontsize = 24)
plt.xlabel('5 minute interval', fontsize = 16)
plt.ylabel('average numbers of steps',fontsize =16)
plt.show()

#The maximum number of steps in the interval
import pandas as pd
print("Maximum steps: ", lst_values.max())

#Part C
#Calculate the total number of NA
import numpy as np
df = pd.read_csv(filename, na_values= ['NA'], keep_default_na= False)
print(np.count_nonzero(df.isnull().values))

#Fill in all the NA & replace all the non value with 0 
df.fillna(0)

#Plot the data 
fig = plt.figure (dpi =128, figsize = (10,6))
plt.hist(listTotal)
plt.title('Total Steps per day', fontsize = 24)
plt.xlabel('Steps per day', fontsize = 16)
plt.ylabel('Frequency', fontsize = 16)  
plt.yticks(range(0,25,5)) 
plt.show()


#Part D 
#Create new factor variable in the dataset with two levels - 'weekday and 'weekend'
lst_keys_weekdays = []
lst_values_weekdays = []

for i in dictInterval_weekdays.keys():
    lst_keys_weekdays.append(i)
for i in dictInterval_weekdays.values():
    lst_values_weekdays.append(i)


fig = plt.figure (dpi = 128, figsize = (10,6))
plt.plot(lst_keys_weekdays,lst_values_weekdays, c='red')
plt.title ('Average Daily activity pattern during Weekdays', fontsize = 24)
plt.xlabel('5 minute interval', fontsize = 16)
plt.ylabel('average numbers of steps',fontsize =16)
plt.show()

lst_keys_weekends = []
lst_values_weekends = []


for i in dictInterval_weekends.keys():
    lst_keys_weekends.append(i)
for i in dictInterval_weekends.values():
    lst_values_weekends.append(i)


fig = plt.figure (dpi = 128, figsize = (10,6))
plt.plot(lst_keys_weekends,lst_values_weekends, c='red')
plt.title ('Average Daily activity pattern during Weekends', fontsize = 24)
plt.xlabel('5 minute interval', fontsize = 16)
plt.ylabel('average numbers of steps',fontsize =16)
plt.show()








