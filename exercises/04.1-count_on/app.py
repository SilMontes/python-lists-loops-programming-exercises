
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello=[]
for item in my_list:
    if type(item)==type([]) or type(item)==type({}):
        hello.append(item)
print(hello)
