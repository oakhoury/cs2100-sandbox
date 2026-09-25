import pytest

# See: https://catalog.northeastern.edu/undergraduate/academic-policies-procedures/progression-standards/


FIRST_YEAR : str = 'First year'
SOPHOMORE : str = 'Sophomore'
JUNIOR : str = 'Junior'
SENIOR : str = 'Senior'

CLASS_STANDING_CUTOFFS : list[int] = [0, 32, 64, 96]
CLASS_STANDINGS : list[str] = [FIRST_YEAR, SOPHOMORE, JUNIOR, SENIOR]
FULL_TIME_CREDITS = 16

class Student:
    """Models a student at a university"""
    def __init__(self, student_id : str, name : str, credits_earned: int) -> None:
        self.id : str = student_id
        self.name = name
        self.credits_earned = credits_earned

    def earn_credits(self, additional_credits : int) -> None:
        """Updates the accumulated credits earned by the `credits` amount """
        self.credits_earned += additional_credits

    def get_class_standing(self) -> str:
        """Returns the class standing of the student based on accumulated credits earned"""
        class_standing : str = SENIOR
        if self.credits_earned < 32:
            class_standing = FIRST_YEAR
        elif self.credits_earned < 64:
            class_standing = SOPHOMORE
        elif self.credits_earned < 96:
            class_standing = JUNIOR

        return class_standing

    def __str__(self) -> str:
        return f'{self.name}, {self.get_class_standing()}, with id {self.id} ' + \
               f'has earned {self.credits_earned} credits'


@pytest.fixture(name="senior_student")
def fixture_senior_student() -> Student:
    """Define the Student object in senior standing"""
    return Student('000135678', 'James Gosling', 115)

@pytest.fixture(name="junior_student")
def fixture_junior_student() -> Student:
    """Define the Student object in senior standing"""
    return Student('000135432', 'Marissa Mayer', 64)


class TestStudent:  # Name must start with Test
    """Tests of the Student class"""


    def test_class_standing_senior(self, senior_student : Student) -> None:
        """Tests a class standing of a senior student"""
        assert senior_student.get_class_standing() == SENIOR

    def test_class_standing_junior(self, junior_student : Student) -> None:
        """Tests a class standing of a junior student"""
        assert junior_student.get_class_standing() == JUNIOR

    def test_earn_credits(self, junior_student : Student) -> None:
        """Tests the earn credits method increases accumulated earned credits"""
        current_credits : int = junior_student.credits_earned
        junior_student.earn_credits(10)
        assert junior_student.credits_earned == current_credits + 10


def end_of_term_earn_credits(students : list[Student]) -> None:
    """Simulates end of a term by each student in the list earning \
        FULL_TIME_CREDITS, assumes a full-time load and they pass all courses"""

    for s in students:
        s.earn_credits(FULL_TIME_CREDITS)

def main() -> None:
    grace : Student = Student('000000001', 'Grace Hopper', 120)
    james : Student = Student('000135678', 'James Gosling', 115)
    marissa : Student = Student('000135432', 'Marissa Mayer', 64)

    all_students : list[Student] = [james, marissa, grace]

    end_of_term_earn_credits(all_students)

    print(*all_students, sep="\n") # *all_students will "unpack" the list
    # Alternatively, use list comprehension
    # print("\n".join(str(s) for s in all_students))


if __name__ == "__main__":
    main()

