incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
transformedData=[]
def my_var(transformedData):
    transformed=list(map(lambda person: person["name"]+" "+person["lastName"],transformedData))
    #for item in argum:
    #    transformedData.append(item.get("name")+" "+item.get("lastName"))
       # transformedData.append(item.key["name"]+" "+item.key["lastName"])
    return transformed

print(my_var(incomingAJAXData))