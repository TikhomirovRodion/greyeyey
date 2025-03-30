R1 = int(input("R1 = "))
R2 = int(input("R2 = "))
R3 = int(input("R3 = "))
Ia = int(input("Ia = "))
Rcom = 1/(1/R1 + 1/R2 + 1/R3)
Ucom = Ia*Rcom
I1 = Ucom/R1
I2 = Ucom/R2
I3 = Ucom/R3
print("Ucom = ", round(Ucom, 2))
print("I1 = ", round(I1, 2))
print("I2 = ", round(I2, 2))
print("I3 = ", round(I3, 2))