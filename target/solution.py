N     = 100000000
STEPS = 1000000
ADD   = 1

#test
#test
#test
#this is temp anyway
#test
def main():
    test = []

    c = 2
    for i in range(1, N):
        c = c**(1+(1/c))
        
        if not i % ADD:
            test.append(c)

        if not i % STEPS:
            print(i, c)
if __name__ == "__main__":
    main()