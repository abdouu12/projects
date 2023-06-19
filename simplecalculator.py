
def add(x_demand,y_demand):
   return x_demand + y_demand
def mult(x_demand,y_demand):
   return x_demand * y_demand
def subs(x_demand,y_demand):
   return x_demand - y_demand
def devis(x_demand,y_demand):
   return x_demand / y_demand
end_of_calculator = False
while end_of_calculator is False:
 redomessage = input("do you want to continue? ")

 if redomessage == "yes":
   x = int(input("what is your first number? "))
   y = int(input("what is your second number? "))
   operator = input("what operator do you want to use? ")
   if operator == "+":
     print(add(x_demand=x,y_demand=y))
     end_of_calculator = False
   elif operator == "*":
     print(mult(x_demand=x,y_demand=y))
     end_of_calculator = False
   elif operator == "-":
     print(subs(x_demand=x,y_demand=y))
     end_of_calculator = False
   elif operator == "/":
      print(devis(x_demand=x,y_demand=y))
      end_of_calculator = False
 elif redomessage == "no":
     end_of_calculator = True