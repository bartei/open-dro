from lib.spi import SpiConnector
import time
import pickle
import redis


spi = SpiConnector()

if __name__ == '__main__':
    while True:
        time.sleep(0.05)
        r = redis.Redis(host='localhost', port=6379, db=0)
        coordinates = spi.read_coordinates()
        print(coordinates)
        r.set('X', coordinates['X'])
        r.set('Y', coordinates['Y'])
        r.set('Z', coordinates['Z'])
        r.set('A', coordinates['A'])
