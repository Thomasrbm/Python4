def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count > limit:
                raise Exception(f"{function} call too many times")
            return function(*args, **kwds)
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        try:
            f()
        except Exception as e:
            print(f"Error: {e}")
        try:
            g()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
