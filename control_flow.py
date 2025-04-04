#2. Control flow
    #if , elif , else
print("@ : if elif else")
x = 5
if x > 10 :
    print("X is greater than 10.")
elif x == 5 :
    print("x is equal to 5")
else:
    print("X is less than 10")

    #while loop
print("@ : While loop")
i = 0
while i < 5:
    print(i)
    i+=1

    #For loop
print("@ : For loop")
fruits = ["apple","mango","banana"]
for f in fruits:
    print(f)

print("@ : Use of break / continue / pass")
    #use of
    # break
    # continue
    # pass
for i in range(5):
    if i == 3:
        break
    print(i,end='')
print()

for i in range(5):
    if i == 3:
        continue
    print(i,end='')
print()
for i in range(5):
    if i == 3:
        pass
    print(i,end='')
print()
