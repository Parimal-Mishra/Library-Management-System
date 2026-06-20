class Book:
    def __init__(self, id, name, quantity):
        self.id = int(id)
        self.name = str(name).strip()
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.id}: {self.name} ({self.quantity} available)"
