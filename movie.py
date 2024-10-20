from pricing import NewRelease, RegularPrice, ChildrensPrice

class Movie:
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code


    def get_title(self):
        return self.title

    def get_price_code(self):
        return self.price_code