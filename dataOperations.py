#задача 1
gramms = 13456
full_kilogramms = gramms//1000
print( "В "+str(gramms)+" граммах содержится "+str(full_kilogramms)+" полных килограмм.")

#задача 2
n1 = 1829475
last_digit = n1%10
print(last_digit)

#задача 3
n1 = 12
if n1>0 and n1%2==0:
    print("Число "+str(n1)+" является положительным и четным.")
else:
    print("Число " + str(n1) + " не подходит под условия.")

#задача 4
n1 = 99.9
if 0<n1<100:
    print("Число "+str(n1)+" находится в пределах диапазона от 0 до 100.")
else:
    print("Число " + str(n1) + " выходит за пределы диапазона от 0 до 100.")

#задача 5
n1 = 9
if n1%3!=0:
    print("Число "+str(n1)+" не кратно 3.")
else:
    print("Число " + str(n1) + " кратно 3.")