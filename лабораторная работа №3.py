# -*- coding: utf-8 -*-
"""Копия блокнота "Untitled1.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AfSYD-RoYfJtxLGgSZHYZnqJ2llZrUeN
"""

a = input('Введите номер мсяца от 1 до 12:')
if a == '1':
  print('Январь')
if a == '2':
  print('Февраль')
if a == '3':
  print('Март')
if a == '4':
  print('Апрель')
if a == '5':
  print('Май')
if a == '6':
  print('Июнь')
if a == '7':
  print('Июль')
if a == '8':
  print('Август')
if a == '9':
  print('Сентябрь')
if a == '10':
  print('Октябрь')
if a == '11':
  print('Ноябрь')
if a == '12':
  print('Декабрь')



a = int(input('Введите число:'))
b = a % 2
if b == 0:
  print('число чётное')
else:
  print('Число нечётное')

N = int(input('Введите число:'))
if N > 40:
  print('stonks')
elif N < 40:
  print('not stonks')
else:
  print('Зачем ты написал 40?')

def is_year_leap(year):
  if year % 4 == 0:
    return True
  else:
    return False

def is_prime():
  n = int(input('введите число:'))
  a =0
  for i in range(2, n//2 +1):
    if (n % i == 0):
      a = a+1
  if a <= 0:
    return True
  else:
    return False
is_prime()

a = int(input('число 1:'))
b = int(input('число 2:'))
if a/b > 3.6 or (b>abs((-138/2)**1.3) and b<(abs(((-69/28**5.1)*4)+1))):
  a,b = b,a
  print(a,b)
else:
  print(a, b)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
Num = 0
Oddnum = 0
Sum = 0
if a != b:
  if a != c:
    if a != d:
      if a != e:
        if b != c:
          if b != d:
            if b != e:
              if c != d:
                if c != e:
                  if d != e:
                    if a%2 == 0:
                      Num += 1
                    if b%2 == 0:
                      Num += 1
                    if c%2 == 0:
                      Num += 1
                    if d%2 == 0:
                      Num += 1
                    if e%2 == 0:
                      Num += 1
                    if a%2 == 0:
                      Oddnum += 1
                    if b%2 == 0:
                      Oddnum += 1
                    if c%2 == 0:
                      Oddnum += 1
                    if d%2 == 0:
                      Oddnum += 1
                    if e%2 == 0:
                      Oddnum += 1                
                    if a >= -256 and a<= 1024:
                      Sum += 1
                    if b >= -256 and b<= 1024:
                      Sum += 1
                    if c >= -256 and c<= 1024:
                      Sum += 1
                    if d >= -256 and d<= 1024:
                      Sum += 1
                    if e >= -256 and e<= 1024:
                      Sum += 113
                    print(Num, Oddnum, Sum)

a = int(input('Число 1:'))
b = int(input('Число 1:'))
c = int(input('Число 1:'))
decision = (((a**2)+(b**3)) / (c+3)) / 4
if decision % 2 == 1:
  print('Число нечетное')
else:
  print('Число четное')
print('Решение:', decision)