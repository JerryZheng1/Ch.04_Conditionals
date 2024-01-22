# 4.0 Jedi Training (40pts)  Name:Jerry
#Below each program list the mistakes found in comments.

  #1. Make the following program work. (3 mistakes)  (3pts)
     midichlorians = float(input("Enter midichlorian count: "))#missing parenthesis to end the float()
     if midichlorians > 10000: #missing : to end statement
         print("You have serious Jedi potential")
     else: #changed elif to else to end the if statement
         print("Jedi, you will never be.")


 # 2. Make the following program work. (3 mistakes)  (3pts)
x = int(input("Enter a number: ")) #int function or else it's a string
if x == 3: #set = to == to check if x is == 3 and forgot :
    print("You entered 3")



  # 3. Make the following program work. (4 mistakes)  (4pts)

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8": #change a = to answer = Also change the single equal sign to a double one
    print("Correct!")
else: #indentation problem and it's forgetting a colon
    print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes) (4pts)
     
jedi = input("Name one of the top 3 greatest Jedi.") #change x to jedi
if jedi.lower() == "yoda" or jedi.lower() == "luke skywalker" or jedi.lower() == "obi-wan kenobi": #jedi == for each name; change the names to strings using "
    print("That is correct!") #parenthesis around "That is correct!" for it to print it



 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.lower() == "a" or user_input.lower() == "jedi master": #changes input to lower cases so it's equal to what we want it to; changes = to == to check
    sensitivity = 1000
elif user_input.lower() == "b" or user_input.lower() =="sith lord": #else if changes to elif
    sensitivity = 900
elif user_input.lower() == "c" or user_input.lower() == "droid": #else if changes to elif
    sensitivity = 0
else:
    sensitivity="" #sets sensitivity to blank text
    print("That's not a choice, try again")


print("Sensitivity: ",sensitivity) #Case sensitive so chance S -> s




'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''
print("NUMBER ANALYSIS CALCULATOR V1.0")
number_input=int(input("Please insert a number"))
if number_input%2==0:
    test1="Even"
else:
    test1="Odd"
if number_input==0:
    test2="Zero"
elif number_input>0:
    test2="Positive"
else:
    test2="Negative"
if number_input>=-100 and number_input<=100:
    test3="Inclusive"
else:
    test3="Exclusive"

print("Test 1: The number is ", test1)
print("Test 2: The number is", test2)
print("Test 3: The number is", test3)




'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print("Final Grade Calculator V2.0")
sgrade=float(input("What is your semester grade CURRENTLY?"))
fgrade=float(input("Insert final exam grade."))
fworth=float(input("How much does the final exam weigh?"))
ograde=(sgrade*(1-(fworth/100)))+((fworth/100)*(fgrade)) #(semester grade * 1-the percent of final grade worth over 100)+(percent of final worth over 100* the final grade)

if ograde>=93 and ograde<=100: #grading system
    gradevalue="A"
elif ograde>=90 and ograde<=92:
    gradevalue="A-"
elif ograde>=88 and ograde<=89:
    gradevalue="B+"
elif ograde>=83 and ograde<=87:
    gradevalue="B"
elif ograde>=80 and ograde<=82:
    gradevalue="B-"
elif ograde>=78 and ograde<=79:
    gradevalue="C+"
elif ograde>=70 and ograde<=77:
    gradevalue="C-"
elif ograde>=68 and ograde<=89:
    gradevalue="D+"
elif ograde>=63 and ograde<=67:
    gradevalue="D"
elif ograde>=60 and ograde<=62:
    gradevalue="D-"
elif ograde>=0 and ograde<=59:
    gradevalue="F"
else:
    print("Hey that's not possible, try again!")

if ograde>=60 and ograde<=100: #checks the value if between them giving 3 different messages
    print("Your overall final grade for the semester will be: " , gradevalue, "(",ograde,")")
elif ograde<=59 and ograde>=0:
    print("Transfer to Johnston because you have failed! Your grade is:", gradevalue, "(", ograde,")")
else:
    print("")
