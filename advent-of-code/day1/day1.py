#No funny business quick solution

def read_data(file_path):
    arr1 = []
    arr2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = map(int, line.split())
            arr1.append(num1)
            arr2.append(num2)
    
    return arr1, arr2


def process_arrays(arr1, arr2):
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    
    differences = [abs(a - b) for a, b in zip(arr1, arr2)]
    total_difference = sum(differences)
    
    return total_difference


def frequencies(arr1, arr2):
    frequency_sum = 0
    
    for item in arr1:
        count = arr2.count(item)
        product = item * count
        frequency_sum += product

    return frequency_sum


def main():
    file_path = 'input.txt'
    arr1, arr2 = read_data(file_path)
    differences = process_arrays(arr1, arr2)
    
    #Part A solution
    print("Absolute differences:", differences)

    #Part B solution
    print("Frequency sum:", frequencies(arr1, arr2))

if __name__ == "__main__":
    main()