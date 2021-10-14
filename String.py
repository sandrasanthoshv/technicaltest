str1 = input('Enter a string: ').strip()
substr = input('Enter a string: ').strip()
count=0
for i in range(0, len(str1)):
    for j in range(0, len(substr)):
        if str1[i+j]==substr[j] and j==(len(substr)-1):
            count=count+1
            if str1[i+j]!=substr[j]:
                break
    if i==len(str1)-len(substr):
        break
print (count)