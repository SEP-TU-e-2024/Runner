import psutil
import sys
import datetime

STDOUT_LOG = 'logs/stdout.txt'

def main(argv):
    if len(argv) < 2:
        return

    with open(STDOUT_LOG, '+a') as f:
        f.write(f'Time: {datetime.datetime.now()}\tArguments: {argv[1:]}\n')
        process = psutil.Popen(argv[1:], stdout=f)

    with process.oneshot():
        print(process.name())
        print(process.pid)
        print(process.parent().name())
        print(process.memory_full_info())

    print(process.wait())

if __name__ == "__main__":
    main(sys.argv)