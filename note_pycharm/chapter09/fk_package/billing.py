class Item:
    '定义代表商品的item类'

    def __init__(self, price):
        self.price = price

    def __repr__(self):
        return 'Item[price=%g]' % self.price
