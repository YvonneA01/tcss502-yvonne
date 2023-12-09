import math
import random

class Item:
    def __init__(self,name):
        self._name=name
        self._health_impact=0

    def __str__(self):
        return f'{str(self._name)}'

class Pillar(Item):
    def __init__(self,name):
        super().__init__(name)

class Vision(Item):
    def __init__(self,name):
        super().__init__(name)

class Exit(Item):
    def __init__(self,name):
        super().__init__(name)

class Healing(Item):
    def __init__(self,name):
        super().__init__(name)
        self._health_impact=random.randint(5, 15)

class Pit(Item):
    def __init__(self,name):
        super().__init__(name)
        self._health_impact=-random.randint(1, 20)

class ItemIterator:
    def __init__(self,item_list):
        self._item_list=item_list
        self._index=0

    def __next__(self):
        if self._index == len(self._item_list):
            raise StopIteration()

        temp_item=self._item_list[self._index]
        self._index+=1
        return temp_item

    def __iter__(self):
        return self



"This is just some testing code."

List=[]

List.append(Pillar("Abstraction"))
List.append(Pillar("Encapsulation"))
List.append(Pillar("Inheritance"))
List.append(Pillar("polyMorphism"))

List.append(Vision("Vision Potion"))

List.append(Exit("Exit"))

List.append(Healing("Healing Potion"))
List.append(Pit("Pit"))




print(List[5]._name)
