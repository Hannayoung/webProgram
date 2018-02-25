Month2=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
Month1=[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]


a= input("태어난 해를 입력하세요:")
b= input("태어난 달을 입력하세요:")
c = input("태어난 일을 입력하세요:")
d= input("이번해를 입력하세요:")
e= input("이번해의 달을 입력하세요:")
f= input("날짜를 입력하세요:")

a= int(a)
b= int(b)
c= int(c)
d= int(d)
e= int(e)
f= int(f)

z= a+1
day1 = 0
day2 = 0
day3 = 0
day4 = 0


q=0
i=1
j=1
if(a+1 == d ) :
         if(a%4 == 0 and a%100== 0 and a%400 == 0) or (a%4 ==0 and a%100 != 0) :
                  day1=Month1[12]-(Month1[b-1]+c)+Month2[e-1]+f

         elif (d%4 == 0 and d%100== 0 and d%400 == 0) or (d%4 ==0 and d%100 != 0) :
                  day1=Month2[12]-(Month2[b-1]+c)+Month2[e-1]+f

         else :
                  day1=Month1[12]-(Month1[b-1]+c)+Month1[e-1]+f

         

else :
         while (q<d-(a+1)) :
                  if (z%4 == 0 and z%100== 0 and z%400 == 0) or (z%4 ==0 and z%100 != 0) :
                           day1+=366
                           q+=1
                           z+=1
                           
                  else :
                           day1+=365
                           q+=1
                           z+=1
                  
if(a+1 != d and a<d) :
         if (a%4 == 0 and a%100== 0 and a%400 == 0) or (a%4 ==0 and a%100 != 0) :
                  while(j<b+1):
                           if j == b :
                                    day2 = Month1[12] - Month1[b]+(Month1[b]-Month1[b-1]-c+1)
                                    j+=1
                           elif j != b :

                                    j+=1

                           else :
                                    print("달이 아닙니다.")
                           
         else :
                  while(j < b+1) :
                           if j == b :
                                    day2 = Month2[12] - Month2[b]+(Month2[b]-Month2[b-1]-c+1)
                                    j+=1
                           
                           elif j != b:
                                    j+=1
                           else :
                                    print("달이 아닙니다.")


         if (d%4 == 0 and d % 100== 0 and d % 400 == 0) or (d % 4 ==0 and d % 100 != 0) :
                  while(i < e+1):
                           if i == e:
                                    day3 = Month1[e-1]+f
                                    i+=1
                           elif i!= e :
                                    i+=1
                           else :
                                    print("달이 아닙니다.")
                           
         else :
                  while(i < e+1) :
                           if i == e :
                                    day3 = Month2[e-1]+f
                                    i+=1
                           elif i!= e :
                                    i+=1
                           else :
                                    print("달이 아닙니다.")
elif (a == d) :
         if (a%4 == 0 and a%100== 0 and a%400 == 0) or (a%4 ==0 and a%100 != 0) :
                  day2 = Month1[e-1]+f-(Month1[b-1]+c)+1

                 

              
                           
         else :
                  day2 = Month2[e-1]+f-(Month2[b-1]+c)+1
                         
                           
                 
                           

day4= day1+day2+day3

print(day4)
