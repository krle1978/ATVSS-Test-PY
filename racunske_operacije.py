# calculator.py
class Calculator:
    def __init__(self, num1, num2):
        """Inicijalizacija sa dva broja"""
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Vraća zbir dva broja"""
        return self.num1 + self.num2

    def subtract(self):
        """Vraća razliku između dva broja"""
        return self.num1 - self.num2

    def multiply(self):
        """Vraća proizvod dva broja"""
        return self.num1 * self.num2

    def divide(self):
        """Vraća količnik dva broja. Proverava da li je drugi broj nula."""
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Deljenje nulom nije dozvoljeno!"
