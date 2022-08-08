def title(func):
    def wrapper(*args, **kwargs):
        print("CEO Red Bull Inc. Mr. John Bigbull")
        return func(*args, **kwargs)
    return wrapper


def vacation_validation():
    if vacation_type == "vacation" or vacation_type == "sick leave" or vacation_type == "day off":
        return validation_user_data()
    else:
        print("You entered type of vacation incorrectly")


def validation_user_data():
    name = input("Enter your Name (example: Johny): ")
    if name.isnumeric() or len(name) < 1:
        print("You entered wrong data (example: Johny)")
    else:
        surname = input("Enter your Surname (example: Depp): ")
        if surname.isnumeric() or len(surname) < 1:
            print("You entered wrong data (example: Depp)")
        else:
            date_from = input("Enter start vacation date (example: 10.03): ")
            date_to = input("Enter finish vacation date (example: 10.03): ")
            return user_data_receiver(name, surname, date_from, date_to)


@title
def user_data_receiver(name, surname, date_from, date_to):
    if vacation_type == "vacation":
        print(f"Hi John,\nI need the paid vacations from {date_from} to {date_to}. \n{name} {surname}")
    elif vacation_type == "sick leave":
        print(f"Hi John, \nI need the paid sick leave from {date_from} to {date_to}.\n{name} {surname}")
    else:
        print(f"Hi John,\nI need the days off from {date_from} to {date_to}.\n{name} {surname}")


if __name__ == "__main__":
    vacation_type = input("Enter type of vacation than you want (Vacation, Sick leave, Day off): ").lower()
    vacation_validation()
