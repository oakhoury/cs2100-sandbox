# See: https://catalog.northeastern.edu/undergraduate/academic-policies-procedures/progression-standards/

FIRST_YEAR : str = 'First year'
SOPHOMORE : str = 'Sophomore'
JUNIOR : str = 'Junior'
SENIOR : str = 'Senior'

CLASS_STANDING_CUTOFFS : list[int] = [0, 32, 64, 96]
CLASS_STANDINGS : list[str] = [FIRST_YEAR, SOPHOMORE, JUNIOR, SENIOR]
FULL_TIME_CREDITS = 16

# DISCLAIMER: This sample code is done to demonstrate concepts in a course
# As such, it's incomplete. For example, it's missing complete docstrings
# that are otherwise desired/required in our code.

class Student:
    """Models a student at a university"""
    def __init__(self, student_id : str, first_name : str, last_name : str, credits_earned: int) -> None:
        self._id : str = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._credits_earned = credits_earned

    def earn_credits(self, additional_credits : int) -> None:
        """Updates the accumulated credits earned by the `credits` amount.
        
            As discussed, this is a mutator method as it mutates/changes the state of the object.
        """
        self._credits_earned += additional_credits

    @property
    def name(self) -> str:
        return f'{self._first_name} {self._last_name}'

    def get_class_standing(self) -> str:
        """Returns the class standing of the student based on accumulated credits earned.
        
            This is an accessor method as it makes no mutations/changes on the object.
        """
        class_standing : str = SENIOR
        if self._credits_earned < 32:
            class_standing = FIRST_YEAR
        elif self._credits_earned < 64:
            class_standing = SOPHOMORE
        elif self._credits_earned < 96:
            class_standing = JUNIOR

        return class_standing

    def __repr__(self) -> str:
        """"A representation of the Student"""
        return f'Student({self._id}, {self.name})'
    
    def __str__(self) -> str:
        """A descriptive string representation of the Student"""
        return f'Student({self.name}, {self.get_class_standing()}, with id {self._id} ' + \
               f'has earned {self._credits_earned} credits)'

    def __eq__(self, other : object) -> bool:
        """Compares two objects for equality returning True if id's are the same"""
        if isinstance(other, Student):
            return self._id == other._id # Assumes unique id's
        return NotImplemented   # Update... this is the expected return on incompatible types
    
    def __lt__(self, other : object) -> bool:
        """Compares two objects for equality returning True if id's are the same"""
        if isinstance(other, Student):
            return self._id < other._id
        return NotImplemented  # Update... this is the expected return on incompatible types


def main() -> None:
    james  = Student('000443103', 'James', 'Gosling', 115)
    james2 = Student('000135678', 'James', 'Patrick', 104)

    students = [james, james2, Student('000472652', 'Ryan', 'Gosling', 60)]

    # Not implemented... but can still use it!
    print(f'james > james2: {james > james2}')
    
    # print(james < 10) # This should raise an exception

    # The relational operators define the "natural order" which is what's used in functions like sorted

    print(sorted(students))

if __name__ == '__main__':
    main()

