import numpy as np
z=np.column_stack((x,y))
print(z)

pf1=np.polyfit(x,y,1)
pf2=np.polyfit(x,y,2)
pf3=np.polyfit(x,y,3)
pf4=np.polyfit(x,y,4)
pf5=np.polyfit(x,y,5)
pf6=np.polyfit(x,y,6)
pf7=np.polyfit(x,y,7)
pf8=np.polyfit(x,y,8)
pf9=np.polyfit(x,y,9)
pf10=np.polyfit(x,y,10)

f1=np.polyval(pf1,x)
f2=np.polyval(pf2,x)
f3=np.polyval(pf3,x)
f4=np.polyval(pf4,x)
f5=np.polyval(pf5,x)
f6=np.polyval(pf6,x)
f7=np.polyval(pf7,x)
f8=np.polyval(pf8,x)
f9=np.polyval(pf9,x)
f10=np.polyval(pf10,x)

e1=y-f1
e2=y-f2
e3=y-f3
e4=y-f4
e5=y-f5
e6=y-f6
e7=y-f7
e8=y-f8
e9=y-f9
e10=y-f10

nm1=np.linalg.norm(e1)
nm2=np.linalg.norm(e2)
nm3=np.linalg.norm(e3)
nm4=np.linalg.norm(e4)
nm5=np.linalg.norm(e5)
nm6=np.linalg.norm(e6)
nm7=np.linalg.norm(e7)
nm8=np.linalg.norm(e8)
nm9=np.linalg.norm(e9)
nm10=np.linalg.norm(e10)


norms=np.array((nm1,nm2,nm3,nm4,nm5,nm6,nm7,nm8,nm9,nm10))
lnorm=norms.min()

print('Least Norm: ',lnorm)

if lnorm==nm1:
    print(pf1)
elif lnorm==nm2:
    print(pf2)
elif lnorm==nm3:
    print(pf3)
elif lnorm==nm4:
    print(pf4)
elif lnorm==nm5:
    print(pf5)
elif lnorm==nm6:
    print(pf6)
elif lnorm==nm7:
    print(pf7)
elif lnorm==nm8:
    print(pf8)
elif lnorm==nm9:
    print(pf9)
elif lnorm==nm10:
    print(pf10)



