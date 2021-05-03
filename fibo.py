def recursive_nth_fibo(nth):
    if nth <= 1:
        return nth
    else:
        fibo = recursive_nth_fibo(nth-1) + recursive_nth_fibo(nth-2)
        return fibo


def main():
    nth = int(input("prvok: "))
    fib_seq = [recursive_nth_fibo(n) for n in range(nth)]

    print(fib_seq)


if __name__ == '__main__':
    main()
