num=35
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print(num,"is Prime")
else:
    print(num,"is not Prime")         