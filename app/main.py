class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(peoples: list) -> list:
    person_list = []
    for person in peoples:
        newperson = Person(person["name"], person["age"])
        person_list.append(newperson)
        Person.people[person["name"]] = newperson

    for person in peoples:
        newperson = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            newperson.wife = Person.people[person["wife"]]
            newperson.wife.husband = newperson
        elif "husband" in person and person["husband"]:
            newperson.husband = Person.people[person["husband"]]
            newperson.husband.wife = newperson
    return person_list
