#Using LOWER INTERVALS

""" person < 2 (Baby)
    person >= 2 and < 4 (Toddler)
    person >= 4 and < 13 (Kid)
    person >= 13 and < 20 (Teenager)
    person >= 20 and < 65 (Adult)
    person >= 65 (Elder) """

age = int(input("Enter your age: "))

if age >= 65:
    msg = 'Elder'

elif age >= 20:
    msg = 'Adult'

elif age >= 13:
    msg = 'Teenager'

elif age >= 4:
    msg = 'Kid'

elif age >= 2:
    msg = 'Toddler'

else:
    msg = 'Baby'

print(msg)
