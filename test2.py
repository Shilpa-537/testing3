#!2.    Question

dic ={"Mary":"Li","James":"O'Day","Thomas":"Miller","William":"Garcia","Elizabeth":"Davis"}

print 'sorted primarily by length of last name' 
ascending = sorted(dic, key =lambda x: len(dic[x]))
for item in ascending:
    print item,'---',dic[item]
print
print 'secondary sort alphabetically by first name'

li =  sorted(ascending)

for item in li:
    print item,'---',dic[item]
