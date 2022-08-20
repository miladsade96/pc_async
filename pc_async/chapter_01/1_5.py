"""
    Generating and timing the Fibonacci sequence
"""

import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        """
        Calculating fibonacci sequence
        :param n: fibonacci sequence from 1 to n
        :return: nth fibonacci number
        """
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f"fib({number}) is {fib(number)}")
