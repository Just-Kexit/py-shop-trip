from app.car import Car
from app.utils import calculate_distance\

class Customer:
    def __init__(self, name, product_cart, location, money, car_data):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car_data

    def __str__(self):
        return f"{self.name} (${self.money})"

    def trip_cost(self, shop, fuel_price):
        distance_to_shop = calculate_distance(self.location, shop.location)
        round_trip_km = distance_to_shop * 2

        fuel_needed = (round_trip_km * self.car["fuel_consumption"]) / 100
        fuel_cost = fuel_needed * fuel_price

        product_cost = 0
        for product, amount in self.product_cart.items():
            if product not in shop.products:
                return float("inf")  # магазин не має потрібного продукту
            product_cost += shop.products[product] * amount

        total_cost = fuel_cost + product_cost
        return round(total_cost, 2)