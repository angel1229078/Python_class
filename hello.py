def student_record():
    name = input("enter student name:")
    email = input("enter student email:")
    phone_number = input("enter student phone number:")
    gender = input()
    age = input()

    student_file = {'student_name':name,
                    'student_email':email,
                    'phone_number':phone_number,        
                    'gender':gender,
                    'age':age}
    


    return student_file


    print(f'student_name is:{name}')
    print(f'student_mail is:{email}')
    print(f'student_phone_number is:{phone_number}')
    print(f'student_gender is:{gender}')
    print(f'student_age is:(age)')