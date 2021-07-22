import spidev
import struct


class SpiConnector:
    spi = None

    def __init__(self):
        self.spi = spidev.SpiDev(0, 0)
        self.spi.max_speed_hz = 500000
        self.spi.open(0, 0)

    def read_coordinates(self):
        send_buffer = bytearray(32)
        receive_buffer = self.spi.xfer(send_buffer)
        x, y, z, a = struct.unpack("qqqq", bytearray(receive_buffer))

        return {
            'X': x,
            'Y': y,
            'Z': z,
            'A': a,
        }
