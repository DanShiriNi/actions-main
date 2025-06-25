def calculate_average(numbers: list[float]) -> int | None:
    if not numbers:
        return None
    sum = 0
    for i in numbers:
        sum += float(i)
    return int(sum / len(numbers))