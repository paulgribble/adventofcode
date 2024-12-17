import numpy as np

def is_safe(report):
    d_report = np.diff(report)
    return (all(d_report<0) or all(d_report>0)) and (all(abs(d_report)>=1) and all(abs(d_report)<=3))

num_safe = 0
with open("day02_input.txt", 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        report = np.array([int(item) for item in line])
        num_safe += is_safe(report)

print(f"Part 1: {num_safe}")

num_safe = 0
with open("day02_input.txt", 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        report = np.array([int(item) for item in line])
        if is_safe(report):
            num_safe += 1
        else:
            becomes_safe = False
            for level in range(len(report)):
                report_new = np.delete(report, level)
                if is_safe(report_new):
                    becomes_safe = True
            if becomes_safe:
                num_safe += 1

print(f"Part 2: {num_safe}")

