from transport.vehicle import Vehicle
from transport.client import Client

class TransportCompany:
    """Класс транспортной компании."""
    
    def __init__(self, name: str):
        """
        Создание транспортной компании.
        
        Args:
            name: Название компании (непустая строка)
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название компании должно быть непустой строкой")
        self.name = name.strip()
        self.vehicles = []
        self.clients = []
    
    def add_vehicle(self, vehicle):
        """
        Добавление транспортного средства.
        
        Args:
            vehicle: Объект Vehicle или его наследник
            
        Raises:
            TypeError: Если передан не транспорт
        """
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Можно добавлять только транспортные средства")
        self.vehicles.append(vehicle)
    
    def list_vehicles(self):
        """Возвращает список всех транспортных средств."""
        return self.vehicles.copy()
    
    def add_client(self, client):
        """
        Добавление клиента.
        
        Args:
            client: Объект Client
            
        Raises:
            TypeError: Если передан не клиент
        """
        if not isinstance(client, Client):
            raise TypeError("Можно добавлять только клиентов")
        self.clients.append(client)
    
    def optimize_cargo_distribution(self):
        """
        Оптимизирует распределение грузов по транспорту.
        
        Returns:
            dict: Результаты распределения
        """
        # Разгружаем весь транспорт
        for v in self.vehicles:
            v.unload_all()
        
        # Сортируем: VIP вперед, тяжелые грузы вперед
        sorted_clients = sorted(self.clients, 
                               key=lambda c: (not c.is_vip, -c.cargo_weight))
        
        # Сортируем транспорт: большая грузоподъемность вперед
        sorted_vehicles = sorted(self.vehicles, 
                                key=lambda v: v.capacity, 
                                reverse=True)
        
        distributed = []
        not_distributed = []
        
        # Распределяем грузы
        for client in sorted_clients:
            loaded = False
            for vehicle in sorted_vehicles:
                if vehicle.get_free_capacity() >= client.cargo_weight:
                    if vehicle.load_cargo(client):
                        distributed.append((client, vehicle))
                        loaded = True
                        break
            if not loaded:
                not_distributed.append(client)
        
        return {
            "distributed": distributed,
            "not_distributed": not_distributed,
            "used_vehicles": sum(1 for v in self.vehicles if v.current_load > 0)
        }
    
    def __str__(self):
        return f"Компания: '{self.name}', Транспорт: {len(self.vehicles)}, Клиенты: {len(self.clients)}"