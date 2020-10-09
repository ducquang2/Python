# Import decimal
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    querry_name = input()

# Extract the value into a list: query_scores
querry_scores = student_marks[querry_name]

# Sum the scores in the list: total_scores
total_scores = sum(querry_scores)

# Convert the floats to dicimals and average the scores: avg
avg = Decimal(total_scores/3)

# Print the mean of the scores, correct to two decimals
print(round(avg,2))
