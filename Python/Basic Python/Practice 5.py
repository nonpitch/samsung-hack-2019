#input
#Weight = input("Enter Your weight")
#BMI = (Weight/((Height/100.0)**2))
#print("BMI = %5.1f" %(BMI))
#if BMI < 18.5:
#    option="Underweight"
#elif BMI >= 25.0 and BMI<=29.9:
#   option="Overweight"
#elif BMI <= 30.0:
#    option="Obese"
#print "You are %s"%(option)
price = input("Enter Price:")
coupon = raw_input("Do you have coupon(yes or no):")
while(coupon != "yes" and coupon !="no"):
    coupon = raw_input("Do you have coupon again(yes or no):")
if coupon == "yes":
    discount = input("How many discount:")
    print"discount =%5.1f"%(price*(discount/100.0))
    print"Net Price =%5.1f"%(price-(price*(discount/100.0)))
elif coupon == "no":
    print"Net Price = %5.1f"%(price)










