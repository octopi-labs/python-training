import os
from datetime import datetime

LOGS_DIR = "logs"
MAX_FILE_SIZE = 2 * 1024 * 1024

file_directory = os.path.dirname(__file__)
dir_path = os.path.realpath(os.path.dirname(file_directory))


def get_sorted_file_list(directory, desc=True):
    files = os.listdir(directory)
    if files:
        files = [os.path.join(directory, item) for item in files if os.path.isfile(os.path.join(directory, item))]
        files.sort(key=lambda item: os.path.getctime(item), reverse=desc)
    return files

def generate_filename(initial="assignment"):
    current_datetime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "{initial}_{timestamp}.log".format(initial=initial, timestamp=current_datetime)

def create_log_file(directory):
    filename = generate_filename()
    filename = os.path.join(directory, filename)
    log_file = open(filename, mode='w', encoding='utf-8')
    log_file.close()
    return filename


def write_to_logs(log_type, message):
    # 1. Get a list of all log files in descending order of creation time
    files = None
    log_directory = os.path.join(dir_path, LOGS_DIR)
    # Check if log directory exists
    if os.path.exists(log_directory) and os.path.isdir(log_directory):
        # If exists, get list of file in sorted by descending order of creation.
        files = get_sorted_file_list(log_directory)
    else:
        # if not create it
        log_dir_parent = os.path.dirname(log_directory)
        log_directory = os.path.join(log_dir_parent, LOGS_DIR)
        os.mkdir(log_directory)

    # 2. Get the top most file and check it's size or create one if no file is present
    current_log = files[0] if files else create_log_file(log_directory)

    # 3. if the filesize is greater than 2 MB, create new file with current timestamp. Go to step 5
    if os.path.getsize(current_log) >= MAX_FILE_SIZE:
        current_log = create_log_file(log_directory)

    # 4. If the filesize is less than 2 MB, go to step 5.
    # 5. Write to the file
    with open(current_log, mode='a', encoding='utf-8') as log_file:
        current_datetime = datetime.now().strftime("%b %d, %Y %-I:%M:%S %p")
        log = "{0}: {1} {2}\n".format(log_type, current_datetime, message)
        log_file.write(log)


if __name__ == "__main__":
    write_to_logs("INFO", "This is it.")
