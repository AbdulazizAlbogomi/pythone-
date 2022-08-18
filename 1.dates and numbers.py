#لطباعه القيمه المطلفه
number = -199
print(abs(number))

#تقريب الرقم
num2 = 3.675
print(round(num2))

# التربيع
num3 =3
print(pow(num3 , 2))

#اقل قيمه و أكبر قيمه
num4 = 300,400,500,1000
print(min(num4))
print(max(num4))

#  جمع مجموعه من 
num5 = 300,400,500,1000
print(sum(num5))

#الحذر لازم امبورت من مكتبه
import math 
num6 =144
print(math.sqrt(num6))

# باقي القسمه
print(math.remainder(9,3))

#رقم عشوائي
import random
print(random.randint(1,100000))

#انشاء تاريخ

import datetime
date = datetime.date(2020,2,2)
print(date.day)
print(date.year)
print(date.month)

#إنشاء الوقت

time = datetime.time(14,33,22)
print(time.hour)
print(time. minute)
print(time.second)

#معرفة الوقت الحالي
now = datetime.datetime.today()
print(now)

#تحويل التاريخ الى نص

now2 = datetime.datetime.today()
print(now2.strftime('%A %B %Y'))