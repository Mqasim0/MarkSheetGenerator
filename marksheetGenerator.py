

print("Mark sheet Generator")
message = int(input("Enter your class in integer number, Only 9 or 10 : "))
name = input("Enter your name : ")
if(message == 9):
    group = input("Enter your group : ")
    if(group == "computer science"):
     english = int(input("Enter your English marks : "))
     pkStudies = int(input("Enter your pakistan studies marks : "))
     chemistry = int(input("Enter your chemistry marks : "))
     sindhi = int(input("Enter your sindhi marks : "))
     computerScience = int(input("Enter your computer science marks : "))

     total_marks = 500
     total_sum_of_marks = english + pkStudies + chemistry + sindhi + computerScience

     percentage = (total_sum_of_marks / total_marks)  * 100
     print("------------------------------------- Marksheet ----------------------------------")
     print("Name :", name)
     print("class :", message) 
     print("Group : ", group)
     print("-----------------------------------------------------------------------------------")
     print("|           Subjects        |   TotalMarks        |           Marks               |" )
     print("-----------------------------------------------------------------------------------")
     print("|           English         |     100             |          ", english,"                  |" )
     print("|           pkstudies       |     100             |          ", pkStudies,"                  |" )
     print("|           Chemistry       |     100             |          ", chemistry,"                  |" )
     print("|           Sindhi          |     100             |          ", sindhi,"                  |" )
     print("|          Computer Science |     100             |          ", computerScience,"                  |" )
     print("                                  500             |          ", total_sum_of_marks,"                 |"      )
     print("-----------------------------------------------------------------------------------")

     print("Percentage :: ", percentage ," %")
     
    elif(group == "biology"):
     english = int(input("Enter your English marks : "))
     pkStudies = int(input("Enter your pakistan studies marks : "))
     chemistry = int(input("Enter your chemistry marks : "))
     sindhi = int(input("Enter your sindhi marks : "))
     biology = int(input("Enter your biology marks : "))
     total_marks = 500
     total_sum_of_marks = english + pkStudies + chemistry + sindhi + biology

     percentage = (total_sum_of_marks / total_marks)  * 100
     print("------------------------------------- Marksheet ----------------------------------")
     print("Name :", name)
     print("class :", message) 
     print("Group : ", group)
     print("-----------------------------------------------------------------------------------")
     print("|           Subjects        |   TotalMarks        |           Marks               |" )
     print("-----------------------------------------------------------------------------------")
     print("|           English         |     100             |          ", english,"                  |" )
     print("|           pkstudies       |     100             |          ", pkStudies,"                  |" )
     print("|           Chemistry       |     100             |          ", chemistry,"                  |" )
     print("|           Sindhi          |     100             |          ", sindhi,"                  |" )
     print("|           Biology         |     100             |          ", biology,"                  |" )
     print("                                  500             |          ", total_sum_of_marks,"                 |"      )
     print("-----------------------------------------------------------------------------------")

     print("Percentage :: ", percentage ," %")



elif(message == 10):
     group = input("Enter your group : ")
     if(group == "computer science" or group == "biology"):
      english = int(input("Enter your English marks : "))
      urdu = int(input("Enter your urdu marks : "))
      islamait = int(input("Enter your islamait marks : "))
      physics = int(input("Enter your physics marks : "))
      math = int(input("Enter your mathametics marks : "))

      total_marks = 500
      total_sum_of_marks = english + urdu + islamait + physics + math

      percentage = (total_sum_of_marks / total_marks)  * 100
      print("------------------------------------- Marksheet ----------------------------------")
      print("Name :", name)
      print("class :", message) 
      print("Group : ", group)
      print("-----------------------------------------------------------------------------------")
      print("|           Subjects        |   TotalMarks        |           Marks               |" )
      print("-----------------------------------------------------------------------------------")
      print("|           English         |     100             |          ", english,"                  |" )
      print("|           Urdu            |     100             |          ", urdu,"                  |" )
      print("|           Islamait        |     100             |          ", islamait,"                  |" )
      print("|           Physics         |     100             |          ", physics,"                  |" )
      print("|           Math            |     100             |          ", math,"                  |" )
      print("                                  500             |          ", total_sum_of_marks,"                 |"      )
      print("-----------------------------------------------------------------------------------")

      print("Percentage :: ", percentage ," %")
      

      

