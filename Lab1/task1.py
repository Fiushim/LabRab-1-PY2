from abc import ABC, abstractmethod
from typing import Any

class Table(ABC):
    """
    Абстрактный класс для описания стола.

    Атрибуты:
        material (str): Материал стола.
        legs (int): Количество ножек у стола.
        color (str): Цвет стола.
    """

    def __init__(self, material: str, legs: int, color: str):
        # Проверяем, что количество ножек больше нуля.
        if legs <= 0:
            raise ValueError("Количество ножек должно быть больше нуля.")

        # Инициализируем атрибуты.
        self.material = material
        self.legs = legs
        self.color = color

    @abstractmethod
    def fold(self) -> None:
        """
        Складывает стол, если он складной.
        """
        ...

    @abstractmethod
    def paint(self, color: str) -> None:
        """
        Красит стол в заданный цвет.

        Args:
            color (str): Новый цвет стола.
        """
        ...

    @abstractmethod
    def measure(self) -> tuple[float, float]:
        """
        Измеряет размеры стола.

        Returns:
            tuple[float, float]: Ширина и длина стола.
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс для описания дерева.

    Атрибуты:
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
        species (str): Вид дерева.
    """

    def __init__(self, height: float, age: int, species: str):
        # Проверяем, что высота положительная.
        if height <= 0:
            raise ValueError("Высота должна быть положительной.")
        # Проверяем, что возраст не отрицательный.
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        # Инициализируем атрибуты.
        self.height = height
        self.age = age
        self.species = species

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Запускает процесс фотосинтеза.
        """
        ...

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева.

        Args:
            years (int): Количество лет роста.
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Процесс сбрасывания листьев.
        """
        ...


class Stack(ABC):
    """
    Абстрактный класс для описания стека (абстрактного типа данных).

    Атрибуты:
        max_size (int): Максимальный размер стека.
    """

    def __init__(self, max_size: int):
        # Проверяем, что максимальный размер больше нуля.
        if max_size <= 0:
            raise ValueError("Максимальный размер должен быть больше нуля.")

        # Инициализируем атрибут.
        self.max_size = max_size

    @abstractmethod
    def push(self, item: Any) -> None:
        """
        Добавляет элемент в стек.

        Args:
            item (Any): Элемент, который нужно добавить.

        Raises:
            OverflowError: Если стек переполнен.

        Doctest:
        >>> stack = StackImplementation(3)
        >>> stack.push(42)
        """
        ...

    @abstractmethod
    def pop(self) -> Any:
        """
        Удаляет и возвращает верхний элемент стека.

        Returns:
            Any: Верхний элемент стека.

        Raises:
            IndexError: Если стек пуст.

        Doctest:
        >>> stack = StackImplementation(3)
        >>> stack.push(42)
        >>> stack.pop()
        42
        """
        ...

    @abstractmethod
    def peek(self) -> Any:
        """
        Возвращает верхний элемент стека без удаления.

        Returns:
            Any: Верхний элемент стека.

        Raises:
            IndexError: Если стек пуст.

        Doctest:
        >>> stack = StackImplementation(3)
        >>> stack.push(42)
        >>> stack.peek()
        42
        """
        ...

class StackImplementation(Stack):
    def __init__(self, max_size: int):
        super().__init__(max_size)
        self._data = []

    def push(self, item):
        if len(self._data) >= self.max_size:
            raise OverflowError("Стек переполнен.")
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Стек пуст.")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("Стек пуст.")
        return self._data[-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()