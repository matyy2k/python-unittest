import random


class TechStack:

    def __init__(self):
        self.tech_name = []

    def add_tech(self, name):
        if not name in self.tech_name:
            self.tech_name.append(name)
            return self
        return self

    def get_tech(self):
        return random.choice(self.tech_name)
