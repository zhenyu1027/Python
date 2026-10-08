def train_fare(f,r1,r2,y,w) :




 f0=2.27
 f1=1.75
 f2=1.46
 f3=1.46



 h = [0,0,0,0,1,2,2,1,2,1,2,1,1,2,1]
  
  
 
   
 g = [0,28.3,35.5,57.4,167.1,169.7,172.3,174.8,179.1,179.4,184.1,184.7,190.7,193.3,193.9]



  
  
  
 s=r1
   #i=0
   #while i<len(f):
 for i in range(0,len(f)):
     #print('第1個'+str(i))
     if s==f[i]: 
        break
     #i+=1  
   #if i<len(f):
   
  #print('第2個'+str(i))
 print("您輸入的起站是 "+s)

  
  
  
 t=r2 
   #j=0
   #while j<len(f):
 for j in range(0,len(f)):
     if t==f[j]:
        break
     #j+=1
 print("您輸入的迄站是 "+t)
  
  # z=abs(eval(str(g[i])+'-'+str(g[j])))
 if h[i]==2 and h[j]==1:
    z=203.8-g[i]+2.2+208.5-g[j]
    #print('山跨海 要特殊處理')
 elif h[i]==1 and h[j]==2:
    z=203.8-g[j]+2.2+208.5-g[i]
    #print('海跨山 要特殊處理')
 else:
      #print('一般 不需特殊處理')
      z=abs(g[i]-g[j])
 print('搭乘距離 = '+str(z)+' 公里')
  
      
  

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

 print('******  需付金額 ' + str(round(a)) + ' 元')

 print('\n')
#######################################
import itertools

f = ['基隆','臺北',"板橋",'桃園',"苑裡",'泰安','后里','日南',"豐原","大甲",'潭子','臺中港','清水','臺中','沙鹿']


for i in itertools.combinations(f,2):
  train_fare(f,i[0],i[1],'3','1')
#print(list(itertools.combinations(f,2)))
    
'''
for i in range(len(f)):
  for j in range(len(f)):
    if i==j:
      continue 
    train_fare(f,f[i],f[j],'3',1)
'''