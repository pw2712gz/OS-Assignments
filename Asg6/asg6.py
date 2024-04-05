# Ayub Yusuf
# Disk Scheduling Program
# Implements FCFS, SSTF, SCAN, C-SCAN, LOOK, and C-LOOK algorithms

def fcfs(start, requests):
    """First-Come, First-Served algorithm."""
    movement = 0
    current_position = start
    for request in requests:
        movement += abs(request - current_position)
        current_position = request
    return movement


def sstf(start, requests):
    """Shortest Seek Time First algorithm."""
    movement = 0
    current_position = start
    local_requests = requests[:]
    while local_requests:
        closest_request = min(local_requests, key=lambda x: abs(x - current_position))
        movement += abs(closest_request - current_position)
        current_position = closest_request
        local_requests.remove(closest_request)
    return movement


def scan(start, requests, cylinders):
    """SCAN algorithm."""
    movement = 0
    current_position = start
    requests.sort()
    if current_position <= requests[0]:
        movement = requests[-1] - current_position
    elif current_position >= requests[-1]:
        movement = current_position - requests[0]
    else:
        movement = max(current_position - requests[0], requests[-1] - current_position) + (requests[-1] - requests[0])
    return movement


def c_scan(start, requests, cylinders):
    """C-SCAN algorithm."""
    movement = 0
    current_position = start
    requests.sort()
    if current_position <= requests[0] or current_position >= requests[-1]:
        movement = requests[-1] - requests[0]
    else:
        movement = (cylinders - current_position) + (cylinders - requests[0]) + (requests[-1] - 0)
    return movement


def look(start, requests, cylinders):
    """LOOK algorithm."""
    return scan(start, requests, cylinders)


def c_look(start, requests, cylinders):
    """C-LOOK algorithm."""
    movement = 0
    current_position = start
    requests.sort()
    if current_position <= requests[0] or current_position >= requests[-1]:
        movement = requests[-1] - requests[0]
    else:
        movement = max(current_position - requests[0], requests[-1] - current_position) + (requests[-1] - requests[0])
    return movement


def read_data(filename):
    """Reads the disk scheduling data from a file."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = []
        i = 0
        while i < len(lines):
            cylinders = int(lines[i].strip())
            start = int(lines[i + 1].strip())
            requests = list(map(int, lines[i + 2].strip().split()))
            data.append((cylinders, start, requests))
            i += 3
        return data


def main():
    filename = 'Asg6 Data.txt'  # Path to the data file
    data = read_data(filename)

    print("Ayub Yusuf, 4.4.2024, Assignment 6.")
    # Process and print results for each data set
    for i, (cylinders, start, requests) in enumerate(data, 1):
        print(f"For FCFS, the total head movement was {fcfs(start, requests)} cylinders.")
        print(f"For SSTF, the total head movement was {sstf(start, requests)} cylinders.")
        print(f"For SCAN, the total head movement was {scan(start, requests, cylinders)} cylinders.")
        print(f"For CSCAN, the total head movement was {c_scan(start, requests, cylinders)} cylinders.")
        print(f"For LOOK, the total head movement was {look(start, requests, cylinders)} cylinders.")
        print(f"For CLOOK, the total head movement was {c_look(start, requests, cylinders)} cylinders.\n")


if __name__ == "__main__":
    main()
