

class Product():
    def __init__(self, unit_cost, unit_price, pricing_strategy):
        self.unit_cost = unit_cost
        self.unit_price = unit_price
        self.pricing_strategy = pricing_strategy

    def get_total_price(self, number_of_products):
        # return the pricing strategy applied to the base price or whatever
        if self.pricing_strategy == None:
            return self.unit_price*number_of_products
        # else:
        #     return pricing_strategy(base_price, etc...)

    