# First solution
username = input()
password = input()

data = input()
while data != password:
    data = input()
print(f"Welcome {username}!")

# Second solution

# username = input()
# password = input()
# user_input = input()
# while True:
#    if user_input != password:
#       user_input = input()
#        continue
#   else:
#        print(f"Welcome {username}!")
#       break
