import time
import pigpio
from lib.spi import SpiConnector
import time
import redis

spi = SpiConnector()
pi = pigpio.pi()
bit_map = {
    0: (0, 0),
    1: (1, 0),
    2: (1, 1),
    3: (0, 1),
}


if __name__ == '__main__':
    period = 2000
    step = 1
    x =  0
    start = spi.read_coordinates()
    print(f"Start: {start}")

    while True:
        pi.write(5, bit_map[x % 4][0])
        time.sleep(1/period)
        pi.write(6, bit_map[x % 4][1])
        time.sleep(1/period)

        x += step

        if x > 100:
            step = -1
            time.sleep(1)
            coordinates = spi.read_coordinates()
            print(f"at 100: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 100: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 100: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 100: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 100: {coordinates}")

        if x < 0:
            step = +1
            time.sleep(1)
            coordinates = spi.read_coordinates()
            print(f"at 0: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 0: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 0: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 0: {coordinates}")
            coordinates = spi.read_coordinates()
            print(f"at 0: {coordinates}")
