students_name = input("Enter students name: ")
score = float(input("students score for cos 101: "))
if score <0 or score >100 :
      print("invalid input. score must be inputed correctly")
else :
    if score >= 70 :
          print("A")
    elif score >= 60 and score < 70 :
        grade = ("B")
    elif score >= 50 and score < 60 :
        grade = ("c")
    elif score >= 45 and score < 50 :
        grade = ("D")
    elif score >= 40 and score < 45 :
        grade = ("E")
    elif score >= 0 and score < 40 :
        grade = ("F")
    elif score < 0 or dscore > 100 :
        grade = "invalid"
        
    print()
    print("STUDENTS SCORE")
    print("==============")
    print(f" Students name : {students_name}")
    print(f" Students score : {score}")
    print(f" Students grade : {grade}")
 
