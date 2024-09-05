
def odd_or_even(n):
    if n % 2 == 0:
        print(n, "is even!")
    else:
        print(n, "is odd")

def main():

    n = int(input("enter a number: "))
    odd_or_even(n)
    a = 15
    odd_or_even(a)
    odd_or_even(10)

main()

