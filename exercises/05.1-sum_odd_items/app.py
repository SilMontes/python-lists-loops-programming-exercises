arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds():
    odd_number=[]
    for item in arr:
        if item % 2 != 0:
            odd_number.append(item)
            #print(item)
    return odd_number

print(sumOdds())


