from pricing import NewRelease, RegularPrice, ChildrensPrice

class Movie:
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title, price_strategy):
        self.title = title
        self.price_strategy = price_strategy

    def get_title(self):
        return self.title