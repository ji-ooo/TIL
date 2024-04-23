from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from .models import Keyword,Trend
from .forms import KeywordForm
from django.utils import timezone
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import base64
from io import BytesIO

# Create your views here.
def get_data(k,period):
    url = f'https://www.google.com/search?q={k}&tbs=qdr:{period}'

    # response = requests.get(url)
    # print(response.text)

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    result_stats = soup.select_one('#result-stats')
    try:
        return int(result_stats.text[7:-10].replace(',',''))
    except ValueError:
        return get_data(k,period)
    

def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword',)
    keywords = Keyword.objects.all()
    form = KeywordForm()
    
    context = {
        'form':form,
        'keywords':keywords,

    }
    return render(request,'trends/keyword.html',context)


def keyword_detail(request,pk):
    kw = Keyword.objects.get(pk=pk)
    kw.delete()
    return redirect('trends:keyword')


def crawling(request):
    keywords= Keyword.objects.all()
    for k in keywords:
        # trend_id = k.pk
        k_count = get_data(k.name,'all')
        
        kco, created = Trend.objects.get_or_create(
            name = k.name, search_period = 'all',
            defaults={
                'keyword': k,
                'result': k_count
                })
        if created:
            pass
        else:
            tr = Trend.objects.get(name=k.name,search_period = 'all')
            tr.result = k_count
            tr.created_at = timezone.now()
            tr.save()
    trends = Trend.objects.all()

    context = {
        'trends':trends
    }
    return render(request,'trends/crawling.html',context)


def crawling_histogram(request):
    conn = sqlite3.connect('db.sqlite3')
    df = pd.read_sql("SELECT * FROM trends_trend WHERE search_period = 'all'", conn)
    df = df.loc[:,['name','result']]

    plt.clf()
    plt.bar(df['name'],df['result'])
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend(['Trends'])
    plt.grid(True)

    Buffer = BytesIO()
    plt.savefig(Buffer,format='png')
    image_base64 = base64.b64encode(Buffer.getvalue()).decode('utf-8').replace('\n', '')
    Buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request,'trends/crawling_histogram.html',context)

def crawling_advanced(request):
    keywords= Keyword.objects.all()
    for k in keywords:
        k_count = get_data(k.name,'y')
        kco, created = Trend.objects.get_or_create(
            name = k.name, search_period = 'year',
            defaults= {
                'keyword': k,
                'result': k_count
                })
        if created:
            pass
        else:
            tr = Trend.objects.get(name=k.name,search_period = 'year')
            tr.result = k_count
            tr.created_at = timezone.now()
            tr.save()

    trends = Trend.objects.all()

    conn = sqlite3.connect('db.sqlite3')
    df = pd.read_sql("SELECT * FROM trends_trend WHERE search_period = 'year'", conn)
    df = df.loc[:,['name','result']]
    plt.clf()
    plt.bar(df['name'],df['result'])
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend(['Trends'])
    plt.grid(True)

    Buffer = BytesIO()
    plt.savefig(Buffer,format='png')
    image_base64 = base64.b64encode(Buffer.getvalue()).decode('utf-8').replace('\n', '')
    Buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request,'trends/crawling_advanced.html',context)
