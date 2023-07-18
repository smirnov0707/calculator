class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, num):
        self.memory += num

    def subtract(self, num):
        self.memory -= num

    def multiply(self, num):
        self.memory *= num

    def divide(self, num):
        self.memory /= num

    def take_root(self, n):
        self.memory **= (1 / n)

    def reset_memory(self):
        self.memory = 0