# Visualization in Python Tutor!
# https://pythontutor.com/visualize.html#code=%23%20See%3A%20https%3A//catalog.northeastern.edu/undergraduate/academic-policies-procedures/progression-standards/%0A%0AFIRST_YEAR%20%3A%20str%20%3D%20'First%20year'%0ASOPHOMORE%20%3A%20str%20%3D%20'Sophomore'%0AJUNIOR%20%3A%20str%20%3D%20'Junior'%0ASENIOR%20%3A%20str%20%3D%20'Senior'%0A%0ACLASS_STANDING_CUTOFFS%20%3A%20list%5Bint%5D%20%3D%20%5B0,%2032,%2064,%2096%5D%0ACLASS_STANDINGS%20%3A%20list%5Bstr%5D%20%3D%20%5BFIRST_YEAR,%20SOPHOMORE,%20JUNIOR,%20SENIOR%5D%0AFULL_TIME_CREDITS%20%3D%2016%0A%0Aclass%20Student%3A%0A%20%20%20%20%22%22%22Models%20a%20student%20at%20a%20university%22%22%22%0A%20%20%20%20def%20__init__%28self,%20student_id%20%3A%20str,%20name%20%3A%20str,%20credits_earned%3A%20int%29%20-%3E%20None%3A%0A%20%20%20%20%20%20%20%20self.id%20%3A%20str%20%3D%20student_id%0A%20%20%20%20%20%20%20%20self.name%20%3D%20name%0A%20%20%20%20%20%20%20%20self.credits_earned%20%3D%20credits_earned%0A%0A%20%20%20%20def%20earn_credits%28self,%20additional_credits%20%3A%20int%29%20-%3E%20None%3A%0A%20%20%20%20%20%20%20%20%22%22%22Updates%20the%20accumulated%20credits%20earned%20by%20the%20%60credits%60%20amount%20%22%22%22%0A%20%20%20%20%20%20%20%20self.credits_earned%20%2B%3D%20additional_credits%0A%0A%20%20%20%20def%20get_class_standing%28self%29%20-%3E%20str%3A%0A%20%20%20%20%20%20%20%20%22%22%22Returns%20the%20class%20standing%20of%20the%20student%20based%20on%20accumulated%20credits%20earned%22%22%22%0A%20%20%20%20%20%20%20%20class_standing%20%3A%20str%20%3D%20SENIOR%0A%20%20%20%20%20%20%20%20if%20self.credits_earned%20%3C%2032%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20class_standing%20%3D%20FIRST_YEAR%0A%20%20%20%20%20%20%20%20elif%20self.credits_earned%20%3C%2064%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20class_standing%20%3D%20SOPHOMORE%0A%20%20%20%20%20%20%20%20elif%20self.credits_earned%20%3C%2096%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20class_standing%20%3D%20JUNIOR%0A%0A%20%20%20%20%20%20%20%20return%20class_standing%0A%0A%20%20%20%20def%20__str__%28self%29%20-%3E%20str%3A%0A%20%20%20%20%20%20%20%20return%20f'%7Bself.name%7D,%20%7Bself.get_class_standing%28%29%7D,%20with%20id%20%7Bself.id%7D%20'%20%2B%20%5C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20f'has%20earned%20%7Bself.credits_earned%7D%20credits'%0A%0Adef%20end_of_term_earn_credits%28students%20%3A%20list%5BStudent%5D%29%20-%3E%20None%3A%0A%20%20%20%20for%20s%20in%20students%3A%0A%20%20%20%20%20%20%20%20s.earn_credits%28FULL_TIME_CREDITS%29%0A%0Adef%20main%28%29%20-%3E%20None%3A%0A%20%20%20%20grace%20%3A%20Student%20%3D%20Student%28'000000001',%20'Grace%20Hopper',%20120%29%0A%20%20%20%20james%20%3A%20Student%20%3D%20Student%28'000135678',%20'James%20Gosling',%20115%29%0A%20%20%20%20marissa%20%3A%20Student%20%3D%20Student%28'000135432',%20'Marissa%20Mayer',%2064%29%0A%0A%20%20%20%20all_students%20%3A%20list%5BStudent%5D%20%3D%20%5Bjames,%20marissa,%20grace%5D%0A%0A%20%20%20%20end_of_term_earn_credits%28all_students%29%0A%0A%20%20%20%20print%28*all_students,%20sep%3D%22%5Cn%22%29%20%23%20*all_students%20will%20%22unpack%22%20the%20list%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main%28%29%0A&mode=edit&origin=opt-frontend.js&py=311
