def vol(R):
    if R < 0:
        return "no solution"
    else:
        volume = (4/3) * 3.14 * R**3
        return volume

radius = int(input())
result = vol(radius)
print(result) 

