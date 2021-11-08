class user:
    id: int
    first_name: str
    last_name: str
    house: str

    def __init__(self, id: int, fname: str, lname: str, house: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.house = house


def find_house(animal: str) -> str:
    if animal == 'eagle':
        return 'ravenclaw'
    elif animal == 'lion':
        return 'gryffindor'
    elif animal == 'badger':
        return 'hufflepuff'
    else:
        return 'slytherin'
