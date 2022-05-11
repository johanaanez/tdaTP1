import csv
import heapq

from route.antenna import Antenna
from heapq import heappush, heapify


class Route:

    def __init__(self, length):
        self.length = length
        self.antennas = []
        self.necessary_antennas = []
        self.unnecessary_antennas = []

    def add_antenna(self, antenna):
        self.antennas.append(antenna)

    def add_necessary_antennas(self, antenna):
        self.necessary_antennas.append(antenna)

    def remove_antenna(self, antenna):
        self.necessary_antennas.remove(antenna)

    def clean_initial_antennas(self):
        for i in range(len(self.antennas)):
            if self.antennas[i].start < 0 and self.antennas[i + 1].start > 0:
                self.add_necessary_antennas(self.antennas[i])
            elif self.antennas[i].start >= 0:
                self.add_necessary_antennas(self.antennas[i])

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

        antenna = self.necessary_antennas[0]
        heap = []
        heapify(heap)
        heappush(heap, antenna.start)

        for i in range(1, len(self.necessary_antennas)):
            p = heapq.nlargest(1, heap)
            antenna = self.necessary_antennas[i]
            if antenna.start > self.length:
                return heap
            if antenna.start > self.necessary_antennas[-1].end:
                return 0
            if antenna.end > p[0]:
                if i < (len(self.necessary_antennas) - 1) and self.necessary_antennas[i + 1].start <= \
                        self.necessary_antennas[i - 1].end:
                    self.unnecessary_antennas.append(antenna)
                else:
                    heappush(heap, antenna.start)
        return heap
