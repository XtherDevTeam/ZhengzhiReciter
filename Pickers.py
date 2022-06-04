import random
import time


def RandomPicker(N, Last):
    print('Picker: RandomPicker')
    random.seed(int(time.time()))
    return random.randint(1, N)


def OrderPicker(N, Last):
    print('Picker: OrderPicker')
    if Last == N:
        return 0

    return Last+1
