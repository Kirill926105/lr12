import uuid

class Vehicle:
    
    def __init__(self, capacity: float):
        """
        Создание транспортного средства.
        
        Args:
            capacity: Грузоподъемность в тоннах (должна быть > 0)
        """
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Грузоподъемность должна быть положительным числом")
        
        self.vehicle_id = str(uuid.uuid4())[:8]
        self.capacity = float(capacity)
        self.current_load = 0.0
        self.clients_list = []
    
    def load_cargo(self, client):
        """
        Загрузка груза клиента.
        
        Args:
            client: Объект класса Client
            
        Returns:
            True - если груз загружен, False - если не хватает места
            
        Raises:
            TypeError: Если передан не Client
        """
        from transport.client import Client
        if not isinstance(client, Client):
            raise TypeError("Можно загружать только объекты класса Client")
        
        if self.current_load + client.cargo_weight > self.capacity:
            return False
        
        self.current_load += client.cargo_weight
        self.clients_list.append(client)
        return True
    
    def unload_all(self):
        """Полная разгрузка транспорта."""
        self.current_load = 0.0
        self.clients_list.clear()
    
    def get_free_capacity(self):
        """Возвращает свободную грузоподъемность."""
        return self.capacity - self.current_load
    
    def __str__(self):
        return f"Транспорт ID: {self.vehicle_id}, Грузоподъемность: {self.capacity}т, " \
               f"Загружено: {self.current_load}т, Свободно: {self.get_free_capacity()}т"