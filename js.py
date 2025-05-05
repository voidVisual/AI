def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = [False] * t 
    job = ['-1'] * t

    for i in range(n):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:
                result[j] = True
                job[j] = arr[i][0]
                break

    print("\nJob sequence for maximum profit:")
    print(' -> '.join([j for j in job if j != '-1']))


if __name__ == '__main__':
    n = int(input("Enter number of jobs: "))
    arr = []
    for i in range(n):
        name = input(f"\nEnter Job {i+1} name: ")
        deadline = int(input("Enter deadline: "))
        profit = int(input("Enter profit: "))
        arr.append([name, deadline, profit])

    t = int(input("\nEnter number of available time slots: "))

    print("\nFollowing is the maximum profit sequence of jobs:")
    printJobScheduling(arr, t)

