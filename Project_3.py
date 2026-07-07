print("=====WELCOME TO THE STUDENT DATA ORGANIZER=====")

while True:

    Students = []
    subjects = set()

    print("\nPlease select an option:  ")
    print("1. Add new students:  ")
    print("2. Display All students:  ")
    print("3. Update Student Information:")
    print("4. Delete student Information:  ")
    print("5. Display Subjects offered:  ")
    print("6. Exit:  ")

#Function
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add new students
        student_id = input("Enter the Id: ")
        student_name = input("Enter your name: ")
        student_age = input("Enter your age: ")
        student_date_of_birth = input("Enter your Date of Birth")
        student_grade = input("Enter your grade: ")
        student_subjects = input("Enter your subjects (comma seperated): ")

        subjects = set(student_subjects.split(","))


        Students2 = {
            "id": student_id,
            "name": student_name,
            "age":  student_age,
            "grade": student_grade,
            "subjects": student_subjects,
            "info":(student_id,student_date_of_birth)
        }
        Students.append(Students2)
        print("Student Added Sucessfully  ! ")


    elif choice == "2":
        if len(Students) == 0:
            print("NO Records Found")
        else:
            for student2 in Students:
                print("===================")


                print (f"id: {student2['id']}")
                print (f"name: {student2['name']}")
                print (f"age: {student2['age']}")
                print (f"grade: {student2['grade']}")
                print (f"subjects:",",",", {student2['subjects']}")
                print (f"Date_of_Birth: {student2['info'][1]}")

    elif choice == "3":
        student_id = int(input("Enter ID to update"))

        for i in Students:
            if i["id"]== student_id:
                i["name"]==student_name= input("Enter New Name")
                i["age"]==student_age= input("Enter New Age")
                i["grade"]==student_grade= input("Enter New Grade")
                print("the updated record")

    elif choice =="4":
        student_id = int(input("Enter ID to delete :"))
        for i in range(len(Students)):
            if Students [i] ["id"]==student_id:
                del Students[i]
                print("Record Deleted")
    
    elif choice =="5":
        all_subjects =set()

        for s in Students:
            all_subject=all_subject.union(s["subjects"])
            print("subject offers")
            for a in all_subjects:
                print(a)

    elif choice ==6:
        print("THANK YOU! ")
        break
    else:
        print("Invalid Choice")
            


                




                



