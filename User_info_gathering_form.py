# We will begin by gathering name information
fname = input("What is your first name? > ")

# Asking the question to assist the code in making the decision of whether to ask for a middle name
q_midname = input("Do you have a middle name? \nAnswer (Y/N) > ")

# Created an if statement to evaluate if asking for the middle name is necessary.
if q_midname == 'Y'.lower():
    mid_name = input("What is your middle name? > ")
# instructing the code to skip over the question if the user answers no to having a middle name.
elif q_midname == 'N'.lower():
    pass
lname = input("What is your last name? > ")

# Assembling the user's name into single string & and capitalizing the name.
full_name = (fname +' '+ lname).title()

# printing full name
print(f"Thank you {full_name}")

# Gathering all other info
post_code = input("What is your post code? > ")
ni_num = input("What is your NI num? > ")
sparta_course = input("What course are you on at Sparta? > ")
recent_edu = input("Latest place of education? > ")
age = int(input("How old are you? > "))

# All information printed in a statement using a print statement and f-string.
print(f"{full_name}, your post code is {post_code}. Your NI number is {ni_num}. You are studying {sparta_course} at Sparta Global. \nYou last worked\studied at {recent_edu} and you are {age}.")


