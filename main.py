from art import logo
import os


print(logo)

final_auction = {}
restart =  True
while restart == True:

  #INPUT name and bid
  name = input("What is your Name?: ")
  if name.isalpha():
    bid = int(input("What's your bid?: $"))
    
    auction = {name: bid}
    
    final_auction.update(auction)
      
    anyOtherBidder = input("Any other bidder? Y or N: ")
    
    if anyOtherBidder == "Y":
      
      os.system('cls')
    elif anyOtherBidder == "N":
      
      max_Bidder = max(final_auction.values())
      for name, bid in final_auction.items():
        if bid == max_Bidder:
          restart = False
          print(f"\n\nthe highest bidder is {name} with the bid of ${max_Bidder}.\n")
    
    else:
      print("Invalid Input. Only 'Y' and 'N' are allowed.\n")
  else:
    print("invalid input. Only alphabets allowed. \n")