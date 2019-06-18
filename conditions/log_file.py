import os
import datetime


def create_file(filename):
    return open(filename, 'w')







if __name__ == '__main__':
    current = '{0:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())
    filename = "training_{}".format

