def input_course_data():
   Courses=[]
   while True:
      number_Courses = int(input("Enter the number of courses:"))
      if number_Courses <= 0:
         print("Cannot access, please enter the number again!")
      else:
         break
   for n in range(0,number_Courses):
      print(f'Give the information of the courses {n+1}:')
      Courses_id= input("Course_ID:")
      Courses_name= input("Course_Name:")
      Courses.append({
      "ID": Courses_id,
      "Name": Courses_name,
      })
   return Courses
def input_student_data():
   Students=[]
   while True:
      number_Students = int(input("\nEnter the number of student:"))
      if number_Students <= 0:
         print("Cannot access, please enter the number again!")
      else:
         break
   for n in range(0,number_Students):
      print(f'Give the information of the student {n+1}:')
      Students_id= input("Student_ID:")
      Students_name= input("Student_Name:")
      Students_DOB= input("Student_DOB(MM/DD/YYYY):")
      Students.append({
      "ID": Students_id,
      "Name": Students_name,
      "DOB": Students_DOB,
      "Mark":{}
      })
   return Students
def input_mark_of_course(Courses,Students):
   print("Course available:")
   for idx, course in enumerate(Courses):
      print(f'{idx}. {course["Name"]} {course["ID"]}')
      while True:
         course_index= int(input("Select your course:"))
         if 0 <= course_index < len(Courses):
            selected_course = Courses[course_index]
            break
         else:
          print("Invalid course index, please select an available course.")
         continue
      course_id = selected_course["ID"]   
      print(f'Input mark (0 - 20) for the course {selected_course["Name"]} (ID: {selected_course["ID"]})')
      for student in Students:
         while True:
            mark = float(input(f'Please input mark for {student["Name"]} (ID: {student["ID"]}): '))
            if 0 <= mark <= 20:
               student["Mark"][selected_course["ID"]] = mark
               break
            else:
                print("Please input a value between 0 and 20")
def display_students(Courses, Students):
    print("Student Information:")
    for student in Students:
        print(f'{student["Name"]} (ID:{student["ID"]})')
        if student["Mark"]: 
            for course_id, mark in student["Mark"].items(): 
                course_name = next(course["Name"] for course in Courses if course["ID"] == course_id) 
                print(f' | {course_name} {course_id} {mark}')
        else:
            print("No mark available")
if __name__ == "__main__":
   while True:
      print("STUDENT MARK MANAGEMENT PORTAL")
      print("Options")
      print("1. Input Course Info")
      print("2. Input Student Info")
      print("3. Mark")
      firstchoice = input("Select your option: ")
      if firstchoice == "1":
         Courses = input_course_data()
         for course in Courses:
             print(f'ID: {course["ID"]}Name: {course["Name"]}')
      elif firstchoice == "2":
         Students = input_student_data()
         for student in Students:
             print(f'ID: {student["ID"]}Name: {student["Name"]}DOB: {student["DOB"]}')         
      elif firstchoice == "3":
            print("Marking...")
            break
      else:
            print("Please input a valid option")      
   while True:
      print("STUDENT MARK MANAGEMENT PORTAL")
      print("Options")
      print("1. Input Mark")
      print("2. Display All Student with Marks")
      print("3. Exit")

      secondchoice = input("Select your option: ")

      if secondchoice == "1":
         input_mark_of_course(Courses,Students )

      elif secondchoice == "2":
         display_students(Courses,Students )
         input("Press Enter to return to the menu...")
            
      elif secondchoice == "3":
            print("Exiting...")
            break

      else:
            print("Please input a valid option")                
          

       
    
           