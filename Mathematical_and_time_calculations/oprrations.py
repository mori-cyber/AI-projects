def add(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2



def main(carry):
    operation = input("Do you want to (+,-,*,/): ")
    if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("That is an invalid operation")
    else:
        a = float(input("choose a number: "))
        b = float(input("Choose another number: "))
        c = float(input("choose a number: "))
        d = float(input("Choose another number: "))
        num1 = a/b
        if carry == None:
            num2 = c/d
        else:
            num2 = carry
        if(operation == "+"):
            answer = add(num1, num2)
        elif(operation == "-"):
            answer = sub(num1, num2)
        elif(operation == "*"):
            answer = mul(num1, num2)
        elif(operation == "/"):
            answer = div(num1, num2)
        print(answer)
        return answer

if input("would you like multiple calculations? (Y or N): ") in ("y", "Y"):
    domultiple = True
else:
    domultiple = False

carry = None
while 1:
    carry = main(carry)
    if domultiple:
        if input("would you like to carry the number (Y or N): ") in ("n", "N"):
            break
    else:
        break
