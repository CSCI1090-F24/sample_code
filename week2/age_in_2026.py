
# Here's the function to calculate the age in 2026.
# The parameters are an int, age, and a string, name
def age_in_2026(age, name):
    agein2026 = age + (2026-2024)
    print(name, "will be", agein2026, "in 2026")


def main():

    # get input from the user
    # remember to convert the age to an int!
    n = input("what is your name? ")
    a = int(input("what is your age? "))

    # call the function
    age_in_2026(a, n)

    # another way to call the function
    age_in_2026(75, "Bert")
    
    

# don't forget to call main()!
main()




