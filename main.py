# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from route.route import Route
import argparse

def main():
    usage_options = "%(prog)s [-v] [-f] "

    parser = argparse.ArgumentParser(
        usage=usage_options,
        description="<command description>"
    )

    parser.add_argument("-k", "--len")
    parser.add_argument("-f", "--file")

    params = parser.parse_args()
    file = params.file
    k = int(params.len)

    route = Route(k)
    route.add_antennas(file)
    route.get_minimun_antennas()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
