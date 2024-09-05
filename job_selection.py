def find_latest_non_conflicting_job(jobs, current_index):
    """
    Finds the most recent job that ends before the job at the current index starts.
    Uses binary search for efficiency.
    """
    low, high = 0, current_index - 1
    while low <= high:
        mid = (low + high) // 2
        # Check if the current mid-job ends before the current job starts
        if jobs[mid][1] <= jobs[current_index][0]:
            if mid + 1 < current_index and jobs[mid + 1][1] <= jobs[current_index][0]:
                low = mid + 1  # Continue searching for a more recent non-conflicting job
            else:
                return mid  # Return the most recent non-conflicting job index
        else:
            high = mid - 1  # Move to the left half if the jobs overlap
    return -1  # No non-conflicting job found

def job_selection_max_profit(n, jobs):
    """
    This function calculates the maximum profit John can earn and determines the number
    of jobs and profit left for other employees.
    """
    # Sort jobs by end time for optimal job selection
    jobs.sort(key=lambda x: x[1])

    # Dynamic programming array where dp[i] stores the max profit up to the i-th job
    dp = [0] * n
    # Array to track jobs selected by John
    selected_jobs = [0] * n

    dp[0] = jobs[0][2]  # First job's profit is directly taken
    selected_jobs[0] = 1  # John picks the first job by default

    # Loop through jobs and calculate maximum profit using dynamic programming
    for i in range(1, n):
        include_current = jobs[i][2]  # Profit if we include the current job
        # Find the latest non-conflicting job
        last_non_conflict = find_latest_non_conflicting_job(jobs, i)
        if last_non_conflict != -1:
            include_current += dp[last_non_conflict]  # Add profit from the last non-conflicting job

        # Take maximum profit by either including or excluding the current job
        if include_current > dp[i-1]:
            dp[i] = include_current
            selected_jobs[i] = 1  # Mark this job as selected by John
        else:
            dp[i] = dp[i-1]

    johns_profit = dp[-1]  # Maximum profit John can earn

    total_profit = sum(job[2] for job in jobs)  # Calculate total profit from all jobs

    # Calculate how many jobs are left for others (jobs John didn't pick)
    jobs_left_for_others = n - sum(selected_jobs)
    remaining_profit = total_profit - johns_profit  # Calculate earnings left for others

    return [jobs_left_for_others, remaining_profit]

def get_input_from_file(filename):
    """
    This function reads the input from a file and returns the result of job selection.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    n = int(lines[0].strip())  # Get the number of jobs
    jobs = []

    # Read jobs from the input file
    index = 1
    for _ in range(n):
        start_time = int(lines[index].strip())  # Start time in HHMM format
        end_time = int(lines[index + 1].strip())  # End time in HHMM format
        profit = int(lines[index + 2].strip())  # Profit for the job
        jobs.append((start_time, end_time, profit))  # Append job details
        index += 3

    # Return the result after processing the input
    result = job_selection_max_profit(n, jobs)
    return result

def process_multiple_files(file_list):
    """
    This function processes multiple input files and prints results for each.
    """
    for filename in file_list:
        print(f"Processing {filename}...")
        result = get_input_from_file(filename)
        print(f"The number of tasks and earnings available for others:")
        print(f"Task: {result[0]}")
        print(f"Earnings: {result[1]}")
        print()  # Blank line for readability between files

# Example of input files to process
input_files = ['input1.txt', 'input2.txt', 'input3.txt']

# Process all input files and print results
process_multiple_files(input_files)
