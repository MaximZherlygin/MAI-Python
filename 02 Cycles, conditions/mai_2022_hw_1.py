drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced",
              "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus",
              "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s",
              "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

# в drone по очереди попадает каждый дрон из списка drone_list
for drone in drone_list:
    print(drone)

# TODO1
# выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество.
# учтите, что:
# 1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
# 2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel
provider_names = {
    'dji': 'DJI',
    'autel': 'Autel',
    'parrot': 'Parrot',
    'ryze': 'Ryze',
    'eachine': 'Eachine'
}
splitted_drones = list()
for drone in drone_list:
    splitted_drones.append(drone.split(' '))

print('------------------------------')
print('Input drone provider: ', end='')
input_drone = str(input())
filtered_drones = [drone for drone in splitted_drones if drone[0].lower() == input_drone.lower()]
for drone in filtered_drones:
    print(f'{provider_names[drone[0].lower()]} {" ".join(drone[1:])}')
print('------------------------------')


# TODO2
# подсчитайте количество моделей дронов каждого производителя из списка drone_list.
# производители: DJI, Autel, Parrot, Ryze, Eachine
drones_dict = {
    'dji': [],
    'autel': [],
    'parrot': [],
    'ryze': [],
    'eachine': []
}
for drone in drone_list:
    current_drone = drone.split(' ')
    provider = current_drone[0].lower()
    drones_dict[provider].append(current_drone[1:])

for item in drones_dict:
    print(f'Amount of drones for provider {provider_names[item]} is {len(drones_dict[item])}')

# TODO3
# выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество.
# сделайте то же самое для всех дронов, которые не нужно регистрировать
# для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
# как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

register = []
not_register = []
for drone, weight in zip(drone_list, drone_weight_list):
    current_drone = drone.split(' ')
    current_drone[0] = current_drone[0].lower()
    if weight > 150:
        register.append(current_drone)
    else:
        not_register.append(current_drone)

print('Drones to be registered:')
for drone in register:
    print(f'{provider_names[drone[0]]} {" ".join(drone[1:])}')

print('Drones that do not need to be registered:')
for drone in not_register:
    print(f'{provider_names[drone[0]]} {" ".join(drone[1:])}')

# TODO4
# для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
# высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
# помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

agreement = []
for drone, weight in zip(drone_list, drone_weight_list):
    current_drone = drone.split(' ')
    current_drone[0] = current_drone[0].lower()
    if weight > 150:
        agreement.append((current_drone, 'YES'))
    else:
        agreement.append((current_drone, 'NO'))

print('Drone must be approved:')
for item in agreement:
    print(f'{provider_names[item[0][0]]} {" ".join(item[0][1:])}: {item[1]}')

# TODO5*
# модифицируйте решение задания TODO1:
# теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей
# и БЕЗ названия производителя.
# например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano,
# Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно
# несколькими разными способами
# производители те же: DJI, Autel, Parrot, Ryze, Eachine
splitted_drones = list()
for drone in drone_list:
    splitted_drones.append(drone.split(' '))

print('-----------------------------')
print('Input drone provider: ', end='')
input_drone = str(input())
filtered_drones = [drone[1:] for drone in splitted_drones if drone[0].lower() == input_drone.lower()]
str_drones = [' '.join(drone) for drone in filtered_drones]
print(', '.join(str_drones))
print('-----------------------------')
