# def even_odd(x):
#     if x%2==0:
#        return ("even")
#     else:
#         return ("odd")
# print(even_odd(2))


# def voters_eligibility(age):w
#     if age>=18:
#         return True
#     else:
#         return False
# print(voters_eligibility(2))
    

# def chec_prime(num1):
#     temp=num1
#     res=0
#     while temp>0:
#         rem=temp%10
#         res+=rem**len(str(num1))
#         temp=temp//10
#     return res==num1
# lower_bond=int(input("entre the lower bond"))
# upper_bond=int(input("enter the upper bond"))
# for i in range(lower_bond,upper_bond+1):
#     if chec_prime(i):
#         print(i)



# def maxmum_number():
#     list1=[1,2,3,4,5,6]

#     sum=sum(list1)
#     max_num=list1[0]
#     min_num=list[0]
#     for i in range(0,len(list1)):
    
#         if list1[i] > max_num:
#             max_num=list1[i]
#     print (maxmum_number(max_num))
#     # print(sum)


# def result(list_pass):
#     if len(list_pass)==0:
#         return
#     max = list_pass[0]
#     min=list_pass[0]
#     sum=0
#     for i in list_pass:
#         max=i if i>max else max
#         min = i if i<min else min
#         sum+=i
#     return max,min,sum
# list[1,2,3,4,5,6,7]
# tup1=result(list)
# if tup1:
#     print(max,tup1[0])
#     print(min,tup1[1])
#     print(sum,tup1[2])
# else:
#     print("not possible empty list")



