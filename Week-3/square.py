# List of animals in correct zodiac order
animals = [
    "Rat", "Ox", "Tiger", "Rabbit",
    "Dragon", "Snake", "Horse", "Goat",
    "Monkey", "Rooster", "Dog", "Pig"
]

# Read year input
year = int(input("Enter a year greater than 0: "))

if year > 0:
    # 2020 was a Rat year, so use it as reference
    index = (year - 2020) % 12
    print("Chinese Zodiac Animal:", animals[index])
else:
    print("Year must be greater than zero.")
