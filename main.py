import transport

company = transport.TransportCompany("MyCompany")

menu = """
1. создать клиента
2. создать самолет
3. создать поезд
4. вывести всех клиентов
5. вывести весь транспорт
6. оптимизировать клиентов и транспорт
7. выход
"""

def select_action():
    try:
        return int(input("выберите действие: "))
    except:
        return None


while True:
    print(menu)
    action = select_action()

    if action is None:
        print("некорректный ввод.")
        continue

    match action:
        case 1:
            name = input("имя клиента: ")
            weight = float(input("вес груза (тонны): "))
            vip = input("vip клиент? (y/n): ").lower() == "y"

            client = transport.Client(name, weight, vip)
            company.add_client(client)
            print(f"клиент '{name}' добавлен.")

        case 2:
            capacity = float(input("грузоподъемность самолета (тонны): "))
            altitude = float(input("максимальная высота (метры): "))

            airplane = transport.Airplane(capacity, altitude)
            company.add_vehicle(airplane)
            print(f"самолет id {airplane.vehicle_id} добавлен.")

        case 3:
            capacity = float(input("грузоподъемность поезда (тонны): "))
            cars = int(input("количество вагонов: "))

            train = transport.Train(capacity, cars)
            company.add_vehicle(train)
            print(f"поезд id {train.vehicle_id} добавлен.")

        case 4:
            print("\n--- клиенты ---")
            if company.clients:
                for c in company.clients:
                    print(f"  {c}")
            else:
                print("  клиентов нет")
            print(f"\nвсего клиентов: {len(company.clients)}")

        case 5:
            print("\n--- транспорт ---")
            if company.vehicles:
                for v in company.vehicles:
                    print(f"  {v}")
            else:
                print("  транспорта нет")
            print(f"\nвсего транспорта: {len(company.vehicles)}")

        case 6:
            print("\nоптимизация распределения грузов...")
            
            if not company.clients:
                print("нет клиентов для распределения!")
                continue
            if not company.vehicles:
                print("нет транспорта для распределения!")
                continue
            
            results = company.optimize_cargo_distribution()
            
            print(f"\nклиентов распределено: {len(results['distributed'])}/{len(company.clients)}")
            print(f"транспорта использовано: {results['used_vehicles']}/{len(company.vehicles)}")
            
            if results['not_distributed']:
                print(f"не распределено: {len(results['not_distributed'])} клиентов")

        case 7:
            print("выход.")
            break

        case _:
            print("некорректное действие.")