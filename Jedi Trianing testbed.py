# # # midichlorians = float(input("Enter midichlorian count:" ))
# # # if midichlorians > 10000:
# # #     print("You have serious Jedi potential")
# # #
# # # else: #changed elif to else to end the if statement
# # #     print("Jedi, you will never be.")
# #
# #
# # # x = int(input("Enter a number"))
# # # if x == 3:
# # #     print("You entered 3")
# # #
# # # answer = input("What is the name of Poe Dameron's Droid? ")
# # # if answer == "BB8": #answer = rather than =. change = to ==
# # #     print("Correct!")
# # # else: #else is missing :
# # #     print("Incorrect! It is BB8.")
# #
# # # jedi = input("Name one of the top 3 greatest Jedi.")
# # # if jedi.lower() == "yoda" or jedi.lower() == "luke skywalker" or jedi.lower() == "obi-wan kenobi": #jedi ==
# # #     print("That is correct!")
# # # jedi = input("Name one of the top 3 greatest Jedi.") #change x to jedi
# # # if jedi.lower() == "yoda" or jedi.lower() == "luke skywalker" or jedi.lower() == "obi-wan kenobi": #jedi == for each name; change the names to strings using "
# # #     print("That is correct!") #parenthesis around "That is correct!" for it to print it
# #
# # # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
# # #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
# #
# # # print("Welcome to the Jedi Academy!")
# # #
# # # print("A. Jedi Master")
# # # print("B. Sith Lord")
# # # print("C. Droid")
# # #
# # # user_input = input("Choose a character?")
# # #
# # # if user_input.lower() == "a" or user_input.lower()=="jedi master":
# # #     sensitivity = 1000
# # # elif user_input.lower() == "b" or user_input.lower()=="sith lord":
# # #     sensitivity = 900
# # # elif user_input.lower == "c" or user_input.lower()=="droid":
# # #     sensitivity = 0
# # # else:
# # #     sensitivity=""
# # #
# # #
# # #
# # # print("Sensitivity: ", sensitivity)
# #
# # # print("Welcome to the Jedi Academy!")
# # #
# # # print("A. Jedi Master")
# # # print("B. Sith Lord")
# # # print("C. Droid")
# # #
# # # user_input = input("Choose a character?")
# # #
# # # if user_input.lower() == "a" or user_input.lower() == "jedi master":  # changes input to lower cases so it's equal to what we want it to; changes = to == to check
# # #     sensitivity = 1000
# # # elif user_input.lower() == "b" or user_input.lower() == "sith lord":  # else if changes to elif
# # #     sensitivity = 900
# # # elif user_input.lower() == "c" or user_input.lower() == "droid":  # else if changes to elif
# # #     sensitivity = 0
# # # else:
# # #     sensitivity = ""
# # #
# # # print("Sensitivity: ", sensitivity)
# #
# # # print("Welcome to the Jedi Academy!")
# # #
# # # print("A. Jedi Master")
# # # print("B. Sith Lord")
# # # print("C. Droid")
# # #
# # # user_input = input("Choose a character?")
# # #
# # # if user_input.lower() == "a" or user_input.lower()=="jedi master": #changes input to lower cases so it's equal to what we want it to; changes = to == to check
# # #     sensitivity = 1000
# # # elif user_input.lower() == "b" or user_input.lower()=="sith lord": #else if changes to elif
# # #     sensitivity = 900
# # # elif user_input.lower() == "c" or user_input.lower()=="droid": #else if changes to elif
# # #     sensitivity = 0
# # # else:
# # #     sensitivity = ""
# # #     print("thats not a choice try again")
# # #
# # # print("Sensitivity: ",sensitivity)
# #
# # # print("Welcome to the Jedi Academy!")
# # #
# # # print("A. Jedi Master")
# # # print("B. Sith Lord")
# # # print("C. Droid")
# # #
# # # user_input = input("Choose a character?")
# # #
# # # if user_input.lower() == "a" or user_input.lower() == "jedi master": #changes input to lower cases so it's equal to what we want it to; changes = to == to check
# # #     sensitivity = 1000
# # # elif user_input.lower() == "b" or user_input.lower() == "sith lord": #else if changes to elif
# # #     sensitivity = 900
# # # elif user_input.lower() == "c" or user_input.lower() == "droid": #else if changes to elif
# # #     sensitivity = 0
# # # else:
# # #     sensitivity=""
# # #     print("Thats not a choice, try again")
# # #
# # #
# # # print("Sensitivity: ",sensitivity)
# # #
# # # print("NUMBER ANALYSIS CALCULATOR V1.0")
# # # number_input=int(input("Please insert a number"))
# # # if number_input%2==0:
# # #     test1="Even"
# # # else:
# # #     test1="Odd"
# # # if number_input==0:
# # #     test2="Zero"
# # # elif number_input>0:
# # #     test2="Positive"
# # # else:
# # #     test2="Negative"
# # # if number_input>-100 and number_input<100:
# # #     test3="Inclusive"
# # # else:
# # #     test3="Exclusive"
# # #
# # # print("Test 1: The number is ", test1)
# # # print("Test 2: The number is", test2)
# # # print("Test 3: The number is", test3)
# #
# # # print("Final Grade Calculator V1.0")
# # # sgrade=float(input("What is your semester grade CURRENTLY?"))
# # # fgrade=float(input("Insert final exam grade."))
# # # fworth=float(input("How much does the final exam weigh?"))
# # # ograde=(sgrade*(1-(fworth/100)))+((fworth/100)*(fgrade)) #(semester grade * 1-the percent of final grade worth over 100)+(percent of final worth over 100* the final grade)
# # #
# # # if ograde>=93:
# # #     gradevalue="A"
# # # elif ograde>=90 and ograde<=92:
# # #     gradevalue="A-"
# # # elif ograde>=88 and ograde<=89:
# # #     gradevalue="B+"
# # # elif ograde>=83 and ograde<=87:
# # #     gradevalue="B"
# # # elif ograde>=80 and ograde<=82:
# # #     gradevalue="B-"
# # # elif ograde>=78 and ograde<=79:
# # #     gradevalue="C+"
# # # elif ograde>=70 and ograde<=77:
# # #     gradevalue="C-"
# # # elif ograde>=68 and ograde<=89:
# # #     gradevalue="D+"
# # # elif ograde>=63 and ograde<=67:
# # #     gradevalue="D"
# # # elif ograde>=60 and ograde<=62:
# # #     gradevalue="D-"
# # # else:
# # #     gradevalue="F"
# # #
# # # if ograde>=60 and ograde<=100:
# # #     print("Your overall final grade for the semester will be: " , gradevalue, "(",ograde,")")
# # # else:
# # #     print("Transfer to Johnston because you have failed! Your grade is:", gradevalue, "(", ograde,")")
# #
# # # print("Final Grade Calculator V2.0")
# # # sgrade=float(input("What is your semester grade CURRENTLY?"))
# # # fgrade=float(input("Insert final exam grade."))
# # # fworth=float(input("How much does the final exam weigh?"))
# # # ograde=(sgrade*(1-(fworth/100)))+((fworth/100)*(fgrade)) #(semester grade * 1-the percent of final grade worth over 100)+(percent of final worth over 100* the final grade)
# # #
# # # if ograde>=93 and ograde<=100: #grading system
# # #     gradevalue="A"
# # # elif ograde>=90 and ograde<=92:
# # #     gradevalue="A-"
# # # elif ograde>=88 and ograde<=89:
# # #     gradevalue="B+"
# # # elif ograde>=83 and ograde<=87:
# # #     gradevalue="B"
# # # elif ograde>=80 and ograde<=82:
# # #     gradevalue="B-"
# # # elif ograde>=78 and ograde<=79:
# # #     gradevalue="C+"
# # # elif ograde>=70 and ograde<=77:
# # #     gradevalue="C-"
# # # elif ograde>=68 and ograde<=89:
# # #     gradevalue="D+"
# # # elif ograde>=63 and ograde<=67:
# # #     gradevalue="D"
# # # elif ograde>=60 and ograde<=62:
# # #     gradevalue="D-"
# # # elif ograde>=0 and ograde<=59:
# # #     gradevalue="F"
# # # else:
# # #     print("Hey that's not possible, try again!")
# # #
# # # if ograde>=60 and ograde<=100: #checks the value if between them giving 3 different messages
# # #     print("Your overall final grade for the semester will be: " , gradevalue, "(",ograde,")")
# # # elif ograde<=59 and ograde>=0:
# # #     print("Transfer to Johnston because you have failed! Your grade is:", gradevalue, "(", ograde,")")
# # # else:
# # #     print("")
# # # print("Welcome to the Jedi Academy!")
# # #
# # # print("A. Jedi Master")
# # # print("B. Sith Lord")
# # # print("C. Droid")
# # #
# # # user_input = input("Choose a character?")
# # #
# # # if user_input.lower() == "a" or user_input.lower() == "jedi master": #changes input to lower cases so it's equal to what we want it to; changes = to == to check
# # #     sensitivity = 1000
# # # elif user_input.lower() == "b" or user_input.lower() =="sith lord": #else if changes to elif
# # #     sensitivity = 900
# # # elif user_input.lower() == "c" or user_input.lower() == "droid": #else if changes to elif
# # #     sensitivity = 0
# # # else:
# # #     sensitivity="" #sets sensitivity to blank text
# # #     print("That's not a choice, try again")
# # #
# # #
# # # print("Sensitivity: ",sensitivity)
# # # print("NUMBER ANALYSIS CALCULATOR V1.0")
# # # number_input=int(input("Please insert a number"))
# # # if number_input%2==0:
# # #     test1="Even"
# # # else:
# # #     test1="Odd"
# # # if number_input==0:
# # #     test2="Zero"
# # # elif number_input>0:
# # #     test2="Positive"
# # # else:
# # #     test2="Negative"
# # # if number_input>-100 and number_input<100:
# # #     test3="Inclusive"
# # # else:
# # #     test3="Exclusive"
# # #
# # # print("Test 1: The number is ", test1)
# # # print("Test 2: The number is", test2)
# # # print("Test 3: The number is", test3)
# # print("NUMBER ANALYSIS CALCULATOR V1.0")
# # number_input=int(input("Please insert a number"))
# # if number_input%2==0:
# #     test1="Even"
# # else:
# #     test1="Odd"
# # if number_input==0:
# #     test2="Zero"
# # elif number_input>0:
# #     test2="Positive"
# # else:
# #     test2="Negative"
# # if number_input>=-100 and number_input<=100:
# #     test3="Inclusive"
# # else:
# #     test3="Exclusive"
# #
# # print("Test 1: The number is ", test1)
# # print("Test 2: The number is", test2)
# # # print("Test 3: The number is", test3)
# #
# # print("This program takes three integers and returns the sum.")
# # total = 0
# # for i in range(3):
# #     x = int(input("Enter a number: "))
# #     total += x
# # print("The total is:", total)
# for i in range(2,102,2):
# #     print(i)
# i=10
# while i>-1:
#     print(i)
#     i-=1
# print("Blast off!")
# import random
# my_number=random.randint(1,10)
# print(my_number)
#
# total=0
# positive=0
# negative=0
# zero=0
# for i in range(7):
#     input_number=float(input("Enter a number"))
#     total+=input_number
#     if input_number>0:
#         positive+=1
#     elif input_number==0:
#         zero+=1
#     else:
#         negative+=1
#
# print("you sum is:",total)
# print("You entered a total of",positive,"positive numbers")
# print("You entered a total of",negative,"negative numbers")
# print("You entered a total of",zero,"zeros")
#
# import random
# heads=0
# tails=0
# for i in range(50):
#     number=random.randint(0,1)
#     if number==1:
#         print("heads")
#         heads+=1
#     else:
#         print("tails")
#         tails+=1
# print("")
# print("TOTAL:")
# print("You got",heads,"heads")
# print("You got",tails,"tails")
import random
done = False
user_input=0
computer_input=0
computer_score=0
user_score=0
tied_score=0

