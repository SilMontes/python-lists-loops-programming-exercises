#Import random
import random
#Create the function below:
def matrixBuilder(num):
    newMatrix=[]
    newList=[]
    for i in range(1,num+1):
        newMatrix.append(newList)
    for m in newMatrix:
        newList.append(1)
    return newMatrix
print(matrixBuilder(6))