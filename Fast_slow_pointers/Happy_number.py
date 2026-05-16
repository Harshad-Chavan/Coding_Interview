def check_happy_number(n):
    sl = fast = n
    while fast != 1:
        sl = get_next_num(sl)
        fast = get_next_num(get_next_num(fast))

        if sl == fast:
            return False

    return True


def get_next_num(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num = num // 10
    return sum(_**2 for _ in digits)


if __name__ == "__main__":
    print("+++check if the number is a happy number")
    n = 116
    (
        print("is a happy number")
        if check_happy_number(n)
        else print("is not a happy number")
    )
