import requests
import csv
import pandas as pd
import numpy as np
import os


print("2012년부터 2021년까지 입력 가능합니다.")
date = input()
print("원하는 날짜를 입력하세요 (예시:2012.01.01) : ", date)
df = pd.read_csv('bitcoin.csv')

find_row = df.loc[df['Date'].str.contains(date, na=False)]

print('시가 :', float(find_row['Open']), 'USD')
print('종가 :', float(find_row['Price']), 'USD')
print('고가 :', float(find_row['High']), 'USD')
print('저가 :', float(find_row['Low']), 'USD')
print('거래량 :', int(find_row['Vol']), 'btc')

#%에 따른 하루 변화율
if (float(find_row['Change %']) <= 0.7 and float(find_row['Change %']) >= -0.7):
    print('변화율 : 횡보, ', float(find_row['Change %']), '%')
elif (float(find_row['Change %']) > 0.7):
    print('변화율 : 상승, ', float(find_row['Change %']), '%')
elif (float(find_row['Change %']) < -0.7):
    print('변화율 : 하락, ', float(find_row['Change %']), '%')

#1차. 단기 추세가 존재할 때 (2012.01.21~)
if np.array(find_row.index.tolist()) >= 20:
    sum1 = 0
    sum2 = 0
    i1 = 1
    i2 = 1
    count = 20

    for i1 in range(count):
        sum1 += float(df['Price'].loc[np.array(find_row.index.tolist()) - np.array(i1)])
    
    short_reverage = sum1 / 20
    
    print('20일 평균 가격 :', round(short_reverage, 3), 'USD')
    
    if (short_reverage < float(find_row['Price'])*0.98):
        print('단기 추세: 상승장')
    elif (short_reverage > float(find_row['Price'])*0.98 and short_reverage < float(find_row['Price'])*1.02):
        print('단기 추세: 횡보장')
    elif (short_reverage > float(find_row['Price'])*1.02):
        print('단기 추세: 하락장')

        
    #단기는 존재하지만 장기는 없을 때 (2012.01.21~2012.04.08)
    if np.array(find_row.index.tolist()) < 100:
        print('장기 추세가 존재하지 않습니다')
    
    #장기 추세가 존재할 때 (2012.04.09~)
    else:
        count = 99
        
        for i2 in range(count):
            sum2 += float(df['Price'].loc[np.array(find_row.index.tolist()) - np.array(i2)])

        long_reverage = sum2 / 99
        
        print('99일 평균 가격 :', round(long_reverage, 3), 'USD')

        if (long_reverage < float(find_row['Price'])*0.98):
            print('장기 추세: 상승장')
        elif (long_reverage > float(find_row['Price'])*0.98 and long_reverage < float(find_row['Price'])*1.02):
            print('장기 추세: 횡보장')
        elif (long_reverage > float(find_row['Price'])*1.02):
            print('장기 추세: 하락장')

#2012.01.01~2012.01.20
elif np.array(find_row.index.tolist()) < 20:
    print('장, 단기 추세가 존재하지 않습니다')

#그래프
#기본적으로 안열릴 수 있으니, 주석처리
#pip install matplotlib 하면 그래프 보임
# import matplotlib.pyplot as plt

# plt.figure(figsize=(15, 8))
# plt.rcParams.update({'font.size': 10})
# ax = df.set_index('Date')['Price'].plot(kind='line', marker='d')
# ax.set_ylabel("USD")
# ax.set_xlabel("Date")
# plt.show()

