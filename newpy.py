
n=int(input('enter amount'))
if (n>=1000 and n<2000):
    dis=n/10
    print ('10%discount=',dis)
    am=n-dis
    print ('amount=',am)
elif (n>=2000 and n<3000):
    dis=n/20
    print('20%discount=',dis)
    am=n-dis
    print ('amount=',am)
elif (n>3000):
    dis=n/30
    print('30%discount=',dis)
    am=n-dis
    print('amount=',am)
else:
    print ('amount=',n)
 
    
