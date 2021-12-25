print("enter number of different values in numerator")
numerator_length=int(input())
numerator=[]
numerator_function=[]



for x in range(0,numerator_length):
    print("Enter number "+ str(x+1) +" value in numerator")
    numerator.append(int(input("")))
    
    while x<numerator_length-1:   
        print("Enter the function add,subtract,multiply,divide")  
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
        print("Enter the function add,subtract,multiply,divide")  
        denominator_function.append(input())
        break

print(numerator)
print(denominator)    



# numerator=[1,2,3,4]  
# numerator_function=["add","divide","multiply","add"]

# denominator=[1,2,3,4]
# denominator_function=["add","divide","multiply","add"]


def calc(array,function_array):
    solution = array[0]
    x=0

    while x<len(array)-1:
        
        solution=function(int(array[x]),int(array[x+1]),function_array[x])
        array[x]=solution
        x=x+1
    
    print(solution)
    return solution


def function(solution,value,function):       
    y=function
        
    if y=="add":
        return solution+value
    
    elif y=="subtract":
        return solution/value
    
    elif y=="multiply":
        return solution/value

    elif y=="divide":
        return solution/value


def kpi2(numerator,denominator,numerator_function,denominator_function):

    print("Value of numerator is : ", end="" )
    numerator=calc(numerator,numerator_function)

    print("Value of denominator is : ", end="" )
    denominator=calc(denominator,denominator_function)

    if denominator!=0:
        print("Final solution is : ",end="")
        print(numerator/denominator)
        print("done")
        return numerator/denominator
    
    else:
        print("not divisible by 0")


kpi2(numerator,denominator,numerator_function,denominator_function)

