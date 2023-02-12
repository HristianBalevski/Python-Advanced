def numbers_searching(*args):
    duplicate_numbers = []

    for num in args:
        result = args.count(num)
        if result > 1 and num not in duplicate_numbers:
            duplicate_numbers.append(num)
    sort_nums = sorted(args)
    output = []
    for num in range(sort_nums[0], sort_nums[-1]):
        if num not in args:
            output.append(num)
            output.append(sorted(duplicate_numbers))
            break
    return output
