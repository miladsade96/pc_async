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


# No-threading Section
def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start = time.time()
fibs_no_threading()
end = time.time()

print(f"Completed in {end - start:.4f} seconds.")