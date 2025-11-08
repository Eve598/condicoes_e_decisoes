num1 = float(input("digite a massa do material: "))
num2 = float(input("digite o valor do volume do material: "))

densidade = num1/num2
print("a densidade do material é", densidade)

if densidade >5:
    print("material muito denso")

elif densidade >=2:
    print("material com densidade media")

else:
    print("material com pouca densidade")