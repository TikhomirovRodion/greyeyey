R1 = int(input("R1 = "))
R2 = int(input("R2 = "))
R3 = int(input("R3 = "))
Uv = int(input("Uv = "))
I = Uv/(R1 + R2 + R3)
U1 = I * R1
U2 = I * R2
U3 = I * R3
print("U1 = ", round(U1, 2))
print("U2 = ", round(U2, 2))
print("U3 = ", round(U3, 2))
print("I = ", round(I, 2))