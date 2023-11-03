class InsufficientFounds(Exception):
    def __init__(self, amount: float, client) -> None:
        super().__init__(f'{client.name} could not pay {amount}')

class Position:
    def __init__(self, x: float = 0., y: float = 0.) -> None:
        self._x, self.__y = x, y

    @property
    def x(self) -> float:
        return self.__x
    
    @x.setter
    def x(self, new_x: float) -> None:
        if not isinstance(new_x, float):
            raise TypeError(f'position should be float, not {type(new_x).__name__}')
        self.__x = new_x
    
    @property
    def y(self) -> float:
        return self.__y
    
    @y.setter
    def y(self, new_y: float) -> None:
        if not isinstance(new_y, float):
            raise TypeError(f'position should be float, not {type(new_y).__name__}')
        self.__y = new_y
    
    @property
    def position(self) -> tuple[float]:
        return self.__x, self.__y
    
    @position.setter
    def position(self, x: float, y: float) -> None:
        self.x, self.y = x, y
def distance(self, other: Self)->float:
    x_delta, y_delta = abs(self.x - other.x), abs(self.y - other.y)
    shortest = (x_delta ** 2 + y_delta ** 2)** .5
    random_length = random.uniform(shortest, x_delta+ y_delta)