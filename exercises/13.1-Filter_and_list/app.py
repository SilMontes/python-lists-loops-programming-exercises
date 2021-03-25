
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_names(name):
    return name.startswith("R")
resulting_names=list(filter(filter_names,all_names))
print(resulting_names)




