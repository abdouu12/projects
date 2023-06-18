print("Welcome to the secret auction")
def auction(name_of_auction,bid_of_auction):
    auctiondict = {}

    auctiondict["name"] = name_of_auction
    auctiondict["bid"] = bid_of_auction
    auctionlist.append(auctiondict)
    list_of_bids.append(auctiondict["bid"])
list_of_bids = []
auctionlist = []
endofauction = False
while endofauction is False:
 name = str(input("what is your name: "))
 bid = int(input("what is your bid: "))
 auction(name_of_auction=name,bid_of_auction=bid)
 end = str(input("is that it?"))
 if end == "yes":
     list_of_bids.sort(reverse=True)
     auctionlist.sort(key=lambda x: x["bid"], reverse=True)
     winnerlist = auctionlist[0]
     print('the winner is :', winnerlist["name"] , "with a bid of",list_of_bids[0])
     endofauction = True
 elif end == "no":
     continue











