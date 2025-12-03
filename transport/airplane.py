from transport.vehicle import Vehicle

class Airplane(Vehicle):
    """Класс самолета."""
    
    def __init__(self, capacity: float, max_altitude: float):
        """
        Создание самолета.
        
        Args:
            capacity: Грузоподъемность в тоннах
            max_altitude: Максимальная высота полета в метрах (должна быть > 0)
        """
        super().__init__(capacity)
        if not isinstance(max_altitude, (int, float)) or max_altitude <= 0:
            raise ValueError("Максимальная высота должна быть положительным числом")
        self.max_altitude = float(max_altitude)
    
    def __str__(self):
        return f"Самолет (высота: {self.max_altitude}м) - {super().__str__()}"