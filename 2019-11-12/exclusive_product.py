def calculate(numbers):
    product = 1

    for i in range(len(numbers)):
        product *= numbers[i]

    for i in range(len(numbers)):
        numbers[i] = product / numbers[i]

    return numbers


def calculate_no_division(numbers):
    result = []
    product = 1
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i:
                product *= numbers[j]
                
        result.append(product)
        product = 1

    return result
