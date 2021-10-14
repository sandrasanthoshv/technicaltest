oldstr = input('Enter a string: ')
newstr = ''
for i in oldstr:
    if (i.isupper() == True):
        newstr += i.lower()
    elif (i.islower() == True):
        newstr += i.upper()
    elif (i.isspace() == True):
        newstr += i
        
print ("Old String : ",oldstr)
print ("New String : ",newstr)
