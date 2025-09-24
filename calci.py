print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")
nums = list(map(float, input("Enter numbers separated by space: ").split()))

if choice == "1":
    print("Result:", sum(nums))
elif choice == "2":
    result = nums[0]
    for n in nums[1:]:
        result -= n
    print("Result:", result)
elif choice == "3":
    result = 1
    for n in nums:
        result *= n
    print("Result:", result)
elif choice == "4":
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            print("Error! Division by zero.")
            break
        result /= n
        .0
    else:
        print("Result:", result)
else:
    print("Invalid choice")
