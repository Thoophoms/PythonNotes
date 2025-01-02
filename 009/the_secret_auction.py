from art import art

print(art)
print("Welcome to the Secret Auction program")

end = False
most_bid = {}

while not end:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    # Todo: Check if the most_bid dict is empty. If so, the person who just bid is the most bidder
    if not most_bid:
        most_bid[bidder_name] = bid_amount
    else:
        # Todo: Get a hold of the most bid value
        current_highest_bid = max(most_bid.values())

        # Todo: Check if the new bid value = the current bid value
        if  bid_amount == current_highest_bid:
            most_bid[bidder_name] = bid_amount
        # Todo: Check if the new bid value is higher than the current bid value
        elif bid_amount > current_highest_bid:
            most_bid.clear()
            most_bid[bidder_name] = bid_amount


    # Todo: Check if there is any more bidder
    more_bidder = (input("Are there any other bidders? Type 'yes' or 'no'.: ")).lower()
    if more_bidder == "yes":
        print("\n" * 100)
    else:
        print("\n" * 100)
        print("The most bid: ")
        for key, value in most_bid.items():
            print(f"{key} with the bid amount of ${value}.")
        end = True
