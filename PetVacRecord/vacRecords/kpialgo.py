print("enter number of different values in numerator")
numerator_length=int(input())
numerator=[]
numerator_function=[]

for x in range(0,numerator_length):
    print("Enter number "+ str(x+1) +" value in numerator")
    numerator.append(int(input("")))
    
    while x<numerator_length-1:   
        print("Enter the function +,-,*,/")  
        numerator_function.append(input())
        break

print("enter number of different values in denominator")
denominator_length=int(input())
denominator=[]
denominator_function=[]

for x in range(0,denominator_length):
    print("Enter number "+ str(x+1) +" value in denominator")
    denominator.append(int(input("")))
    
    while x<denominator_length-1:   
        print("Enter the function +,-,*,/")  
        denominator_function.append(input())
        break

print(numerator)
print(denominator)    

# numerator=[1,2,3,4,5,6]  
# numerator_function=["divide","add","divide","multiply","add"]

# denominator=[1,2,3,4,5]
# denominator_function=["add","divide","multiply","add"]

def calc(array,function_array):
    print(array)
    
    division=[i for i, x in enumerate(function_array) if x=="/"]
    print("division at ",division)
    counter=0
    for x in division:
        if array[x+1-counter]==0:
            return "e"
        array[x-counter] = array[x-counter]/array[x+1-counter]
        function_array.remove("/")
        array.pop(x+1-counter)
        counter=counter+1
        print(array)
        print(function_array)

    multiplication= [i for i, x in enumerate(function_array) if x=="*"] 
    print("multiplication at :", multiplication)
    counter=0 
    for x in multiplication:
        array[x-counter] =array[x-counter]*array[x+1-counter]
        function_array.remove("*")
        array.pop(x+1-counter)
        counter=counter+1
        print(array)
        print(function_array)

    addition= [i for i, x in enumerate(function_array) if x=="+"] 
    print("addition at :", addition)
    counter=0 
    for x in addition:
        array[x-counter] =array[x-counter]+array[x+1-counter]
        function_array.remove("+")
        array.pop(x+1-counter)
        counter=counter+1
        print(array)
        print(function_array)
          
    subtraction= [i for i, x in enumerate(function_array) if x=="-"] 
    print("subtraction at :", subtraction) 
    counter=0
    for x in subtraction:
        array[x-counter] =array[x-counter]-array[x+1-counter]
        function_array.remove("-")
        array.pop(x+1-counter)
        counter=counter+1
        print(array)
        print(function_array)

    print(function_array)
    print("solution ",array)
    return array[0]

def kpi2(numerator,denominator,numerator_function,denominator_function):

    print("numerator Part ")
    numerator=calc(numerator,numerator_function)
    print()
    
    if numerator=="e":
        print("division by zero not allowed")
        return numerator

    print("Denominator Part")
    if len(denominator)==0:
        denominator=[1]
    denominator=calc(denominator,denominator_function)
    print()
    if denominator=="e":
        print("division by zero not allowed")
        return denominator

    if denominator!=0:
        print("Final solution is : ",end="")
        print(numerator/denominator)
        print("done")
        return numerator/denominator
    else:
        print("division by zero not allowed")

kpi2(numerator,denominator,numerator_function,denominator_function)

