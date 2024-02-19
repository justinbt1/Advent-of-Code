
def fuel_adder_upper(mass, recursive):
    fuel_amount = mass // 3 - 2

    if not recursive:
        return fuel_amount

    if fuel_amount < 0:
        return 0
    else:
        fuel_amount += fuel_adder_upper(fuel_amount, recursive)
        return fuel_amount


def get_fuel_requirement(module_masses, recursive=False):
    fuel = 0
    for mass in module_masses:
        fuel += fuel_adder_upper(mass, recursive=recursive)

    return fuel


if __name__ == '__main__':
    with open('2019/data/1.txt', 'rt') as file:
        module_masses = [int(line.strip()) for line in file]

    print(get_fuel_requirement(module_masses))
    print(get_fuel_requirement(module_masses, recursive=True))
