#at least 8 characters long
#contain any sort of character, numbers $%#@
#has to end with a number
import re

password = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}\d")
passw = input("Please enter your password")

check = password.fullmatch(passw)

print(check)
