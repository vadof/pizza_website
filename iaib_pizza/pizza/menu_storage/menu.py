
class Food:

    def __init__(self, name, price, ingredients, image, id):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.image = image
        self.id = id

    def show_ingredients(self):
        return ', '.join(map(str, self.ingredients))

    def get_image_dir(self):
        pass


class Pizza(Food):

    def get_image_dir(self):
        return f"pizza/menu/images/pizza_images/{self.image}"


class Burger(Food):

    def get_image_dir(self):
        return f"pizza/menu/images/burger_images/{self.image}"


class Drink:

    def __init__(self, name, price, ml, image, id):
        self.name = name
        self.price = price
        if ml < 1000:
            self.ml = f'{ml} ml'
        elif ml // 1000 == 0:
            self.ml = f'{ml // 1000} l'
        else:
            self.ml = f'{int(ml // 1000)} l {ml % 1000}'
        self.image = image
        self.id = id

    def get_image_dir(self):
        return f"pizza/menu/images/drinks_images/{self.image}"
