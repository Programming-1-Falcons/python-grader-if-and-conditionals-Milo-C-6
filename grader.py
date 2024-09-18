maxP = float(input("How many total points can you get?: "))
Points = float(input("How many points did the student get?: "))

percentage = Points/maxP*100

print("They got a %"+str(percentage)+", Which is a") #had to use + and str to not add a space between the variable adn rest of text, probably a better way to do it, but we were never taught it...
if (percentage<51): print("F")
elif (percentage<61): print("D")
elif (percentage<76): print("C")
elif (percentage<89): print("B")
else: print("A")