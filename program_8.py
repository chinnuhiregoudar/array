# Program to calculate the sum and average of scores

scores = list(map(int, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
