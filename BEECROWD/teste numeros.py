from itertools import combinations

def all_numbers(numbers):
    result = set()
    for i in range(1, len(numbers) + 1):
        for combination in combinations(numbers, i):
            prod = 1
            for number in combination:
                prod *= number
            result.add(prod)
    return sorted(result)

# Exemplo de uso
numbers = [2, 2, 5, 5]
print(all_numbers(numbers))
