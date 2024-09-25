# enter a string
userstring = input("Enter a long string: ")

# old way: count the number of e with a for loop
total_e = 0
for x in userstring:
    if x == "e":
        total_e += 1
print(total_e)

# new way: count the number of e using the count() function
print(userstring.count("e"))

# isalpha() function
if userstring.isalpha() == True:
    print("ALPHANUMERIC")

# upper() function
userstring_upper = userstring.upper()
print("THIS IS UPPERCASE:", userstring_upper)
