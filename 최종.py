# -*- coding: utf-8 -*-
"""최종

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U8IiI_EBJodm49fcQOiJjx55mhnpMY_Q
"""

def solution(coordinate):
  coordinate=sorted(coordinate)
  x=[0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0]
  x_1=[0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0]
  for i in range(len(coordinate)):
    a=coordinate[i][0]
    b=coordinate[i][1]
    c=coordinate[i][1]+10
    if x[a]==0:
      x[a:a+10]=b,b,b,b,b,b,b,b,b,b
    else:
      k=coordinate[i][0]-coordinate[i-1][0]
      if max(x[a:coordinate[i-1][0]+10])<b:
        for i in range(1,k+1):
          x[a+10-i]=b
      else:
        x[a:a+10]=b,b,b,b,b,b,b,b,b,b
    if x_1[a]==0:
      x_1[a:a+10]=c,c,c,c,c,c,c,c,c,c
    else:
      if x_1[a]<=c:
        x_1[a:a+10]=c,c,c,c,c,c,c,c,c,c
      else:
        p=coordinate[i][0]-coordinate[i-1][0]
        for q in range(1,p+1):
          x_1[a+10-q]=c
  result_x=sum(x)
  result_x_1=sum(x_1)
  return result_x_1-result_x
print(solution(coordinate=[(5,2),(7,6),(8,10)]))
print(solution(coordinate=[(1,5),(7,6),(8,9),(2,7),(5,8),(58,20),(2,2),(80,90),(76,50),(15,23)]))

def solution(coordinate):
  x=[]
  for a in range(100):            #가로와 세로의 길이가 100인 도화지를 1*1크기의 정사각형으로 나누기
    for b in range(100):
      x.append(0)
  result_1=x.count(0)             # 총 초기리스트의 0의 개수 세기
  for i in range(len(coordinate)):      # coordinate의 좌표 개수만큼 반복
    for p in range(10):                 # 각 좌표가 가로, 세로길이가 10인 색종이기때문에 색종이가 해당하는 인덱스에 1 더해주기
      for q in range(10):
        x[coordinate[i][0]+q+(coordinate[i][1]+p)*100]+=1
  result_2=x.count(0)
  return result_1-result_2             # 도화지의 0의 개수는 색종이가 없는 부분으로 원래 전체 0의 개수에서 색종이로 덮이지 않은 부분인 0의 개수를 빼면 색종이가 있는 부분을 찾을 수 있음

import random
coordinate=[]
for i in range(0,10**5):
  number_1=random.randint(0,89)
  number_2=random.randint(0,89)
  coordinate.append((number_1,number_2))
print(coordinate)

def solution(coordinate):
  x=[]
  for a in range(100):            #가로와 세로의 길이가 100인 도화지를 1*1크기의 정사각형으로 나누기
    for b in range(100):
      x.append(0)
  result_1=x.count(0)             # 총 초기리스트의 0의 개수 세기
  for i in range(len(coordinate)):      # coordinate의 좌표 개수만큼 반복
    for p in range(10):                 # 각 좌표가 가로, 세로길이가 10인 색종이기때문에 색종이가 해당하는 인덱스에 1 더해주기
      for q in range(10):
        x[coordinate[i][0]+q+(coordinate[i][1]+p)*100]+=1
  result_2=x.count(0)
  return result_1-result_2             # 도화지의 0의 개수는 색종이가 없는 부분으로 원래 전체 0의 개수에서 색종이로 덮이지 않은 부분인 0의 개수를 빼면 색종이가 있는 부분을 찾을 수 있음
print(solution(coordinate))

import time
start_time=time.time()
print(solution(coordinate))
end_time=time.time()
print(end_time-start_time)

x=[]
for i in range(100):
  for j in range(100):
    x.append(0)
print(len(x))