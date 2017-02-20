"""Lab 2: Higher Order Functions & Lambdas"""
from utils import letter_to_num, num_to_letter, looper, mirror_letter

def make_derivative(f, h=1e-5):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> square = lambda x: x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    def f_d(a):
        return (f(a+h)-f(a))/h
    return f_d


# String Transformers

from operator import add, sub

def caesar_generator(num, op):
    """Returns a one-argument Caesar cipher function. The function should "rotate" a
    letter by an integer amount 'num' using an operation 'op' (either add or
    sub).

    You may use the provided `letter_to_num` and `num_to_letter` functions,
    which will map all lowercase letters a-z to 0-25 and all uppercase letters
    A-Z to 26-51.

    >>> letter_to_num('a')
    0
    >>> letter_to_num('c')
    2
    >>> num_to_letter(3)
    'd'

    >>> caesar2 = caesar_generator(2, add)
    >>> caesar2('a')
    'c'
    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus3('d')
    'a'
    """
    a = lambda x: num_to_letter(op(letter_to_num(x), num))
    return a


# Encryption and Decryption

def make_encrypter(f1, f2, f3):
    """Generates an "encrypter" that applies a specific set of encryption
    functions on the message

    >>> caesar3 = caesar_generator(3, add)
    >>> caesar2 = caesar_generator(2, add)
    >>> encrypter = make_encrypter(caesar2, mirror_letter, caesar3)
    >>> encrypter('abcd') # caesar2(mirror_letter(caesar3('a'))) -> 'y'
    'yxwv'
    """
    f1, f2, f3 = looper(f1), looper(f2), looper(f3)
    def encrypter(x):
        return f1(f2(f3(x)))
    return encrypter

def make_decrypter(f1, f2, f3):
    """Generates a "decrypter" function.

    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus2 = caesar_generator(2, sub)
    >>> decrypter = make_decrypter(brutus2, mirror_letter, brutus3)
    >>> decrypter('yxwv') # brutus3(mirror_letter(brutus2('y'))) = 'a'
    'abcd'
    """
    f1, f2, f3 = looper(f1), looper(f2), looper(f3)
    def decrypter(x):
        return f3(f2(f1(x)))
    return decrypter

def new_func(x, y):
    return x+2, y+1

def generator():
    """Generates an encrypter and decrypter.

    >>> e, d = generator()
    >>> msg = 'text'
    >>> encrypted = e(msg)
    >>> encrypted != msg
    True
    >>> decrypted = d(encrypted)
    >>> decrypted == msg
    True
    """
    def encrypter():
        return make_encrypter(caesar_generator(2, add), mirror_letter, caesar_generator(3, add))
    def decrypter():
        return make_decrypter(caesar_generator(2, sub), mirror_letter, caesar_generator(3, sub))
    return encrypter(), decrypter()

e, d = generator()

def count_cond(condition):
    """
    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2) # 1, 2
    2
    >>> count_factors(4) # 1, 2, 4
    3
    >>> count_factors(12) # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2) # 2
    1
    >>> count_primes(3) # 2, 3
    2
    >>> count_primes(4) # 2, 3
    2
    >>> count_primes(5) # 2, 3, 5
    3
    >>> count_primes(20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def cond(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return cond

def add1(x):
    return x+1
def times2(x):
    return x*2
def add3(x):
    return x+3

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def cycle_n(n):
        def cycle_x(x):
            def g1(x):
                return f1(x)
            def g2(x):
                return f2(f1(x))
            def g3(x):
                return f3(f2(f1(x)))
            if n == 0:
                return x
            if n == 1:
                return g1(x)
            if n == 2:
                return g2(x)
            if n == 3:
                return g3(x)
            else:
                return cycle_n(n-3)(g3(x))
        return cycle_x
    return cycle_n
