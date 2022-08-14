def search(timestamp, ids):
    """Return the waiting time * the ID of the earliest bus."""
    wait, id = min(((id - timestamp % id) % id, id) for id in ids)
    return wait * id


if __name__ == '__main__':
    with open('../data/day13.txt') as f:
        timestamp = int(f.readline().strip())
        ids = [int(d) for d in f.readline().strip().split(',') if d.isdigit()]
    print(search(timestamp, ids))
