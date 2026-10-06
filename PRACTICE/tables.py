#tables from 1 to 20
for i in range(1,21):
    print("table of",i)
    for j in range(1,11):
        print(i,"x",j,"=",i*j)

#tables from 1 to 20 and multiples of 3 are skipped 
for i in range(1,21):
    if i%3==0:
        continue
    print("table of",i)
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
print()