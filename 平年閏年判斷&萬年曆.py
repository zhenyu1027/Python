
b=[31,28,31,30,31,30,31,31,30,31,30,31]
c=('一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月')
a=int(input('請輸入西元年數 : '))


if a%400==0 or (a%4==0 and a%100!=0) :
  print('是閏年')
  b[1]+=1
else:
  print('是平年')


#from datetime import date
#y=date(a, 1, 1).isoweekday()
y= ((a-1)*365+(a-1)//400+(a-1)//4-(a-1)//100) % 7 + 1




#y%=7
if y==7:
   y=0
print('此年元旦 是 星期'+str(y))
print()


for j in range(0,12):
 print('\n\n\n'+c[j])
 print(' 日  一  二  三  四  五  六')
 for i in range(0,y):
   print('    ',end='')
 for i in range(1,b[j]+1):
  if i<10:
    print(' ',end='')
  print(' '+str(i)+' ' ,end='')
  y+=1
  #y%=7
  if y%7==0:
     y=0
     print()
