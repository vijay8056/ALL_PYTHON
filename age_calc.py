from datetime import datetime

print("Enter Number: ")

x= int(input())
print("value enetered:", x)
y=0

while x>y:
    print (y)
    y=y+1

def calc_age(date_of_birth):
    birthdate = datetime.strptime(date_of_birth, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print("Your age is:", age)


if '__main__' == __name__:
    print("Enter your birthdate (YYYY-MM-DD): ")
    date_of_birth = input()
    calc_age(date_of_birth);

