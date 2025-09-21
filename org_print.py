friuts=['apple','banana','cherry','apple','cherry']
seen_list=set()
dup=[]
for i in friuts:
    if i in seen_list:
        dup.append(i)
    else:
        seen_list.add(i)    
print(seen_list)        