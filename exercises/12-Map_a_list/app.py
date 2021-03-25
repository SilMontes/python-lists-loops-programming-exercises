Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
   return (x*9/5)+32
                    #funcion para cad elemento del iterable          #iterable
result = list(map(fahrenheit_values, Celsius_values))
print(result) #lo que devolverá map 
