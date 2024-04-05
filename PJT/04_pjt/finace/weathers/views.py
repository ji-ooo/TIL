from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
# Create your views here.
plt.switch_backend('Agg')
csv_path = 'austin_weather.csv'
df = pd.read_csv(csv_path)
def problem1(request):
    
    context = {
        'df':df
    }

    return render(request,'weathers/problem1.html',context)
    

def problem2(request):
    dc = df.loc[:,['Date','TempHighF','TempAvgF','TempLowF']]
    dc['TempHighF'] = dc['TempHighF'].astype(int)
    dc['TempAvgF'] = dc['TempAvgF'].astype(int)
    dc['TempLowF'] = dc['TempLowF'].astype(int)
    dc['Date'] = pd.to_datetime(dc['Date'])

    plt.clf()
    plt.plot(dc['Date'], dc['TempHighF'], label='TempHighF')
    plt.plot(dc['Date'], dc['TempAvgF'], label='TempAvgF')
    plt.plot(dc['Date'], dc['TempLowF'], label='TempLowF')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend()
    plt.grid(True)

    Buffer = BytesIO()
    plt.savefig(Buffer,format='png')
    image_base64 = base64.b64encode(Buffer.getvalue()).decode('utf-8').replace('\n', '')
    Buffer.close()


    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request,'weathers/problem2.html',context)

def problem3(request):
    dp = df.loc[:,['Date','TempHighF','TempAvgF','TempLowF']]
    dp['Date'] = pd.to_datetime(dp['Date'])

    df_monthly_cut = dp.groupby(dp['Date'].dt.strftime("%Y-%m")).mean()
    dp['TempHighF'] = dp['TempHighF'].astype(int)
    dp['TempAvgF'] = dp['TempAvgF'].astype(int)
    dp['TempLowF'] = dp['TempLowF'].astype(int)

    plt.clf()
    plt.plot(df_monthly_cut['Date'], df_monthly_cut['TempHighF'], label='TempHighF')
    plt.plot(df_monthly_cut['Date'], df_monthly_cut['TempAvgF'], label='TempAvgF')
    plt.plot(df_monthly_cut['Date'], df_monthly_cut['TempLowF'], label='TempLowF')
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.legend()
    plt.grid(True)

    Buffer = BytesIO()
    plt.savefig(Buffer,format='png')
    image_base64 = base64.b64encode(Buffer.getvalue()).decode('utf-8').replace('\n', '')
    Buffer.close()
    
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request,'weathers/problem3.html',context)

def problem4(request):
    events = ['No Events','Rain','Thunderstorm','Fog','Snow']
    event_dict ={i:0 for i in events}
    events_count = df['Events'].replace(' ', np.nan).fillna('No Events')
    events_count = events_count.value_counts()

    for event, count in events_count.items():
        for i in event_dict:
            if i in event:
                event_dict[i] += count

    counts = []
    for i in events:
        counts.append(event_dict[i])

    plt.bar(events,counts)
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid(True)

    Buffer = BytesIO()
    plt.savefig(Buffer,format='png')
    image_base64 = base64.b64encode(Buffer.getvalue()).decode('utf-8').replace('\n', '')
    Buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'weathers/problem4.html', context)
    
