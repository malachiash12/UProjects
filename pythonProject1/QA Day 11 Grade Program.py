hworkscore = int(input("What's your homework score?\n"))
assessscore = int(input("How about your assessment score?\n"))
finalscore = int(input("And finally, what's your final exam score\n"))

def itscore(hwork, assess, final):
   answer = round((hwork + assess + final)/175*100, 2)
   if answer >= 90:
       grade = "You got an A*"
   elif answer >= 80:
       grade = "You got an A"
   elif answer >= 70:
       grade = "You got a B"
   elif answer >= 60:
       grade = "You got a C"
   elif answer >= 50:
       grade = "You got a D"
   else:
       grade = "Forget about IT mate"
   print(f"You got {answer}%")
   return grade



print (itscore(hworkscore, assessscore, finalscore))