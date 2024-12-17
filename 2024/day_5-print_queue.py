from itertools import combinations


def read_data():
    page_ordering_rules = set()
    page_numbers = []
    with open('2024/data/5.txt', 'rt') as file:
        for row in file:
            row = row.strip()
            if '|' in row:
                page, rule = row.split('|')
                page_ordering_rules.add((rule, page))
            if ',' in row:
                page_numbers.append([i for i in row.split(',')])

    return page_ordering_rules, page_numbers


def validate_pages(page, rules):
    for p in list(combinations(page, r=2)):
        if p in rules:
            return 0
        
    return int(page[len(page) // 2])


def part_one(pages, rules):
    mid_page_n = 0
    for page in pages:
        mid_page_n += validate_pages(page, rules)
    
    print(mid_page_n)

if __name__ == '__main__':
    rules, updates = read_data()
    part_one(updates, rules)
