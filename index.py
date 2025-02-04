# num1 = float(input("enter the frist number:"))

# if num1 > 0:
#     print("number is postive")
# elif num1 == 0:
#     print("enter number zero")
# else :
#     print("entre number is negitive")



# num1=int(input("enter a number:"))
# if num1 %2 == 0:
#     print("even number")
# else:
#     print("odd number")



# age=int(input("enter your age:"))
# if age >= 18:
#     print("you are eligible fot voting")
# else:
#     print("not eligiable for voting")



# marks=float(input("enter your marks:"))
# if marks > 40:
#     print("PASS")
# else:
#     print("FAIL")



# num1=float(input("enter a number from 0 to 6:"))
# if num1 == 0:
#     print("sunday")
# elif num1 == 1:
#     print("monday")
# elif num1 == 2:
#     print("tuesday")
# elif num1 == 3:
#     print("wednessday")
# elif num1 == 4:
#     print("thursday")
# elif num1 == 5:
#     print("friday")
# elif num1 == 6:
#     print("saturday")
# else:
#     print("enter the correct number")








# num1 = float(input("enter frist number:"))
# num2 = float(input("enter second number:"))
# num3 = float(input("enter third number:"))
# if num1>num2 and num1>num3:
#     greatest=num1
# elif num2>num3 and num2>num1:
#     greatest=num2
# else :
#     greatest=num3
# print("the gretest number is:",greatest)



# marks=float(input("enter the marks:"))
# if marks >= 90 and marks <= 100:
#     print("A grade")
# elif marks >= 80 and marks < 90:
#     print("B grade")
# elif marks >= 70 and marks < 80:  
#     print("C grade")
# else:
#     print("fail")



# year=int(input("enter the year:"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("is a leap uear")
# else:
#     print("is not a leap year")




# using terinary operators

# year='is a leap year' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'not aleap yeear'
# print(year)




# side1=float(input("side1:"))
# side2=float(input("side2:"))
# side3=float(input("side3:"))
# print("traingle is possible" if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2) else "it is not possible")






# by using string to find vowels, consonants,neither

# str1=input("enter a single character:").lower()
# if len(str1)>1 or len(str1)==0:
#     print("i cant run the code")
# else:
#     if str1 in "aeiou":
#         print("vowels")
#     elif str1.isalpha():
#         print("consonants")
#     else:
#         print("neither")





# by using list

# str2=input("enter a single character:").lower()
# if str2 in['a','e','i','o','u']:
#     print("vowels")
# else:
#     print("consonants")
 




# warrior1=int(input("entre warrior1 attack power:"))
# warrior2=int(input("entre warrior2 attack power:"))
# warrior1_health=int(input("enter health1:"))
# warrior2_health=int(input("enter health2:"))
# if warrior1>warrior2:
#     print("warrior1 wins")
# elif warrior2>warrior1:
#     print("warrior 2 is win")
# elif warrior1==warrior2:
#     if warrior1_health>warrior2_health:
#         print("warrior 1 wins")
#     elif warrior2_health>warrior1_health:
#         print("warrior 2 wins")
#     elif warrior1_health==warrior2_health:
#         print("draw")
# else:
#     print("nothing")



# current_balnce=int(input("entre the currentamount:"))
# withdrwa_blance=int(input("enter with draw amount:"))
# if withdrwa_blance%100==0 and withdrwa_blance<=current_balnce:
#     print("transaction succesfully")
# else:
#     print("transaction fail")









