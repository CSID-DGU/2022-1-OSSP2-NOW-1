myl = [1,None, 2,None, 3,None]

print(myl, len(myl))

for v in myl:
    if v == None:
        myl.remove(v)

print(myl)

print("월화수"[0:2])
print(len("   ".strip()))

myl2 = [1,2,3,4,5]

for i in range(len(myl2)):
    myl2[i] += 3

print(myl2)