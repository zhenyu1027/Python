#區間 舊1.46 新1.82 刷卡打九折
#自強2.27 刷卡前70 1.46 打九折 後2.27
#莒光1.75 刷卡1.46 打九折
#復興 舊1.46 新1.82 刷卡1.46 打九折
x=1
while True :
  print('第'+str(x)+'次 while 迴圈')
  y=int(input('輸入車種\n自強=0 莒光=1 復興=2 區間(快)=3 : '))
  z=abs(eval(input('輸入總公里數：')))
  print(str(z)+' 公里')
  if z<10:
     z=10
  w=int(input('是否使用悠遊卡 1為使用 0為不使用 : '))
  if w==0 and y==0:
     a=z*2.27
  elif w==0 and y==1:
     a=z*1.75
  elif w==0 and y==2:
     a=z*1.46
  elif w==0 and y==3:
     a=z*1.46
  elif w==1 and y==0 and z>70:
     a=70*1.46*0.9+(z-70)*2.27
  elif w==1 and (y==0 or y==1 or y==2 or y==3):
     a=z*1.46*0.9
  a=round(a)
  print('車資 '+str(a)+' 元')
  print('\n')
  x+=1