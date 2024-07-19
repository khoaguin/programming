class IDiscountCalculator:
    def calculate(self, order):
        raise NotImplementedError

    
class NoDiscount(IDiscountCalculator):
    def calculate(self, order):
        return 0


class TwentyPercentDiscount(IDiscountCalculator):    
    def calculate(self, order):
        return order.price * 0.20


class OnSaleDiscount(IDiscountCalculator):
    def calculate(self, order):
        return order.price * 0.25 + 20
    

# Dependency injection container
class DiscountStrategies:
    def __init__(self):
        self.no_discount = NoDiscount()
        self.on_sale_discount = OnSaleDiscount()
        self.twenty_percent_discount = TwentyPercentDiscount()


"""A separate class for Item"""
class Item:

    def __init__(self, price, discount_strategy: IDiscountCalculator):
        self.price = price
        self.discount_strategy = discount_strategy
        self.discount_strategy_str = self.discount_strategy.__class__.__name__

    def price_after_discount(self):
        """A separate function for price after discount"""
        if self.discount_strategy:
            discount = self.discount_strategy.calculate(self)
        else:
            discount = 0
            
        return self.price - discount

    def __repr__(self):
        if self.discount_strategy:
            statement = f"Price: {self.price}, price after {self.discount_strategy_str}: {self.price_after_discount()}"
        else:
            statement = f"Price: {self.price}. No discount applied!"
        return statement


"""main function"""
if __name__ == "__main__":
    discount_strats = DiscountStrategies()
    user_input = input("Enter discount strategy (on sale / 20 / no discount): ")
    if user_input == "no":
        discount_strat = discount_strats.no_discount
    elif user_input == "on sale":
        discount_strat = discount_strats.on_sale_discount
    elif user_input == "20":
        discount_strat = discount_strats.twenty_percent_discount
    else:
        raise ValueError("Invalid discount strategy")
    """with discount strategy as 20 % discount"""
    print(Item(20000, discount_strategy=discount_strat))