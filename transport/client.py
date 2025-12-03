class Client:
    
    def __init__(self, name: str, cargo_weight: float, is_vip: bool = False):
        """
        Создание клиента.
        
        Args:
            name: Имя клиента (непустая строка)
            cargo_weight: Вес груза в тоннах (должен быть > 0)
            is_vip: VIP статус (по умолчанию False)
        """
        # ВАЛИДАЦИЯ
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя клиента должно быть непустой строкой")
        if not isinstance(cargo_weight, (int, float)) or cargo_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом")
        if not isinstance(is_vip, bool):
            raise ValueError("VIP статус должен быть True или False")
        
        self.name = name.strip()
        self.cargo_weight = float(cargo_weight)
        self.is_vip = is_vip
    
    def __str__(self):
        vip = "VIP" if self.is_vip else "обычный"
        return f"Клиент: {self.name}, Груз: {self.cargo_weight}т, Статус: {vip}"