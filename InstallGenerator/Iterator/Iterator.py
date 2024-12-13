# Загальний клас Iterator
class Iterator:
    def __init__(self, iterator_imp):
        self.iterator_imp = iterator_imp

    def first(self):
        return self.iterator_imp.first()

    def next(self):
        return self.iterator_imp.next()

    def is_done(self):
        return self.iterator_imp.is_done()

    def current_item(self):
        return self.iterator_imp.current_item()