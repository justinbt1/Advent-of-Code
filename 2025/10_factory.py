

def load_data():
    with open('2025/data/10.txt', 'rt') as tachyon_buffer:
        machines = []
        for row in tachyon_buffer:
            row = row.strip().split()
            indicators = [1 if i == '#' else 0 for i in row[0][1:-1]]
            buttons = [[int(i) for i in array[1:-1].split(',')] for array in row[1:-1]]
            joltage = row[-1]
            machine = {'indicator': indicators, 'buttons': buttons, 'joltage': joltage}
            machines.append(machine)
 
    return machines


def check_activation(lights, indicator):
    for light in lights:
        if light == indicator:
            return True


def part_one(machine_data):
    presses = 0
    for row in machine_data:
        lights = [[0] * len(row['indicator'])]
        while True:
            presses += 1
            activations = []
            for toggle in row['buttons']:
                for light in lights:
                    light = light.copy()
                    for i in toggle:
                        light[i] = 1 - light[i]
                    if light not in activations:
                        activations.append(light)

            if check_activation(activations, row['indicator']):
                break

            lights = activations

    print(presses)


if __name__ == '__main__':
    data = load_data()
    part_one(data)
