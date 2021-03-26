par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for i in par:
    if(i != " "):
        x=i.lower()
        counts[x]=par.count(x)

print(counts)
#print(sorted(counts))

