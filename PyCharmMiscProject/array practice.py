import array as ar
arr =ar.array ('i',[1,2,3,4,5,6,7])
a =1
for i in arr:
    if i == a:
        print("true")
        break
    else:
        print("false")
