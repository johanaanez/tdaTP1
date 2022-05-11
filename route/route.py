import csv
import heapq

from route.antenna import Antenna
from heapq import heappush, heapify


class Route:

    def __init__(self, length):
        self.length = length
        self.antennas = []

    def add_antenna(self, antenna):
        self.antennas.append(antenna)

    def remove_antenna(self, antenna):
        self.necessary_antennas.remove(antenna)

    def clean_initial_antennas(self):
        necessary_antennas = []
        for i in range(len(self.antennas)):
            if self.antennas[i].start < 0 and self.antennas[i + 1].start > 0:
                necessary_antennas.append(self.antennas[i])
            elif self.antennas[i].start >= 0:
                necessary_antennas.append(self.antennas[i])
        self.antennas = necessary_antennas.copy()

    def order_by_start(self):
        self.antennas.sort(key=lambda x: x.start)

    def add_antennas(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                antenna = Antenna(int(row[0]), int(row[1]), int(row[2]))
                self.add_antenna(antenna)

        file.close()

    def get_minimun_antennas(self):
        self.order_by_start()
        self.clean_initial_antennas()

        antenna = self.antennas[0]
        necessary_antennas = [antenna.id]
        unnecessary_antennas = []
        heap = []
        heapify(heap)
        heappush(heap, antenna.start)

        for i in range(1, len(self.antennas)):
            p = heapq.nlargest(1, heap)
            antenna = self.antennas[i]
            if antenna.start > self.antennas[-1].end:
                return 0
            if antenna.start > self.length:
                return necessary_antennas
            if antenna.end > p[0]:
                if i < (len(self.antennas) - 1) and self.antennas[i + 1].start <= \
                        self.antennas[i - 1].end:
                    unnecessary_antennas.append(antenna.id)
                else:
                    heappush(heap, antenna.start)
                    necessary_antennas.append(antenna.id)
        return necessary_antennas
