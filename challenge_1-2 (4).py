def is_leap_year(year):
    # Define a dictionary where keys are conditions and values are corresponding actions.
    conditions = {
        "divisible_by_4": lambda: year % 4 == 0,
        "divisible_by_100": lambda: year % 100 == 0,
        "divisible_by_400": lambda: year % 400 == 0,
    }

    # Define the logic for leap year determination using the conditions dictionary.
    is_leap = (
        conditions["divisible_by_4"]() and
        (conditions["divisible_by_100"]() or conditions["divisible_by_400"]())
    )

    return is_leap

# Input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year and print the result
if is_leap_year(year):
    print(year," is a leap year.")
else:
    print(year," is not a leap year.")
