year = int(input("Introduce un año:"))

if not (year % 4 == 0):
    print ('Año Común')
elif not (year % 100 == 0):
    print ('Año Bisiesto')
elif not (year % 400 == 0):
    print ('Año Común')
if (year == 1580):
    print ('No dentro del período del calendario Gregoriano')
else:
    print ('Año Bisiesto')
