from typing import TypeVar, Generic, Sequence, reveal_type

T = TypeVar('T')

# Example from Python documentation on Generics
# source: https://typing.python.org/en/latest/reference/generics.html

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


# Construct an empty Stack[int] instance
stack = Stack[int]()
stack.push(2)
print(f'First pop: {stack.pop() + 1}')
stack.push('x')  # error: Argument 1 to "push" of "Stack" has incompatible type "str"; expected "int"

print(f'Second pop: {stack.pop()}')

# A generic function!
def first(seq: Sequence[T]) -> T:
    if len(seq) > 0:
        return seq[0]
    else:
        raise ValueError('Sequence is empty')

reveal_type(first([1, 2, 3]))   # Revealed type is "int"
reveal_type(first('abc'))  # Revealed type is "str"
