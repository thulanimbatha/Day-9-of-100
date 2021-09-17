# day project
auc_bid = {}    # empty dict
bid_end = False # while loop
highest_bid = -1    # for loop
highest_bidder = ""

'''INITIAL KEY-VALUE PAIR IN DICT'''
name = input("What is your name? ")
bid = float(input("What is your bid? "))
# add initial kv in dict
auc_bid[name] = bid
print(auc_bid)
'''START LOOP - FOR ADDITIONAL KV PAIRS'''
while not bid_end:
    other_bids = input("Is the any other bidders (type 'yes' or 'no')? ").lower()

    if other_bids == "yes":
        name = input("What is your name? ")
        bid = float(input("What is your bid? "))
        auc_bid[name] = bid
        bid_end = False
    elif other_bids == "no":
        bid_end = True
print(auc_bid)
'''DETERMINE WHICH KEY HAS THE HIGHEST VALUE'''
for name in auc_bid:
    if auc_bid[name] > highest_bid:
        highest_bid = auc_bid[name]
        highest_bidder = name
print(f"The winner is: {highest_bidder}")