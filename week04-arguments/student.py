import pytest

UNDECLARED : str = 'Undeclared'

# DISCLAIMER: This sample code is done to demonstrate concepts in a course
# As such, it's incomplete. For example, it may be missing complete docstrings
# that are otherwise desired/required in our code.

# This class is defined only with an object initializer as it's used to
# demonstrate default argument values and keyword parameters

class Student:
    """Models a student at a university"""
    def __init__(self, student_id : str, name : str, *,    # We discussed purpose of this * in class
                 major : str = UNDECLARED, credits_earned: int = 0) -> None:
        self.id : str = student_id
        self.name = name
        self.major = major
        self.credits_earned = credits_earned

    def __str__(self) -> str:
        """A descriptive string representation of the Student"""
        return f'{self.name}, with id {self.id} ' + \
               f'major: {self.major} and has earned {self.credits_earned} credits'


def main() -> None:
    grace  : Student =  Student("001732", "Grace Hopper") # no major and no incoming credits
    woz    : Student = Student("019254", "Steve Wozniak", major="CS") # major but no incoming credits
    liskov : Student = Student("000251", "Barbara Liskov", credits_earned=12) # no major but has incoming credits
    tbl    : Student = Student("000387", "Tim Berners-Lee", major="Physics", credits_earned=24) # both

    print(grace, woz, liskov, tbl, sep='\n')

if __name__ == "__main__":
    main()
