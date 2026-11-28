# Q.1
def sum_even_positions(n, pos=1):
    if n == 0:
        return 0
    current = (n % 10) if pos % 2 == 0 else 0
    return current + sum_even_positions(n // 10, pos + 1)


print(sum_even_positions(583246))  # Output: 12