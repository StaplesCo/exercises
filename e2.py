d1 = 1
d2 = 4
d3 = 0
d4 = 6
d5 = 3
d6 = 5
d7 = 7
d8 = 2
d9 = 8
d10 = 9

#this makes the numbers into strings, not numbers.
#Combines the strings then turns them to intergers again.

a  = int(str(d2) + str(d3)+ str(d4))
b  = int(str(d3) + str(d4)+ str(d5))
c  = int(str(d4) + str(d5)+ str(d6))
d  = int(str(d5) + str(d6)+ str(d7))
e  = int(str(d6) + str(d7)+ str(d8))
f  = int(str(d7) + str(d8)+ str(d9))
g  = int(str(d8) + str(d9)+ str(d10))



aa = (a/2)
bb = (b/3)
cc = (c/5)
dd = (d/7)
ee = (e/11)
ff = (f/13)
gg = (g/17)

print (aa + bb + cc + dd +  ee + ff + gg)
