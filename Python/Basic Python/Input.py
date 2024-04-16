#input
from datetime import  datetime
currentyear = datetime.now().year
#currentyear = currentyear + 543
currentyear += 543
Name = raw_input("Please Enter Your Name")
print("Name = %s" %Name)
Birthyear = input("Enter Your Birth Year")
print("Birth Year = %d" %(Birthyear))
print("Age = %d" %(currentyear-Birthyear))

