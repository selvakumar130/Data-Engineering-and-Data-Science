from faker import Faker
from datetime import datetime
import random
import time

# log syntax
LINE = """\
{remote_addr} - - [{time_local} +0000] "{request_type} {request_path} HTTP/1.1" {status} {body_bytes_sent} "{http_referer}" "{http_user_agent}"\
"""
# log file declaration
LOG_FILE_A = "log_a.txt"
LOG_FILE_B = "log_b.txt"
LOG_MAX = 100

# generating log using faker library
def generate_log_line():
    fake = Faker()
    now = datetime.now()
    remote_addr = fake.ipv4()
    time_local = now.strftime('%d/%b/%Y:%H:%M:%S')
    request_type = random.choice(["GET", "POST", "PUT"])
    request_path = "/" + fake.uri_path()

    status = random.choice([200, 401, 404])
    body_bytes_sent = random.choice(range(5, 1000, 1))
    http_referer = fake.uri()
    http_user_agent = fake.user_agent()

    log_line = LINE.format(
        remote_addr=remote_addr,
        time_local=time_local,
        request_type=request_type,
        request_path=request_path,
        status=status,
        body_bytes_sent=body_bytes_sent,
        http_referer=http_referer,
        http_user_agent=http_user_agent
    )

    return log_line

# writing log into log files
def write_log_line(log_file, line):
    with open(log_file, "a") as f:
        f.write(line)
        f.write("\n")

def clear_log_file(log_file):
    with open(log_file, "w+") as f:
        f.write("")

if __name__ == "__main__":
    current_log_file = LOG_FILE_A
    lines_written = 0

    clear_log_file(LOG_FILE_A)
    clear_log_file(LOG_FILE_B)

    while True:
        line = generate_log_line()

        
        write_log_line(current_log_file, line)
        lines_written += 1

        if lines_written % LOG_MAX == 0:
            new_log_file = LOG_FILE_B
            if current_log_file == LOG_FILE_B:
                new_log_file = LOG_FILE_A

            clear_log_file(new_log_file)
            current_log_file = new_log_file

        sleep_time = random.choice(range(1, 5, 1))

        time.sleep(sleep_time)


