hours = float(input("Enter total hours: "))
rate = float(input("Enter the rate per hour (in %): "))

if hours <= 40 and hours > 0:
    gross_pay = hours * rate
else:
    over_hours = hours - 40
    gross_pay = (over_hours * rate*1.5) + (40*rate)

print("Gross Pay is: ", gross_pay)