def factors_of(item: int):
    response = []
    if item > 1:
        while item % 2 == 0:
            response.append(2)
            item //= 2
    if item > 1:
        response.append(item)
    return response
