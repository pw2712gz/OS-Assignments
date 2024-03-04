
def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data_sets = []
        for i in range(0, len(lines), 3):
            n_cylinders = int(lines[i].strip())
            start_pos = int(lines[i + 1].strip())
            requests = list(map(int, lines[i + 2].strip().split(',')))
            data_sets.append((n_cylinders, start_pos, requests))
    return data_sets

def FCFS(requests, start_pos):
    head_movement = 0
    current_pos = start_pos
    for req in requests:
        head_movement += abs(req - current_pos)
        current_pos = req
    return head_movement

def SSTF(requests, start_pos):
    head_movement = 0
    current_pos = start_pos
    unvisited = requests.copy()

    while unvisited:
        closest = min(unvisited, key=lambda x: abs(x - current_pos))
        head_movement += abs(closest - current_pos)
        current_pos = closest
        unvisited.remove(closest)

    return head_movement

def SCAN(requests, start_pos, n_cylinders):
    head_movement = 0
    direction = 1  # Assume initially moving towards higher cylinder numbers
    current_pos = start_pos
    requests.sort()
    
    while requests:
        next_request = None
        for request in requests:
            if direction == 1 and request >= current_pos or direction == -1 and request <= current_pos:
                next_request = request
                break
        
        if next_request is not None:
            head_movement += abs(next_request - current_pos)
            current_pos = next_request
            requests.remove(next_request)
        else:
            # Change direction at the end of the disk
            if direction == 1:
                head_movement += abs(n_cylinders - 1 - current_pos)
                current_pos = n_cylinders - 1
            else:
                head_movement += abs(0 - current_pos)
                current_pos = 0
            direction *= -1

    return head_movement

def C_SCAN(requests, start_pos, n_cylinders):
    head_movement = 0
    current_pos = start_pos
    requests.sort()
    
    # Move towards the end, then jump to the beginning
    for request in requests:
        if request >= current_pos:
            head_movement += abs(request - current_pos)
            current_pos = request

    # If we haven't reached the end, add the movement to the end and then to the start
    if current_pos != n_cylinders - 1:
        head_movement += abs(n_cylinders - 1 - current_pos)  # to the end
        head_movement += n_cylinders - 1  # to the start
        current_pos = 0

    for request in requests:
        if request < start_pos:
            head_movement += abs(request - current_pos)
            current_pos = request

    return head_movement

def LOOK(requests, start_pos):
    head_movement = 0
    direction = 1  # Assume initially moving towards higher cylinder numbers
    current_pos = start_pos
    requests.sort()
    
    while requests:
        next_request = None
        for request in requests:
            if direction == 1 and request >= current_pos or direction == -1 and request <= current_pos:
                next_request = request
                break
        
        if next_request is not None:
            head_movement += abs(next_request - current_pos)
            current_pos = next_request
            requests.remove(next_request)
        else:
            # Change direction when no further requests in the current direction
            direction *= -1

    return head_movement

def C_LOOK(requests, start_pos):
    head_movement = 0
    current_pos = start_pos
    requests.sort()
    
    # First move towards the highest request
    for request in requests:
        if request >= current_pos:
            head_movement += abs(request - current_pos)
            current_pos = request

    # Then jump to the lowest request and move upwards again
    lowest_requests = [request for request in requests if request < start_pos]
    if lowest_requests:
        head_movement += abs(current_pos - min(lowest_requests))
        current_pos = min(lowest_requests)

        for request in sorted(lowest_requests):
            head_movement += abs(request - current_pos)
            current_pos = request

    return head_movement

def main():
    filename = "/Users/ayubyusuf/Desktop/OS/OS-Assignments/Asg6/Asg6Data.txt"
    data_sets = read_data(filename)
    
    for i, (n_cylinders, start_pos, requests) in enumerate(data_sets, 1):
        print(f"Data Set {i}:")
        print(f"For FCFS, the total head movement was {FCFS(requests, start_pos)} cylinders.")
        print(f"For SSTF, the total head movement was {SSTF(requests, start_pos)} cylinders.")
        print(f"For SCAN, the total head movement was {SCAN(requests, start_pos, n_cylinders)} cylinders.")
        print(f"For C-SCAN, the total head movement was {C_SCAN(requests, start_pos, n_cylinders)} cylinders.")
        print(f"For LOOK, the total head movement was {LOOK(requests, start_pos)} cylinders.")
        print(f"For C-LOOK, the total head movement was {C_LOOK(requests, start_pos)} cylinders.")
        print()

if __name__ == "__main__":
    main()
