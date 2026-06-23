def input_is_valid(msg, start=None, end=None):
    while True:
        inp = input(msg).strip()
        if not inp.isdigit():
            print("Invalid input. Try again!")
            continue

        value = int(inp)
        if start is not None and end is not None and not (start <= value <= end):
            print("Invalid range. Try again!")
            continue

        return value

