#自強 原價 2.27 ； 刷卡（前面70km 1.46 打九折) (超過70km  2.27)
#莒光 原價 1.75 ； 刷卡1.46 打九折
#復興 原價 1.46 ； 刷卡1.46 打九折
#區間 原價 1.46 ； 刷卡1.46 打九折

f0=2.27
f1=1.75
f2=1.46
f3=1.46

h=9

if h<10 :
   print('成功')
  
h=0 or print('也能成功')

print('\n')








import time

from datetime import datetime,timezone,timedelta

x = 1
while 1:  # 無窮迴圈
  print('第' + str(x) + '次 while 迴圈')

  print("\n英國_Server 現在時間 "+time.ctime(time.time()))    # 上面 印出 英國_Server 時間

  dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
  dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區 台灣時區
  print('臺灣 現在時間 '+dt2.strftime("%A %Y-%m-%d %H:%M:%S")+'\n')  # 上面 印出 台灣 時間
  
  


  h = [0,0,0,0,1,2,2,1,2,1,2,1,1,2,1]
  
  
  f = ['基隆','臺北',"板橋",'桃園',"苑裡",'泰安','后里','日南',"豐原","大甲",'潭子','臺中港','清水','臺中','沙鹿']
   
  g = [0,28.3,35.5,57.4,167.1,169.7,172.3,174.8,179.1,179.4,184.1,184.7,190.7,193.3,193.9]

  for i in range(0,len(f)):
    # print(str(i)+f[i]+" "+str(g[i])+' 公里處')
    if len(f[i])==2 :  # 站名 是 2個字 時
      print('%3d %-4s %6.1f %s' % (i,f[i],g[i],'公里處'))
    else :  # 站名 是 3個字 時
      print('%3d %s %6.1f %s' % (i,f[i],g[i],'公里處'))


  
  flag=0
  while '趙振宇':
   s=input("\n請輸入  起站 : ") 
   s=s.replace('台','臺')
   #i=0
   #while i<len(f):
   for i in range(0,len(f)):
     #print('第1個'+str(i))
     if s==f[i]:
        flag=1 
        break
     #i+=1  
   #if i<len(f):
   if flag:   
      break
  #print('第2個'+str(i))
  print("您輸入的起站是 "+s)

  print()
  
  flag=0
  while '王':
   t=input("請輸入  迄站 : ")
   t=t.replace('台','臺') 
   #j=0
   #while j<len(f):
   for j in range(0,len(f)):
     if t==f[j]:
        flag=1
        break
     #j+=1
   if flag:
      break
  print("您輸入的迄站是 "+t)
  
  # z=abs(eval(str(g[i])+'-'+str(g[j])))
  if h[i]==2 and h[j]==1:
    z=203.8-g[i]+2.2+208.5-g[j]
    print('\n山跨海 需特殊處理')
  elif h[i]==1 and h[j]==2:
    z=203.8-g[j]+2.2+208.5-g[i]
    print('\n海跨山 需特殊處理')
  else:
      print('\n一般 不需特殊處理')
      z=abs(g[i]-g[j])
  print('\n搭乘距離 = '+str(z)+' 公里')
  
  while 1:
    y = input('\n請輸入 車種\n自強=0 莒光=1 復興=2 區間(快)=3 : ')
    if y == '0' or y == '1' or y == '2' or y == '3':
      break
      
  while ' ':
    w = input('\n是否使用悠遊卡 0為不使用 1為使用 : ')
    if w=='0' or w=='1':
      break

  if z<10:
    z=10   # 不足10公里 以10公里計費

  if w=='1':  # 代表 有刷卡
    if y == '0' and z > 70:  # 自強號 且 超過70公里
      a = 70 * f3 * 0.9 + (z - 70) * f0
    else:  # 莒光號 或 復興號 或 區間(快) 或 自強號但不超過70公里
      a = z * f3 * 0.9
  else:  # 即 w=='0'  代表 無刷卡
    if y == '0':  # 自強號
      a = z * f0
    else:
      if y == '1':  # 莒光號
        a = z * f1
      else:
        if y == '2':  # 復興號
          a = z * f2
        else:  # 區間(快)
          a = z * f3

  print('\n\n******  需付金額 ' + str(round(a)) + ' 元')

  print('\n')
  x += 1