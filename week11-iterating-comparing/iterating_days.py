from collections.abc import Iterable, Iterator

# DISCLAIMER: This sample code is done to demonstrate concepts in a course
# As such, it's incomplete. For example, it's missing complete docstrings
# that are otherwise required in our code.

class Calendar(Iterable[str]):
    def __init__(self, days: list[str]):
        self._days = days

    def __iter__(self) -> Iterator[str]:
        """Returns an iterator over the days in this Calendar"""
        return iter(self._days) # delegating to the list's iterator

    def __reversed__(self) -> Iterator[str]:
        return reversed(self._days) # also delegating

    def alternating(self) -> Iterator[str]:
        """Returns an iterator for every other day in this Calendar"""
        return AlternatingDayIterator(self._days)

class AlternatingDayIterator(Iterator[str]):
    def __init__(self, days: list[str]):
        self._days = days
        self._index: int = 0
    
    def __next__(self) -> str:
        if self._index >= len(self._days):
            raise StopIteration
        
        value = self._days[self._index]
        self._index += 2
        return value

def demo() -> None:
    days = Calendar(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

    print('Days using natural/default iterator')
    for day in days:
        print(day)

    print('Days in reverse iterator:')
    for day in reversed(days):
        print(day)

    print('\n\nAlternating days iterator:')
    for alt in days.alternating():
        print(alt)

if __name__ == '__main__':
    demo()