import random
import string
from dataclasses import dataclass, field

# eviter classe boiler plate = classe ou tu dois ecrire :
# __init__, __repr__ à la chaine (plaque métal écrasé à la chaine)


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


# data class genere le __init__ avec name, surname etc le self.name etc;
# et le repr aussi
# le field(init=False) ne sera pas dans le __init__,
# on peut pas les metre entre ()
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    # post init dans les data classe pour
    # appeler des fonction d init et pas __init__
    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.capitalize()
        self.id = generate_id()


def main():
    try:
        student = Student(name="Edward", surname="agle")
        print(student)

        student2 = Student(name="Edward", surname="agle", id="toto")
        print(student2)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
