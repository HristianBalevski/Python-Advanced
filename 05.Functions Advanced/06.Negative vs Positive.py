def negative_vs_positive(*args):
    negative = 0
    positive = 0

    for number in args:
        if number < 0:
            negative += number
        else:
            positive += number
    return negative, positive


given_numbers = [int(num) for num in input().split()]
negative_sum, positive_sum = negative_vs_positive(*given_numbers)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")