def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


# outer appelé au début, puis que inner par my counter
# inner est return dans my counte

# non local crée une "statique pour l'appel", une statique
# par function assigné. chaque = outer aura sa statiaue
# en c y'en aurait qu'une au total
def outer(x, function):
    count = 0
    current = x

    def inner():
        nonlocal count, current
        count += 1
        current = function(current)
        return current
    return inner


def main():
    try:
        my_counter = outer(3, square)
        print(my_counter())
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    main()
