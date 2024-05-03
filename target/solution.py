N = 10000000
STEPS = 100000


def main():
    c = 2
    for i in range(1, N):
        c = c**(1+(1/c))

        if not i % STEPS:
            print(i, c)
if __name__ == "__main__":
    main()