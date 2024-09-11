#Working with Sets
set1 = {10,20,30,40,50}
set2 = {50,60,90,20,30}

print(set1)
print(set2)



set3 = set1.difference(set2)
set4 = set1.union(set2)
set5  = set1.intersection(set2)
print("Difference btw teh sets")
print(set3)
print("Everything / Union of sets")
print(set4)
print("Common / Intersection of sets")
print(set5)
print("-----------------------")
print("-----------------------")

#Working with Strings
org_str = "Cybernaut is learning platform"

print(type(org_str))

print(f"Original string :{org_str}")

underscore_str = org_str.replace(" ","_")
print(f"Stings with Underscore: {underscore_str}")

no_underscore_str = underscore_str.replace("_","")
print(f"No Underscore string: {no_underscore_str}")
