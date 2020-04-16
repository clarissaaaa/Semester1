#16-2
import csv
from datetime import datetime 
from matplotlib import pyplot as plt
filename = 'sitka_weather_2014.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_daate, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
fig =plt.figure(dpi=128, figsize= (10,6))
plt.title("Daily High and Low Temperature - 2014 \n Sitka,AK")
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.plot (dates,highs,c='blue',alpha =1)
plt.plot (dates,lows,c='red',alpha =1)
plt.fill_between(dates,highs,lows, facecolor ='green', alpha =0.1)