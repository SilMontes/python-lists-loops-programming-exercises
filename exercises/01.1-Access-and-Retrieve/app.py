
my_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

# 1. print the item here
print(my_list[2])
# 2. change the position were 'thursday' is to None
my_list[4]=None
# 3. print that position now here
print(my_list[4])


#PRACTICING
#slicing
x="Electrifying"
print(x[3:7]) #items from 1 to 6
print(x[1:6:2]) #items 1, 3 and 5   //from 1 to 6 steping by 2
print(x[4:]) #item to the end
print(x[:6]) #0 to 5
print(x[-1]) #last item
print(x[-3:]) #last 3 items
print(x[:-2]) #all except las 2 items
print("Count", x.count("i"))


# index and item
x = [7,8,3]
for index,item in enumerate(x):
    print(index,item)
print(sum(x[-2:])) #suma de los dos últimos

names=["John", "Zenia","Luke","Ana","Aaron","Ana"]
print(max(names)) # maximo alfabeticamente
print(min(names)) # minimo alfabeticamente
print(sorted(names[0])) #"devulve orde alfabetico"
print(sorted(names))
print(names.count("Ana")) #cuantas veces se repite Ana
print(names.index("Zenia")) #imprime el idex de el elemento dado

#unpacking    el numero de variabls debe ser de la misma cantidad de elementos 
animals=["pig","cow","horse"]
a,b,c=animals # a is pig b is cow...
print(animals)
print(a)

new_list=[ele for ele in range(8)]
print(new_list)

#numeros mayores a 5 elevados a la 2
new_list2=[z**2 for z in range(10) if z>4]
print(new_list2)
new_list2.extend(new_list)
print(new_list2)

y=[5,6,7,8,9,]
p=[9,9,9]
y.insert(4,p) #insert receives 2 parameters: index, item
print(y)
print(y.pop()) #prints the last item of the list
