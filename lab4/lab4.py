import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from datetime import date
import calendar
import math


def datasetNormalise()->DataFrame:
    df = pd.read_csv('lab1/dataset.csv', sep=',')
    df = df.dropna()
    df_mean = df["Value"].mean()
    df_median = df["Value"].median()
    df["Mean"] = df.apply(lambda x: (abs(x["Value"] - df_mean)), axis=1)
    df["Median"] = df.apply(lambda x: (abs(x["Value"] - df_median)), axis=1)
    df = df.sort_values(by="Date", ascending=True)
    return df

def findValueByMean(df:DataFrame, value:float)->DataFrame:
    return df.query('Mean > @value')

def findValueInTimedelta(df:DataFrame, first_date:date, last_date:date)->DataFrame:
    #print(df)
    return df.query('Date >= @first_date and Date <= @last_date')

def makePlot(df:DataFrame, year:int, month:int):
    fig = plt.figure(figsize=(10, 5))
    plt.ylabel('Значение')
    plt.xlabel('Дата')
    plt.title('Курс Доллара')
    _, last_day = calendar.monthrange(year, month)
    first = str(date(year, month, 1))
    last = str(date(year, month, last_day))
    #print()
    new_df = findValueInTimedelta(df, first, last)
    #print(findValueInTimedelta(df, first, last))
    x = new_df["Date"]
    y = new_df["Value"]
    y1 = new_df["Value"].mean()
    y2 = new_df["Value"].median()
    plt.scatter(x, y, color='black', linestyle='-', linewidths=1)
    plt.axhline (y=y1, color='red', linestyle='--', label='Среднее значение')
    plt.axhline (y=y2, color='brown', linestyle='--', label='Медиана') 
    plt.legend()
    plt.show()


def main():
    df = datasetNormalise()
    makePlot(df, 2022, 3)
    #print(findValueInTimedelta(df, '2005-03-10', '2005-04-01'))
    #new_df = findValueInTimedelta(df, '2000-01-01', '2000-01-31')
    #print(new_df)
    #df = df.query('Date >= "1998-01-01"')
    #x = df["Date"]
    #y = df["Value"]
    #fig = plt.figure(figsize=(20, 5))
    #plt.ylabel('Значение')
    #plt.xlabel('Дата')
    #plt.title('Курс Доллара')
    #plt.scatter(x, y, color='black', linestyle='-.', linewidths=1) 
    #plt.show()
    #df_month = df.groupby([df.Date.dt.year, df.Date.dt.month]).mean()

if __name__=="__main__":
    main()
