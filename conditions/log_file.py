import os
import datetime
import ex31


def create_file(filename):
    return open(filename, 'w')






print("Inside log_file:", __name__)
if __name__ == '__main__':
    current = '{0:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())
    filename = "training_{}".format(current)
    print(filename)
