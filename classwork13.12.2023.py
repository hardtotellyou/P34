#a = int(input("Enter a number 1: "))
#b = int(input("Enter a number 2: "))
#print(a, "+", b, "=" ,a + b)
#print(a, "-", b, "=" ,a - b)
#print(a, "*", b, "=" ,a * b)
#print(a, "/", b, "=" ,a / b)
#a = int(input("Enter a value: "))
#b = int(input("Enter a percent: "))
#print(a/b)
#a = int(input("Enter a height: "))
#b = int(input("Enter a width: "))
#print("S=",a,"*", b, "=",a * b)
h1=int(input("hours first time"))
m1=int(input("min first time"))
s1=int(input("sec first time"))
h2=int(input("hours second time"))
m2=int(input("min second time"))
s2=int(input("sec second time"))
Sum1=(h1*3600)+(m1*60)+s1
Sum2=(h2*3600)+(m2*60)+s2
globalsum=Sum2 - Sum1
global_h= globalsum//3600
global_m= (globalsum-(global_h * 3600))//60
global_s=globalsum-((global_h * 3600)+global_m* 60)
print("hours:",global_h, " minutes:",global_m, " seconds:",global_s )