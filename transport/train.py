from transport.vehicle import Vehicle

class Train(Vehicle):
    """Класс поезда."""
    
    def __init__(self, capacity: float, number_of_cars: int):
        """
        Создание поезда.
        
        Args:
            capacity: Грузоподъемность в тоннах
            number_of_cars: Количество вагонов (должно быть > 0)
        """
        super().__init__(capacity)
        if not isinstance(number_of_cars, int) or number_of_cars <= 0:
            raise ValueError("Количество вагонов должно быть положительным целым числом")
        self.number_of_cars = number_of_cars
    
    def __str__(self):
        return f"Поезд ({self.number_of_cars} вагонов) - {super().__str__()}"