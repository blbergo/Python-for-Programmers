from math import sqrt

x = float(input("Enter a number for x:\n"))
y = float(input("Enter a number for y:\n"))
z = float(input("Enter a number for z:\n"))

print(f'X^Z: {pow(x, z):.2f}'  )
print(f'X^(Y^Z)): {pow(x, pow(y, z)):.2f}')
print(f'|X-Y|: {abs(x - y):.2f}')
print(f'Sqrt(X^Z): {sqrt(pow(x, z)):.2f}')
