# dictionaries



# grading program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# dictionaries in a list
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
    travel_log.append({"country": country, "visits": visits, "cities": list_of_cities})

add_new_country("USA", 19, ["San Francisco", "Chicago", "San Diego"])
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")


# Blind Auction
other_bidders = 'yes'
print("Welcome to the secret auction program.")
auction = {}
while other_bidders == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))

    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
# print(auction)

highest_bid = {'bidder': 'default', 'amount': 0}
# Below should be its own function 
for bidder in auction:
    # print(bidder, auction[bidder])
    if auction[bidder] > highest_bid["amount"]:
        highest_bid = {}
        highest_bid["bidder"] = bidder
        highest_bid["amount"] = auction[bidder]

print(f"The winner is {highest_bid['bidder']} with a bid of {highest_bid['amount']}.")
