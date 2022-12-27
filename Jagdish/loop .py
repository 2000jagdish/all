# i = 1
# while i <= 100:
#     if i%7 == 0:
#         print(i)
#     i = i+1

# num=407
# i=2
# first_divisor=-1
# while i<num:
#     prime=False
#     first_divisor=i
#     break
# print(prime)
# if not prime:
#     print(first_divisor)

#NUMBWER
#hppy number :   

# n=int(input("enter the number:- "))
# x=n
# while x>10:
#     sum =0
#     while x>0:
#         r=x%10
#         sum =sum+(r**2)
#         x=x//10
#     x=sum
#     print ("sum:",sum)
# if x==1:
#     print (n,"is a happy number ")
# else:
#     print(n,"is not a happy numbmer" )


# amstrong number:-
# var = int(input("Enter-:"))
# string = str(var)
# sum = 0
# for i in string:
#     sum = sum+int(i)**len(string)   
# if var == sum:
#     print("this is armstorng number")
# else:
#     print("this is not an armstorng number")
    
#amrstrong number:
# n=int(input("enter the number:-"))
# badali=str(n)
# sum=0
# let = 0
# while len(badali)>let:
#     sum =sum+int(badali[let])**len(badali)
#     let+=1
# if sum == n:
#     print("this is a armstrong number")
# else:
#     print ("this not a armstrong number")
    
#perfact number :-
# a=int(input("enter the number:- "))
# sum =0
# for i in range (1,a):
#     if a%i==0:
#         print(i,end="")
#         sum=sum+i
# if sum==a:
#     print (a,"this is perfact number ")
# else :
#     print (a,"this is not perfact number")
        
        
# n=1
# while n<=10:
#     n=n+1
#     print(n)
    
    
# n=int(input("enter:-"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)


# for i in range (1,11):
#     print(i)
# n=0
# while n<=10:
#     n+=1
#     print (n)
    
# for i in range(1,3): 
#     print(i)
#     for i in range(1,4):
#         print(i)
#         for i in range(1,3):
#             print(i)
#             for i in range(1,6):
#                 print(i)
#                 for i in range(1,3):
#                     print(i)
#                     for i in range(5,1,-1):
#                         print(i)
#binary to decimel
# n=(input("enter the number: "))
# a=list(n)
# a.reverse()
# sum=0
# for i in range(len(a)):
#     sum=sum+int(a[i])*2**i
# print(sum)

#Q1.
# for i in ("my blog"):
#     print (i,"?")
#q2.
# for i in range (5):
#     print (i)
#q3.
# n=int(input("enter binary number:-"))
# l=list[n]
# sum=0
# l.reverse()
# print(l)
# for i in range (len(l)):
#     sum=sum+int(l[i])*2**i
# print(sum)

# a=5
# for i in range(a):
#     for j in range (i+1):
#         print ('*',end=" ")
#     print()
    
# b=5
# for i in range (b):
#     for x in range (i,b):
#         print('*',end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range (i,n):
#         print(' ',end=" ")
#     for x in range (i+1):
#         print ('*',end=" ")
#     for j in range (i):
#         print('*',end=" ")
#     print()

# q=5
# for i in range (q):
#     for r in range(q,0,-1):
#         print('*',end=" ")
#     print()

# n=5
# for i in range (n):
#     for b in range (i,n):
#         print (" ",end =" ")
#     for c in range (i+1):
#         print ('* ',end ="")
# #     print ()

# n=5
# for i in range (n-1):
#     for j in range (i,n):
#         print ("  ",end="")
#     for c in range (i):
#         print("* ",end ="")
#     for x in range (i+1):
#         print ("* ",end ="")
#     print ()
# for i in range (n):
#     for j in range (i+1):
#         print("  ",end ="")
#     for c in range (i,n-1):
#         print ("* ",end="")
#     for d in range (i,n):
#         print ("* ",end ="")
#     print ()

# a=5
# for i in range (a):
#     for j in range (i+1):
#         print (" ",end="")
#     for x in range (i,a-1):
#         print("*",end="")
#     for z in range (i,a):
#         print ("*",end="") 
#     print ()







# for i in range(5, 0, -1):
#     for j in range(0, 6):
#         if(i == j):
#            print("*",end="")
#         else:
#          print(" ",end="")
#     for j in range(4, 0, -1):
#         if(i == j):
#            print("*",end="")
#         else:
#            print(" ",end="")
#     print()

# for i in range(0, 5):
#     for j in range(0, 5):
#         if(i == j):
#            print("*",end="")
#         else:
#            print(" ",end="")
#     for j in range(3, -1, -1):
#         if(i == j):
#            print("*",end="")
#         else:
#            print(" ",end="")
#     print()

