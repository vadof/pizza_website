
class Pizza:

    counter = 1

    def __init__(self, name, price, ingredients, image):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.image = image

    def show_ingredients(self):
        return ', '.join(map(str, self.ingredients))

    @classmethod
    def get_count(cls):
        cls.counter += 1
        return cls.counter

    def get_image_dir(self):
        return f"pizza/menu/images/pizza_images/{self.image}"


winter_pizza = Pizza('Winter Pizza', 8.50, ['Tomate sauce', 'Pepperoni', 'Greenery', 'Pickles'], 'pizza1.jpg')
pepperoni_pizza = Pizza('Pepperoni Pizza', 6.50, ['Tomate sauce', 'Pepperoni'], '2.jpg')
other_pizza = Pizza('Other Pizza', 23.50, ['Tomate sauce', 'Pepperoni', 'Potato'], 'pizza1.jpg')

pizzas = [winter_pizza, pepperoni_pizza, other_pizza]
