# num=float(input())
# num_sqrt=num**0.5
# print('%0.2f'%num_sqrt)
import math
import numbers

#美团笔试题一（练习题）
#数列的定义如下： 数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
#输入数据有多组，每组占一行，由两个整数n（n<10000）和m(m<1000)组成，n和m的含义如前所述。
#对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。
# while 1:
#  nm = list(map(float,input().split(" ")))
#  N=nm[0]
#  M=nm[1]
#  m=int(M)
#  s=[None]*m
#  for i in range(m):
#         if i==0:
#            s[i]=N
#         else:
#            s[i] = (N**(0.5**i))
#  sum_sum=0
#  for j in range(m):
#         sum_sum=s[j]+sum_sum
#
#  print('%0.2f'%sum_sum)

#水仙花  第九次调试 100%AC
# while 1:
#   mn = list(map(str,input().split(" ")))
#   M=int(mn[0])
#   N=int(mn[1])
#   # print(M,N)
#   # print(mn[0][0])
#   # print(type(mn[0][0]))
#   sym=0
#   str1 = mn[0]
#   for i in range(M,N+1):
#
#       if int(str1[0])*100+int(str1[1])*10+int(str1[2])*1== int(str1[0])**3+int(str1[1])**3+int(str1[2])**3:
#           print(int(str1[0])*100+int(str1[1])*10+int(str1[2])*1,end=' ')
#           sym=sym+1
#       str1=str(i+1)
#
#
#
#   if sym==0:
#       print("no")
#   else:
#       print()

import  math
# n,n0=map(int,input().split(" "))
# houselist=list(map(int,input().split(" ")))
# k=0
# for i in range(n):
#     if houselist[i]==0:
#        k=i
# for i in range(n):
#     if houselist[i]!=0 and i<k:
#         houselist[i]=houselist[i]*(k-i)
#     if houselist[i]!=0 and i>k:
#         houselist[i] = houselist[i] * (i-k)
# min_min=houselist[0]
# for i in range(n):
#     if houselist[i] <= min_min and i!=k:
#         min_min=houselist[i]
#         min_i=i
#
# print(min_i+1)


# n,m=map(int,input().split(" "))
# Mlist=list(map(int,input().split(" ")))
# Tlist=list(map(int,input().split(" ")))
# max=0
#
# Max=0
# for d in range(1,1001):
#    Mscore = 0
#    Tscore = 0
#    for i in range(n):
#      if Mlist[i]  <=d:
#          Mscore=Mscore+1
#      if Mlist[i] >d:
#          Mscore=Mscore+2
#    for i in range(m):
#      if Tlist[i]  <=d:
#          Tscore=Tscore+1
#      if Tlist[i] >d:
#          Tscore=Tscore+2
#    max=Tscore-Mscore
#    if max>Max and max >=0:
#        Max=max
# print(Max)
# import math
# def mofa(b):
#     for j in range(b):
#       B=0
#       s=math.pow(0,n)
#       for i in range(s,n):
#         del Nlist[i]
#         B=B+1
#         if B==3:
#            break
# n=input()
# Nlist=list(map(str,input()))
# score0=0
# score1=0
# scoreSub=0
# k=int(n)
# for i in range(k):
#     if int(Nlist[i])==0:
#         score0=score0+1
#     if int(Nlist[i])==1:
#         score1=score1+1
# if score1>=score0:
#    scoreSub=score1-score0
# if score1<score0:
#    scoreSub=score0-score1
#
# print(scoreSub)
n=input(int)
s = list(map(str, input()))
score_str_son=0
for i in range(n):
    str_son = s[i]
    for j in range(n):

      if i ==0:
          str_son=list(s[j])
          score_str_son=score_str_son+1
          break

      str_son=str_son+s[j]
      for k in range(len(str_son)):
          if str_son[k]==str_son[k+1]:
              print()

print(score_str_son)