print("ROSHAMBO PROGRAM V1.0")
while not done:
    print("")
    user_input=int(input("Choose an option, 1 for rock, 2 for paper, 3 for scissors and 4 to quit."))
    print("")
    if user_input==4:
        done = True
    elif user_input==1 or user_input==2 or user_input==3:
        if user_input==1:
            print("You chose Rock")
        elif user_input == 2:
            print("You chose Paper")
        else:
            print("You chose Scissors")
        computer_input=random.randint(1,3)
        if computer_input==1:
            print("Computer chooses Rock")
        elif computer_input==2:
            print("Computer chooses paper")
        else:
            print("Computer chooses scissors")
        if computer_input==user_input:
            print("It's a tie!")
            tied_score+=1
        elif user_input==1 and computer_input==2:
            print("The Computer won! Paper > Rock")
            computer_score+=1
        elif user_input == 1 and computer_input == 3:
            print("You won! Rock > Scissors")
            user_score+=1
        elif user_input == 2 and computer_input == 3:
            print("The Computer won! Scissors > Paper")
            computer_score += 1
        elif user_input == 2 and computer_input == 1:
            print("You won! Paper > Rock")
            user_score+=1
        elif user_input == 3 and computer_input == 1:
            print("The Computer won! Rock > Scissors")
            computer_score += 1
        elif user_input == 3 and computer_input == 2:
            print("You won! Scissors > Paper")
            user_score += 1
        else:
            print("Hey that's not an option!")
    else:
        print("Hey that's not an option!")
print("")
print("YOUR FINAL SCORE")
print("WINS:",user_score)
print("LOSES:",computer_score)
print("TIES:",tied_score)


