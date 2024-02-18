import requests
import sheety


print("Welcome to Utkarsh's Flight Club.")
print("We find the best flight deals and email you.")

f_name = input("What is your first name?\n").title()
l_name = input("What is your last name?\n").title()
email = "email"
re_email = "re_email"

while email != re_email:
    email = input("What is your email?\n")
    if email.lower() == "quit" or email.lower() == "exit":
        exit()
    re_email = input("Type your email again.\n")
    if re_email.lower() == "quit" or re_email.lower() == "exit":
        exit()

print("Ok. You are in the club!")

sheety.post_new_row(first_name=f_name, last_name=l_name, email=email)

