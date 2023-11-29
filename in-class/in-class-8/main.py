# lab 1
class Car:
    def __init__(self, model_year, purchase_price):
        self.model_year = model_year
        self.purchase_price = purchase_price
        self.current_value = purchase_price

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.model_year
        self.current_value = round(
            self.purchase_price * (1 - depreciation_rate) ** car_age
        )

    def print_info(self, current_year):
        self.calc_current_value(current_year)
        print("Car's information:")
        print("   Model year:", self.model_year)
        print("   Purchase price: ${:,.2f}".format(self.purchase_price))
        print("   Current value: ${:,.2f}".format(self.current_value))


class FoodItem:
    def __init__(self, name="Water", fat=0.0, carbs=0.0, protein=0.0, servings=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = servings

    def get_calories(self, num_servings=1.0):
        calories = (
            (self.fat * 9) + (self.carbs * 4) + (self.protein * 4)
        ) * num_servings
        return calories

    def print_info(self):
        print("Nutritional information per serving of {}: ".format(self.name))
        print("   Fat: {:.2f} g".format(self.fat))
        print("   Carbohydrates: {:.2f} g".format(self.carbs))
        print("   Protein: {:.2f} g".format(self.protein))
        print(
            "Number of calories for 1.0 serving(s): {:.2f}".format(self.get_calories())
        )
        print(
            "Number of calories for {:.2f} serving(s): {:.2f}".format(
                self.servings, self.get_calories(self.servings)
            )
        )


def main():
    # lab 1
    year = int(input("Enter the car's purchase year: "))
    price = float(input("Enter the car's purchase price: "))
    car = Car(year, price)
    current_year = int(input("Enter the current year: "))
    car.print_info(current_year)

    # lab 2
    name = input("Enter food item name: ")
    fat = float(input("Enter fat content (in grams): "))
    carbs = float(input("Enter carbohydrate content (in grams): "))
    protein = float(input("Enter protein content (in grams): "))
    servings = float(input("Enter number of servings: "))
    food = FoodItem(name, fat, carbs, protein, servings)
    food.print_info()


main()
