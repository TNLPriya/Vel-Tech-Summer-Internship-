age = int(input("Enter your age: "))
if(age<2026):
    present = 2026-age
    future = present+10
    print(f"You were born in {present} and after 10 years it will be {future}.")
else:
    print("Please enter a valid age.")