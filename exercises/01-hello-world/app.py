import datetime
# On the next line, use Python's print function to say `Hello World` in the console (this exercise is case-sensitive!)
#print("Hello World")
        # x is the argument
add5 = lambda x: x+5
print(add5(3))

square= lambda x: x*x
print(square(4))

get_tens= lambda p: int(p/10)%10
print(get_tens(80))

#sorting a list of tuples using lambada
list1= [("eggs",5.25), ("honey", 9.70), ("carrots",1.10), ("peaches",2.45)]
#def looping(item):
 #   return item
#list1_result=list(map(looping,list1))
#print(list1_result)

#the lambda function is been used as the key
#sort imprime de menor a mayor, segun el argumento. En este caso, al pasarle i a x, le estamos diciendo que ordene según los valores de cada key
#list1.sort(key = lambda x:x[1])
#print(list1)

list2=[{"make":"Ford", "model":"Focus","year":2013},{"make":"Tesla", "model":"Focus22","year":2015},{"make":"Ford33", "model":"Focus33","year":2000}]
#list2B=sorted(list2,key=lambda x:x["year"]) #x represents each dictionary in this list
#print(list2B)

list3=[1,2,3,4,5,6,7]
#list3B=list(filter(lambda x: x % 2 == 0, list3)) ##it returns the items that pass the filter, that is, if x is even
#print(list3B)
odds= lambda x: x % 2 == 1
list3C=list(filter(odds,list3))
print(list3C)

#this squares each item on the list
list3D=list(map(lambda x: x**2, list3))
print(list3D)


#lambda conditionals
#evaluará si el argumento inicia con la letra J
starts_with = lambda x : True if x.startswith("J") else False
print(starts_with("Silvia")) 
print(starts_with("john")) #the result will be false as the function is case sensitive

#in this case we are going to get the word before the word specified
# s is for the sentence
# w is for the word
#this function will start be spliting the sentence list, the it will take the same list and the, it wiill take the index of word -1 (-1 to take the word before). If the word is not in the sentence it will return None
                                                  #bu changing 1 and - we can get words in different positions
word_before=lambda s, w : s.split()[s.split().index(w)+-1] if w in s else None
sentence="There is a cute cat on the table"
print(word_before(sentence,"cat"))

#lambda on DataTime Objects 
now = datetime.datetime.now()
print(now)
current_year=lambda x: x.year
print(current_year(now)) 
current_month=lambda x: x.month
print(current_month(now))
current_hour=lambda x: x.hour
print(current_hour(now))

def do_something(f,val):
    return f(val)   #in this function f will act as a function and val as an argument

func=lambda x: x**3  #numero=x elevado a 3
print(func(2))
print(do_something(func,2))

#the following lambda function will test if a given argument is or not a numerical value. It return a boolean
   #it remove .  and empty space " ". We must add 1. Si es un negativo, la respuesta será falso
isnum = lambda q: q.replace(".","",1).isdigit()
print(isnum('23455'))
#modificamos la funcion anterior para que valide los numeros negativos
                #si el primer caracter es signo negativo, lo ignorará. Si no hay signo negativo, llamara a la funcion isnum para validar el valor de r
is_num = lambda r: isnum(r[1:]) if r[0] =="-" else isnum(r)
print(is_num("-16.44"))

#checking and converting the argument to a number
# if s is a number will gonna call the float function thet returns the number otherwise it will return -1
# tonum calls is_num and is_num calls to isnum
tonum = lambda s: float(s) if is_num(s) else -1
print(tonum("30y"))
print(tonum("-21.88"), type(tonum("-21.88")))