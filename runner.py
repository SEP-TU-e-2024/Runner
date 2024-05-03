import psutil
import sys
import datetime
import time

STDOUT_LOG = 'logs/stdout.txt'
RETRIEVAL_INTERVAL = 0.1

def get_details(process: psutil.Process):
    with process.oneshot():
        print(process.cpu_percent())
        print(process.memory_full_info())


def main(argv: list[str]):
    if len(argv) < 2:
        return
    
    start_wall_time = time.time()

    with open(STDOUT_LOG, '+a') as f:
        f.write(f'Time: {datetime.datetime.now()}\tArguments: {argv[1:]}\n')
        process = psutil.Popen(argv[1:], stdout=f)

    with process.oneshot():
        print(f"Name: {process.name()}\tId: {process.pid}")

    while process.poll() == None:
        get_details(process)
        time.sleep(RETRIEVAL_INTERVAL)

    print(process.wait())
    print(f"Rough wall time: {time.time() - start_wall_time}")

if __name__ == "__main__":
    main(sys.argv)