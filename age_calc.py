from datetime import datetime

def list_numbers(n):
    for i in range(n):
        print(i)


def calc_age(date_of_birth):
    birthdate = datetime.strptime(date_of_birth, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    print("Your age is:", age)


if '__main__' == __name__:
    print("Enter a number: ")
    n = int(input())
    list_numbers(n)

    print("Enter your birthdate (YYYY-MM-DD): ")
    date_of_birth = input()
    calc_age(date_of_birth)

