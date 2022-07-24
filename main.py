import string

import Handler
from Handlers.CatHandler import CatHandler
from Handlers.DogHandler import DogHandler
from Handlers.MonkeyHandler import MonkeyHandler
from Handlers.SquirrelHandler import SquirrelHandler


def who_eat(handler: Handler, food: string) -> None:
    print(f"\nClient: Who wants a {food}?")
    result = handler.handle(food)
    if result:
        print(f"  {result}", end="")
    else:
        print(f"  {food} was left untouched.", end="")

def who_eat_ifood(handler: Handler, animal: string) -> None:
    result = handler.ifood(animal)
    if result:
        print(f"  {result}", end="")
    else:
        print(f"  {animal} was left untouched.", end="")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    cat = CatHandler()

    monkey.set_next(cat).set_next(dog).set_next(squirrel)

    print("Chain: Monkey > Squirrel > Dog")
    food = 'nut'
    animal = 'cat'
    who_eat_ifood(monkey, animal)
    print("\n")
    who_eat(monkey, food)
    print("\n")
    #
    # print("Subchain: Squirrel > Dog")
    # who_eat(squirrel, food)
    #
    # print("\n")
    #
    # print("Subchain: Dog")
    # who_eat(dog, food)
