def read_input_file(file_name):
    # Read the input file and extract the number of employees and goodies
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Extract number of employees
    number_of_employees = int(lines[0].split(":")[1].strip())

    # Extract goodies and their prices
    goodies = []
    for line in lines[2:]:
        if ":" in line:
            goodie, price = line.split(":")
            goodies.append((goodie.strip(), int(price.strip())))

    return number_of_employees, goodies


def bubble_sort_goodies(goodies):
    # Bubble sort to sort goodies by price (no external libraries used)
    n = len(goodies)
    for i in range(n):
        for j in range(0, n - i - 1):
            if goodies[j][1] > goodies[j + 1][1]:
                # Swap the goodies if they are in the wrong order
                goodies[j], goodies[j + 1] = goodies[j + 1], goodies[j]
    return goodies


def find_min_diff_goodies(employees, goodies):
    # Sort goodies by price using custom bubble sort
    sorted_goodies = bubble_sort_goodies(goodies)

    min_diff = float('inf')
    selected_goodies = []

    # Find the subset with minimum price difference
    for i in range(len(sorted_goodies) - employees + 1):
        diff = sorted_goodies[i + employees - 1][1] - sorted_goodies[i][1]
        if diff < min_diff:
            min_diff = diff
            selected_goodies = sorted_goodies[i:i + employees]

    return selected_goodies, min_diff


def print_output(selected_goodies, min_diff, test_case_name):
    # Print the output to the terminal
    print(f"Results for {test_case_name}:")
    print("The goodies selected for distribution are:")
    for goodie, price in selected_goodies:
        print(f"{goodie}: {price}")
    print(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {min_diff}\n")
    print("--------------------------------------------------")


def main():
    # List of input files for different test cases
    input_files = [
        "sample_input1.txt",
        "sample_input2.txt",
        "sample_input3.txt"
    ]
    
    # Loop through each file and process it
    for idx, input_file in enumerate(input_files):
        # Read input
        number_of_employees, goodies = read_input_file(input_file)
        
        # Find goodies with minimum price difference
        selected_goodies, min_diff = find_min_diff_goodies(number_of_employees, goodies)
        
        # Print output to the terminal
        print_output(selected_goodies, min_diff, f"Test Case {idx + 1}: {input_file}")


if __name__ == "__main__":
    main()
