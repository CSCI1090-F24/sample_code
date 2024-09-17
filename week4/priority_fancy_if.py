# Assign a priority to a student for CS course registration
# based on their graduation year and major.

# get into
year = int(input("what year will you graduate? "))
major = input("are you a CS major? ")

# initialize the priority
priority = 0

# solve the problem using conjoined conditions

# if they're a major and a senior...
if major=="yes" and year==2025:
    priority = 1

# else if they're a major and a junior...
elif major=="yes" and year==2026:
    priority = 2

# if they're a senior but not a major...
elif year == 2025:
    priority = 3

# if they are a major and a sophomore...
elif major == "yes" and year==2027:
    priority= 4

# if they are a junior and not a major...
elif year == 2026:
    priority = 5

# if they are a sophomore OR a freshman
elif year == 2027 or year == 2028:
    priority = 6

print(f"Your priority is {priority}")


# solve the problem using nested if statements

# first check if they are a major, then check their year
if major == "yes":
    if year == 2025:
        priority = 1
    elif year == 2026:
        priority = 2
    elif year == 2027:
        priority = 4
else:
    if year == 2025:
        priority = 3
    elif year == 2026:
        priority = 5
    else:
        priority = 6
