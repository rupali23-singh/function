def add(*b):
    result=0
    for i in b:
        result=result+i
    return(result)
print(add(1,2,3,4,5))




'''def even_numbers(num1,num2):
    i=0
    c=0
    while i<len(num1):
        c=num1[i]+num2[i]
        c+=1
    i=i+1
print(even_numbers([1, 2, 3, 4, 5,],[6, 7, 8, 9]))