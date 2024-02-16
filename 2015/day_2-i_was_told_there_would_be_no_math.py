def calculate_wrapping(dimensions):
    paper_area = 0
    for dim in dimensions:
        l, w, h = dim
        sides = (l * w, w * h, h * l)
        slack = min(sides)
        paper_area += sum(sides) * 2 + slack

    print(paper_area)

def calculate_ribbon(dimensions):
    ribbon_length = 0
    for dim in dimensions:
        dim = sorted(dim)
        perimiter = 2 * (dim[0] + dim[1])
        volume = dim[0] * dim[1] * dim[2]
        ribbon_length += perimiter + volume

    print(ribbon_length)

if __name__ == '__main__':
    with open('2015/data/2.txt', 'rt') as dim_file:
        dimensions = [
            tuple(int(dim) for dim in line.strip().split('x')) for line in dim_file
        ]
        
        calculate_wrapping(dimensions)
        calculate_ribbon(dimensions)
