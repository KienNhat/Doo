x=0
n = int(input('n='))
for i in range (1,n+1):
    if n % i == 0: x+=i
if (x-n)//n==1: print ('Đó là số hoàn hảo')   
else: print ('Đó không là số hoàn hảo')

#####################3
a=0
n = int (input('N='))
for i in range(1,n+1):
    if n%i==0:
        a+=i
if a-n==n:
    print ('Đó là số hoàn hảo')
else: print ('Đó không là số hoàn hảo')        