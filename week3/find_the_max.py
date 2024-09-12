# Figure out which friend has the longest name.

# Make a list of friends
friends = ["Amanda", "Robin", "Andy", "Josephine", "Mark"]

# These variables keep track!
# NOTE: I initialied maxlength to 0 since I know that is 
# minimum value for length of a string, but you need
# to pick a value for your particular problem based on what you
# know about the possible outcomes.
maxlen = 0     # the length of the longest name so far
maxname = ""   # the longest name so far

# For each friend's name...
for n in friends:

    # if the length of that name is longer than the current maxlen
    if len(n) > maxlen:

        # update the maximum length to this new length
        maxlen = len(n)

        # update the longest name to this new name
        maxname = n

        # you can print this out just for a sanity check
        print(f"{maxname} is the longest name so far ({maxlen})")

# Print out result
print(f"The longest name, {maxname}, has {maxlen} characters.")
