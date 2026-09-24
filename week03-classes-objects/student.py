import pytest

# See: https://catalog.northeastern.edu/undergraduate/academic-policies-procedures/progression-standards/

FIRST_YEAR = 'First year'
SOPHOMORE = 'Sophomore'
JUNIOR = 'Junior'
SENIOR = 'Senior'

CLASS_STANDING_CUTOFFS = [0, 32, 64, 96]
CLASS_STANDINGS = [FIRST_YEAR, SOPHOMORE, JUNIOR, SENIOR]

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
        return f'{self.name}, {self.get_class_standing()}, with id {self.id} has earned {self.credits_earned} credits'


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


if __name__ == '__main__':
    grace : Student = Student('000000001', 'Grace Hopper', 120)
    print(grace)
