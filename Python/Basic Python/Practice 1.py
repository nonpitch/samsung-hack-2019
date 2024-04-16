#input
Weight = input("Enter Your weight")
Height = input("Enter Your height")
BMI = (Weight/((Height/100.0)**2))
print("BMI = %5.1f" %(BMI))
if BMI < 18.5:
    option="Uderweight"
elif BMI >= 18.5 and BMI<=24.9:
    option="Normal"
elif BMI >= 25.0 and BMI<=29.9:
    option="Overweight"
elif BMI <= 30.0:
    option="Obese"
print "You are %s"%(option)
