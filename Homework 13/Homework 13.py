def title(func):
    def wrapper():
        print(">" * 35)
        print("CEO Red Bull Inc. Mr. John Bigbull")
        print(">" * 35)
        return func()
    return wrapper


@title
def vacation_pattern():
    input_data = input("Enter type of vacation than you want (Vacation, Sick leave, Day off): ")
    input_1 = input_data.lower()
    if input_1 != "vacation" and input_1 != "sick leave" and input_1 != "day off":
        print("You entered type of vacation incorrectly")
    else:
        entered_data = input("Enter your Name, Surname, Date from, To date: ")
        data = entered_data.split()
        if len(data) != 4:
            print("You entered incorrect data (You need enter Name, Surname, Date from, To date)")
        elif input_1 == "Vacation":
            print(f"Hi John,\nI need the paid vacations from {data[2]} to {data[3]}. \n{data[0]} {data[1]}")
        elif input_1 == "Sick leave":
            print(f"Hi John, \nI need the paid sick leave from {data[2]} to {data[3]}.\n{data[0]} {data[1]}")
        else:
            print(f"Hi John,\nI need the days off from {data[2]} to {data[3]}.\n{data[0]} {data[1]}")


vacation_pattern()


