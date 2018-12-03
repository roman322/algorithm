def get_combination_lengths(words):
    words.sort(key=len)
    solutions = {words[0]: 1}
    print(solutions)
    for parent in words[1:]:
        print(parent)
        max_length = 0
        print(range(len(parent)))

        for i in range(len(parent)):
            print(range)
            option = parent[:i] + parent[i + 1:]
            if option not in solutions:
                continue
            option_length = solutions[option]
            if option_length > max_length:
                max_length = option_length
        max_length += 1
        solutions[parent] = max_length
        yield max_length


if __name__ == '__main__':
    with open('wchain.in', 'r') as fl:
        fl.readline()
        words = [ln.strip() for ln in fl.readlines()]

    result = max(get_combination_lengths(words))
    print(result)
