'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
correct=0
questions_answered=0
questions_left=10

print("\033[1;31;40m WELCOME TO THE JEDI BOWL, PASS THIS QUIZ OR ELSE.... ")
print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 1:")
print("\033[2;35;40m What happens to the Urbie in U-Hub?")
print("\033[2;36;40m A. It changes color\n B. The Urbie grows bigger \n C. The Urbie shrinks\n D. Nothing\n E. Whats an Urbie?") #questions
answer=(input("\033[2;36;40m Enter Answer (A,B,C,D or E)")) #answering input

if answer.lower()=="a": #correct input
    print("\033[2;32;40m Correct! A: It changes color")
    correct+=1
    questions_answered+=1
    questions_left-=1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else: #incorrect input
    print("\033[2;31;40m Incorrect! The correct answer is A: It changes color" )
    correct+=0
    questions_answered+=1
    questions_left-=1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 2:")
print("\033[2;35;40m Consider this scenario: Mr.Hermon's car can go 120mph and every day he drives 60 miles to get to Menards.\n How long does it take for Mr.Hermon to get to Menards considering there is no traffic and he drives at a constant speed?\n Leave your answer without the units")
print("\033[2:31;40m")
print("\033[2:35;40m Mr. Hermon takes ___ minutes to get to Menards")
answer=float(input("\033[2:31;40m"))

if answer==30:
    print("\033[2;32;40m Correct! It will take Mr.Hermon 30 minutes to get to Menards")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is 30")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")


print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 3:")
print("\033[2;35;40m What is Mr.Hermon's first name?")
print("\033[2:31;40m")
answer=input("")
if answer.lower()=="marc":
    print("\033[2;32;40m Correct! Mr. Hermon's first name is Marc!")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is Marc.")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 4:")
print("\033[2;35;40m How long has Mr. Hermon been teaching at UHS?")
print("\033[2:31;40m")
print("\033[2;36;40m A.16 yrs\n B.22 yrs\n C.23 yrs\n D.24 yrs\n E.25 yrs")
answer=(input("\033[2;36;40m Enter Answer (A,B,C,D or E)"))

if answer.lower()=="d":
    print("\033[2;32;40m Correct! D.24 yrs, Mr.Hermon has been at UHS since 1999!")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is D:24 yrs, Mr. Hermon has been at UHS since 1999!")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 5:")
print("\033[2;35;40m How many youtube subscribers does Mr.Hermon have?")
print("\033[2:31;40m")
print("\033[2;36;40m A.0\n B.1000\n C.1350\n D.1500\n E.1750")
answer=(input("\033[2;36;40m Enter Answer (A,B,C,D or E)"))
if answer.lower()=="c":
    print("\033[2;32;40m Correct! Mr. Hermon's channel has 1350 subscribers, make sure to subscribe to the channel!")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is C: 1350, Mr. Hermon's channel has 1350 subscribers! Make sure to subscribe to the channel!")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 6:")
print("\033[2;35;40m If x= 6/2*(1+2), what does x equal to?")
print("\033[2:31;40m")
print("\033[2:35;40m x=___")
answer=float(input("\033[2:31;40m"))
if answer==9:
    print("\033[2;32;40m Correct! x is equal to 9")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is 9!")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 7:")
print("\033[2;35;40m Which option below is the closest time from midnight?")
print("\033[2:31;40m")
print("\033[2;36;40m A.11:55 a.m.\n B.12:03 a.m.\n C.12:06 p.m.\n D.11:30 a.m. \n E.11:00 p.m.")
answer=(input("\033[2;36;40m Enter Answer (A,B,C,D or E)"))
if answer.lower()=="b":
    print("\033[2;32;40m Correct! B. 12:03 a.m. is the closest time to midnight!")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is B. 12:03 a.m.")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 8:")
print("\033[2;35;40m What is this quiz called?")
print("\033[2:31;40m")
answer=input("")
if answer.lower()=="jedi bowl" or answer.lower()=="the jedi bowl":
    print("\033[2;32;40m Correct! The quiz name is Jedi Bowl!")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is Jedi Bowl.")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"questions remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")

print("\033[2;34;40m Question 9:")
print("\033[2;35;40m Which choice below is NOT a unit in Physics?")
print("\033[2:31;40m")
print("\033[2;36;40m A.Tesla\n B.Ampere\n C.Hermonz\n D.Candela\n E.Farad")
answer=(input("\033[2;36;40m Enter Answer (A,B,C,D or E)"))
if answer.lower()=="c":
    print("\033[2;32;40m Correct! C: Hermonz is not a unit in Physics. ")
    correct += 1
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"question remaining.")
else:
    print("\033[2;31;40m Incorrect! The correct answer is C: Hermonz, Hermonz is not a unit in Physics.")
    correct += 0
    questions_answered += 1
    questions_left -= 1
    print("\033[2;36;40m Your current score is:",correct,"/",questions_answered,"(",(correct/questions_answered)*100,"% )","\033[2;36;40m There is",questions_left,"question remaining.")

print("\033[1;31;40m")
print("\033[1;31;40m")
print("\033[2;34;40m Question 10:")
print("\033[2;35;40m What room are we in?")
print("\033[2:35;40m Room ___")
answer=float(input("\033[2:31;40m"))

if answer==614:
    print("\033[2;32;40m Correct! We are in room 614!")
    correct += 1
    questions_answered += 1
    percentage = ((correct / 10) * 100)
    if percentage == 100:
        gradevalue = "A+"
        message = "Great work! You crushed it!"
    elif percentage == 90:
        gradevalue = "A"
        message = "Good job!"
    elif percentage == 80:
        gradevalue = "B"
        message= "Nice job!"
    elif percentage == 70:
        gradevalue = "C"
        message = "Average!"
    elif percentage == 60:
        gradevalue = "D"
        message = "Ok... the score can be improved. Lets try harder next time."
    else:
        gradevalue="F"
        message = "Lets forget this quiz...."
    print("\033[2;36;40m",message,)
    print("\033[2;36;40m Your final score is:",gradevalue,"(",(correct/questions_answered)*100,"% )")
    print("\033[2;36;40m Thank you for playing my quiz game!")
else:
    print("\033[2;31;40m Incorrect! The correct answer is 614!")
    correct += 0
    questions_answered += 1
    percentage = ((correct / 10) * 100)
    if percentage == 100:
        gradevalue = "A+"
        message = "Great work!"
    elif percentage == 90:
        gradevalue = "A"
        message = "Good job!"
    elif percentage == 80:
        gradevalue = "B"
        message= "Nice job!"
    elif percentage == 70:
        gradevalue = "C"
        message = "Average!"
    elif percentage == 60:
        gradevalue = "D"
        message = "Ok... the score can be improved. Lets try harder next time."
    else:
        gradevalue="F"
        message = "Lets forget this quiz...."
    print("\033[2;36;40m",message,)
    print("\033[2;36;40m Your final score is:",gradevalue,"(",(correct/questions_answered)*100,"% )")
    print("\033[2;36;40m Thank you for playing my quiz game!")