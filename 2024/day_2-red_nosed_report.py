def check_report(report):
    direction = (report[0] - report[1]) > 0
    for i in range(0, len(report) - 1):
        diff = report[i] - report[i + 1]
        if not (diff > 0) is direction or abs(diff) > 3 or abs(diff) == 0:
            return 0
        
    return 1


def safety_check(reports, dampner=False):
    safe_reports = 0
    for report in reports:
        result = check_report(report, dampner)
        if result == 0 and dampner:
            for j in range(0, len(report)):
                if check_report(report[:j] + report[j + 1:]):
                    result = 1
                    break
        
        safe_reports += result

    print(safe_reports)        


if __name__ == '__main__':
    reports = []
    with open('2024/data/2.txt') as file:
        for row in file:
            reports.append([int(level) for level in row.split()])

    safety_check(reports)
    safety_check(reports, dampner=True)
