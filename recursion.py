                             # sum of digitis


# def sum_of_digits(num1):
#     if num1==0:
#         return 0
#     rem =num1%10
#     return rem+sum_of_digits(num1//10)
# print(sum_of_digits(234567))


                          # factorial of a number

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(8))


                             # exponent using recursion

# def exponent(a,b):
#     if b==0:
#         return 1
#     return a* exponent(a,b-1)
# print(exponent(2,3))


                            # reversing a string with out using recursion

# new_str1=""
# str1="reverse a string"
# for i in str1:
#     # print(i)
#     new_str1=i+new_str1
# print(new_str1)


                               # reverse a strig using recursion
# def reverse_string(str1):
#     if len(str1)<=0:
#         return ''
#     return str1[-1]+reverse_string(str1[:-1])
# print(reverse_string("sathish"))




                           # palidrome using recursion
# def palindrome(str1):
#     if len(str1) in [0,1]:
#         return "yes..... it is plaindrome"
#     return str1[0]==str1[-1] and palindrome(str1[1:-1])
# print(palindrome("malayalam"))


                             # finding max number in list using recursion

def max_in_list(list1):
    if len(list1)==1:
        return list1[0]
    first_element=list1[0]
    rec_max = max_in_list(list1[1:])
    final_max=first_element if first_element > rec_max else rec_max
    return final_max
list1=[1,2,3,4,4,5]
print(max_in_list(list1))