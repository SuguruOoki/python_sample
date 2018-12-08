#-*- using:utf-8 -*-
import time

def kadai1(max_number):
    fizzbuzz_list = []
    for n in range(1, max_number + 1):
        if n % 3 == 0 and n % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif n % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif n % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(n)

    return fizzbuzz_list

def kadai2(max_number):
    counter = 0
    primes = [2, 3]

    for n in range(5, max_number + 1, 2):
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if primes[i] ** 2 > n:
                break
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)

    return primes

def kadai3(max_number):
    counter = 0
    primes = [2, 3]
    l = len

    for n in range(5, max_number + 1, 2):
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if primes[i] ** 2 > n:
                break
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)

    return primes[-1], len(primes)


if __name__ == '__main__':
    kadai12_max_number = 100
    kadai3_max_number = 1000000

    # 課題１
    print("課題１！--------------------------")
    print("{}までのFizzBuzzを表示する".format(str(kadai12_max_number)))
    fizzbuzz_list = kadai1(kadai12_max_number)
    print(fizzbuzz_list)

    # 課題２
    print("課題２！--------------------------")
    print("{}までの素数を求める".format(str(kadai12_max_number)))
    prime_list = kadai2(kadai12_max_number)
    print(prime_list)

    # 課題３
    print("課題３！--------------------------")
    print("{}までの素数の個数と最大値を求める".format(str(kadai12_max_number)))
    start = time.time()
    prime_max, prime_count = kadai3(kadai3_max_number)
    print('{}までの素数において'.format(str(kadai3_max_number)))
    print('素数の最大値:{}'.format(str(prime_max)))
    print('素数の数:{}'.format(str(prime_count)))
    elapse = time.time() - start
    print('課題３の実行時間:{}'.format(str(elapse)))
