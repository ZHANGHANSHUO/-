import csv
import matplotlib.pyplot as plt
from datetime import datetime
 
filename=r'weather.csv'
 

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            date=datetime.strptime(row[0],'%Y-%m-%d')
            high=int(row[1])
            low=int(row[3])
        except:
            print(date,'missing date')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
            
print(dates)       
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
 
plt.title('Daily high and low temperature - 2014\nDeath Valley,CA',fontsize=24)
plt.xlabel('',fontsize=12)

fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=10)
plt.tick_params(axis='both',labelsize=12)
 

y_ticks=list(range(20,120,5))
plt.yticks(y_ticks)
 
plt.show()
