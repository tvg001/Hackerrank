#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matqueue(Array,ins,ine,es,en):
    j=ins
    k=es
    qu=[]
    while k<=en:
        qu.append(Array[j][k])
        k+=1
    k-=1
    while k==en and j<ine:
        j+=1
        qu.append(Array[j][k])
        
    #print(j)
    while j==ine and k>es:
        k-=1
        qu.append(Array[j][k])
    #print(k)
    j-=1
    while k==es and j>ins:
        qu.append(Array[j][k])
        j-=1
    return qu


def Matrixfill(out,ins,ine,es,en,qu):
    j=ins
    k=es
    while k<=en :
        out[j][k]=qu.pop(0)
        k+=1
    k-=1
    while k==en and j<ine:
        j+=1
        out[j][k]=qu.pop(0)
    while j==ine and k>es:
        k-=1
        out[j][k]=qu.pop(0)
    j-=1
    while k==es and j>ins:
        out[j][k]=qu.pop(0)
        j-=1
def rotate(Array,out,ins,ine,es,en,r):
    while ins<ine and es<en:
        qu=matqueue(Array,ins,ine,es,en)
        size=len(qu)
        temp=r%size
        i=0
        for i in range(0,temp):
            qu.append(qu.pop(0))
        Matrixfill(out,ins,ine,es,en,qu)
        ins+=1
        ine-=1
        es+=1
        en-=1
def matrixRotation(matrix,m,n,r):
    out=[]
    for i in range(m):
        temp=[0]*n
        out.append(temp)
    rotate(matrix,out,0,m-1,0,n-1,r)
    for i in range(m):
        for j in range(n):
             print(out[i][j],end=' ')
        print()

    
    

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix,m,n,r)
