from typing import TypeVar, Generic

A = TypeVar('A')
B = TypeVar('B')

class Pair(Generic[A, B]):
    '''A continaer of exactly two values. ''' 
    def __init__(self, first: A, second: B) -> None:
        self.first = first
        self.second = second

    def swap(self) -> None:
        '''Swaps the values at first and second, only if they are of the same type'''
        if isinstance(self.first, type(self.second)):
            self.first, self.second = self.second, self.first

    def __str__(self):
        return f'<{self.first}, {self.second}>'



def main() -> None:
   '''Sample instances of Pair and calls on methods'''
   p1 = Pair(10, 20)
   p2 = Pair('center', p1)

   print(f'Before swap\np1={p1}, p2={p2}')

   p1.swap()
   p2.swap()
   print(f'After swap\np1={p1}, p2={p2}')


if __name__ == '__main__':
    main()
