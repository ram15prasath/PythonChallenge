a=[1,2,3,3,4,5]
seen_lst=set()
dup_lst=[]
for i in a:
    if i in seen_lst:
        dup_lst.append(i)
    else:
        seen_lst.add(i)

print(f"Duplicate elements are {dup_lst}")        
