'''D. Let's learn all about VARIABLES
Use Case 1:
Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)
Then print a formatted message:
Name: Arun is learning the course Python Fundamentals at the
institute Inceptez Technologies'''
s_name="Arun"
c_name="Python Fundamentals"
t_name="Inceptez Technologies"
print(s_name,"is learning the course",c_name,"at the institute",t_name)
print("=========================================================")

'''Use Case 2:
Demonstrate dynamic inference, dynamic typing using with fee by applying .18 gst  and prove strongly typing 
character also by operating it with Eighteen percent gst
fee = 45000'''
#dynamic inference
fee= 45000
print(type(fee),fee)

#dynamic typing
fee= 45000+.18
print(type(fee),fee)

'''
E. Variables Naming Conventions
Use Case 1:
Identify which variable names below are invalid for Inceptez’s student database:
1) 2student = 'Ravi' #invalid
2) _student_id = 1001 #valid
3) studentName = 'Priya' #valid
4) class name = 'Python' #invalid
5) inceptez_batch = 'Morning' #valid
'''
_student_id = 1001
print(_student_id)
studentName = 'Priya'
print(studentName)
inceptez_batch = 'Morning'
print(inceptez_batch)

'''Use Case 2:
Declare 3 variables following naming styles for Inceptez projects:

PascalCase: DataEngineeringBatch
camelCase: dataEngineeringBatch
snake_case: data_engineering_batch'''

DataEngineeringBatch="Inceptez Projects"
print(DataEngineeringBatch)
dataEngineeringBatch="Inceptez Projects"
print(dataEngineeringBatch)
data_engineering_batch="Inceptez Projects"
print(data_engineering_batch)






