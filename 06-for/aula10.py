# i = 1
# f = 11

# for cont in range(i,f):
#     print(f"{cont}")

# for cont in range(10):
#     print(f"for 2 {cont}")
    
# for cont in range(0, 50, 2):
#     print(f"for 3 {cont}")
    
# for cont in range(50, 0, -2):
#     print(f"for 4 {cont}")

# for externo in range(9):
#     print(">", end=" ")
#     for interno in range(10):
#         print(externo, interno, sep="", end=" ")
#         print()
        

i = 12
for j in range(1, i + 1):
    print("", j, end="")
    if j % 5 == 0 or j % 3 == 0:
        print(" A", end="")
    if i % j == 0:
        print(" B", end="")
    else:
        print(" C", end="")
        