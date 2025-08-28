class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You took {self.color} {self.model} for a drive.")

    def stop(self):
        print(f"You parked {self.color} {self.model} in a garage.")

    def details(self):
        print(f"{self.model} {self.year} {self.color} {self.for_sale}")