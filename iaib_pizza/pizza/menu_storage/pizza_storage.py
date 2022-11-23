
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


winter_pizza = Pizza('Winter Pizza', 8.50, ['Ham', 'Bacon', 'Cheese', 'Parmesan', 'Tomato sauce'], 'pizza1.jpg')
pepperoni_pizza = Pizza('Pepperoni Pizza', 8.00, ['Pepperoni', 'Tomato sauce', 'BBQ sauce', 'Cheese'], 'pepperoni.jpg')
avocado_pizza = Pizza('Avocado Pizza', 6.50, ['Avocado', 'Crispy cauliflower', 'Tomato sauce', 'Cheddar'], 'avocado.jpg')
jalapeno_pizza = Pizza('Jalapeno Pizza', 8.00, ['Jalapeno', 'Paprika', 'Mushrooms', 'Spicy tomato sauce', 'Cheddar'], 'jalapeno.jpg')
mushroom_pizza = Pizza('Mushroom Pizza', 6.50, ['Mushrooms', 'Tomato sauce', 'Brie cheese', 'Fresh thyme'], 'mushrooms.jpg')
mozzarella_pizza = Pizza('Mozzarella Pizza', 7.00, ['Mozzarella', 'More cheese', 'Tomato sauce', 'Cherry tomatoes', 'Fresh basil'], 'mozzarella.jpg')
shrimp_pizza = Pizza('Shrimp Pizza', 8.50, ['Shrimps', 'Tomato sauce with garlic', 'Cheese', 'Parsley'], 'shrimps.jpg')
olive_pizza = Pizza('Salad Pizza', 6.50, ['Olives', 'Green paprika', 'Red onions', 'Tomato sauce', 'Cheese'], 'pizza.jpg')

pizzas = [winter_pizza, pepperoni_pizza, avocado_pizza, jalapeno_pizza, mushroom_pizza, mozzarella_pizza, shrimp_pizza, olive_pizza]
