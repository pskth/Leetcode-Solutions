class AuctionSystem:
    """
    d[itemID] = (userId, bidAmount)
    """
    def __init__(self):
        self.sl = dict()
        self.d = collections.defaultdict(int)
        
    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.sl:
…# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)