salary = input ("PLease enter your start salary")
print "Your start salary = %d" %(salary)
accumulate = 0
for i in range(1,11):
    increase = salary*5.5/100
    salary = salary+(salary*5.5/100)
    accumulate += increase
    print("Salary after %d year is %.2f increase %.2f accumulate %.2f"%(i,salary,increase,accumulate))
