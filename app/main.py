class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    list_of_persons_instances = [
        Person(person["name"],
               person["age"])
        for person in people
    ]

    for i, person in enumerate(people):
        get_wife = person.get("wife")
        get_husband = person.get("husband")
        person_instance = list_of_persons_instances[i]
        if get_wife:
            person_instance.wife = person_instance.people[get_wife]
        elif get_husband:
            person_instance.husband = person_instance.people[get_husband]

    return list_of_persons_instances
