"""A separate class for Item"""
class Item:

    def __init__(self, price, discount_strategy = None):
        """Constructor function with price and discount
        take price and discount strategy
        """
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        """A separate function for price after discount"""
        
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
            
        return self.price - discount

    def __repr__(self):
        if self.discount_strategy:
            statement = f"Price: {self.price}, price after {self.discount_strategy.__qualname__}: {self.price_after_discount()}"
        else:
            statement = f"Price: {self.price}. No discount applied!"
        return statement


def on_sale_discount(order):
    """function dedicated to On Sale Discount"""
    return order.price * 0.25 + 20


def twenty_percent_discount(order):
    """function dedicated to 20 % discount"""
    return order.price * 0.20


"""main function"""
if __name__ == "__main__":
    print(Item(20000))
    # the user decides which discount strategy to use at run time
    user_input = input("Enter discount strategy (on sale / 20): ")
    if user_input == "on sale":
        print(Item(20000, discount_strategy = on_sale_discount))
    elif user_input == "20":
        print(Item(20000, discount_strategy = twenty_percent_discount))
    else:
        raise ValueError("Invalid discount strategy")