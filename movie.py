from pricing import NewRelease, RegularPrice, ChildrensPrice

class Movie:
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title
