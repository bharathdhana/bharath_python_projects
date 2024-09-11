a = 5
b = 10

print(f"Before Swapping: a = {a}, b = {b}")

# Swap the values using a temporary variable
temp = a
a = b
b = temp

print(f"After Swapping: a = {a}, b = {b}")

#Swap the variables w/o using temp variable
c = 10
d = 2
print(f"Before Swapping: c = {c}, d = {d}")

#via Arithmetic Op
c=c+d
d=c-d
c=c-d

print(f"After Swapping: c = {c}, d = {d}")


print(f"Before Swapping: a = {a}, b = {b}")
#Tuple unpacking
a,b = b,a

print(f"After Swapping: a = {a}, b = {b}")
