import random


def RandomPicker(N, Last):
    return int(random.random()) % N + 1


def OrderPicker(N, Last):
    if Last == N:
        return 0

    return Last+1