# sanke_pattren
# k=0
# n=int(input("enter the number:-"))
# for i in range (n):
#     for j in range (1,n+1):
#         if i%2==0:
#             k+=1
#             print(k,end=" ")
#         else:
#             print(k,end=" ")
#             k-=1
#     k=k+n
#     print ()



# for i in range(2, 6):
#     count = 1
#     for j in range(5, i):
#         a = (i)
#         if(count == 1):
#             print(a, end="")
#             count = 2
#         else:
#             print("*"+a, end="")
#     print()

# for i in range(6, 1, -1):
#     count = 1
#     for j in range(1, i):
#         if(count == 1):
#             a = (i)
#             print(a, end="")
#             count = 2
#         else:
#             print("*"+a, end="")
#     print()

# print(-18/4)

# k=0
# n=int(input("enter no :-"))
# for i in range(n):
#     for j in range(1,n+1):
#      if i%2==0:
#       k+=1
#       print(k,end=" ")
#      else:
#       print(k,end=" ")
#       k-=1
#     k=k+n
#     print()
# print()

# n=1
# while n<=10:
#     print(n)
#     n+=1

# 1q
# n=int(input("enter-"))
# for i in range(1,n+1):
#     print (i,"natural numnber")
#     if i%2==0:
#         print (i,"even")
#     else:
#         print (i,"odd")
# Q2.  
# n=int(input("enter "))
# a=1
# while (n):
# que2
# n=1
# while n<=10:
#     print("squre of ",n,n*n)
#     n+=1

# n=1
# while n<=30:
#     print("series",n*10)
#     n+=1
 
# n=105
# while n>=7:
#     print("series",n)
#     n-=7

# n=10
# while n>=1:
#     print("natural number revers",n)
#     n-=1

# n=1
# while n<=10:
#     print ("natural number",n)
#     n+=1

# n=int(input("enter -"))
# i=1
# while (n>=i):
#     if i%2==0:
#       print ("even number",i)
#     i+=1
    
# n=int(input("enter-"))
# i=2
# while (i<=n):
#     print("even number",i)
#     i+=2

# n=int(input("table number-"))
# i=1
# while i<=100:
#     if i%n==0:
#      print("table",i)
#     i+=1

# n=int(input("enter number-"))
# b=int(input("enter number-"))
# i=0
# while (n<=b):
#     if n%2==0:
#         print("even number",n)
#     i+=1

#1,3,5qution
# m=int(input("enter number-"))
# k=1
# for i in range (1,m+1):
#     for x in range(1,k+1):
#         print ("*",end="")
#     k+=2
#     print()

# x=int(input("enter-"))
# for i in range (0,x):
#     for q in range(0,x-i-1):
#         print(end=" ")
#     for r in range (0,2*i+1):
#         print(r,end="")
#     print()
    
# for row in range(6):
#     for col in range (7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print ("*",end="  ")
#         else:
#             print (end="  ")
#     print()

    
#     for q in range(0,x-i-1):
#         print(end=" ")
#     for r in range (0,2*i+1):
#         print(r,end="")
#     print()
    
# for row in range(6):
#     for col in range (7):
#         if (row==0 and col%3!=0) or (row==1 







# n=int(input("enter  "))
# a=0
# b=1
# c=0
# for i in range(n):
#     for j in range (n-i-1):
#         print(" ",end="")
#     for j in range (i):
#         print (c,end=" ")
#         a=b
#         b=c
#         c=a+b
#     print()















# for row in range(23):
#     for col in range(14):
#         if(col==3 and row==1)or(row==0 and(col>3 and col<8))or(col==2 and row==2)or(col==2 and row==3)or(col==2 and row==4)or(col==8 and(0<row<11))or(row==4 and(2<col<6))or(col==5 and row==5)or(row==6 and(2<col<6))or(col==2 and row==6)or(col==3 and row==1)or(col==1 and row==6)or(col==0 and(6<row<12))or(row==11 and(4<col<8))or(col==4 and(11<row<16))or(col==1 and row==12)or(col==2 and row==13)or(col==3 and row==14)or(col==4 and row==2)or(col==9 and(5<row<12))or(row==12 and(4<col<9))or(col==5 and(12<row<22))or(row==22 and(5<col<11))or(col==10 and row==6)or(col==11 and row==7)or(col==12 and row==8)or(col==13 and(8<row<17))or(col==11 and row==21)or(col==12 and row==20)or(col==12 and row==19)or(row==19 and(7<col<13))or(row==17 and(7<col<13))or(col==8 and row==18)or(col==8 and row==21):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()













# num_rows = int(input("Enter the number of rows"));
# for i in range(0, num_rows):
# 	for j in range(0, num_rows-i-1):
# 		print(end=" ")
# 	for j in  range(0, i+1):
# 		print("*", end=" ")
# 	print()






# for row in range(27):
#     for col in range(16):
#         if  :
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()


