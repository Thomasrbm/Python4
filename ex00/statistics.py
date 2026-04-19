def ft_mean(nb: list):
    if not nb:
        print("ERROR")
        return
    mean = sum(nb) / len(nb)
    print(f"mean = {mean}")


def ft_median(nb: list):
    if not nb:
        print("ERROR")
        return
    sort = sorted(nb)
    i = len(nb)
    mid = i // 2
    if i % 2 == 0:
        print(f"median = {sort[mid - 1] + sort[mid] / 2}")
    print(f"median = {sort[mid]}")


def ft_quartile(nb: list):
    if not nb:
        print("ERROR")
        return
    sort = sorted(nb)
    n = len(nb)
    q1 = sort[n // 4]
    q3 = sort[(3 * n) // 4]
    print(f"quartile : [{float(q1)}, {float(q3)}]")


def ft_std(nb: list):
    if not nb:
        print("ERROR")
        return
    mean = sum(nb) / len(nb)
    variance = sum((x - mean) ** 2 for x in nb) / len(nb)
    print(f"std : {variance ** 0.5}")


def ft_var(nb: list):
    if not nb:
        print("ERROR")
        return
    mean = sum(nb) / len(nb)
    print(f"var : {sum((x - mean) ** 2 for x in nb) / len(nb)}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    if not all(isinstance(a, (int, float)) for a in args):
        raise ValueError("all args must be numbers")
    if not all(isinstance(v, str) for v in kwargs.values()):
        raise ValueError("all kwargs values must be strings")

    nb = []
    for n in args:
        nb.append(int(n))

    b_mean = False
    b_median = False
    b_quartile = False
    b_sdevia = False
    b_variance = False

    for m in kwargs.values():
        if m == "mean":
            b_mean = True
        if m == "median":
            b_median = True
        if m == "quartile":
            b_quartile = True
        if m == "std":
            b_sdevia = True
        if m == "var":
            b_variance = True

    if b_mean:
        ft_mean(nb)
    if b_median:
        ft_median(nb)
    if b_quartile:
        ft_quartile(nb)
    if b_sdevia:
        ft_std(nb)
    if b_variance:
        ft_var(nb)


def main():
    try:

        ft_statistics(1, 42, 360, 11, 64, toto="mean",
                      tutu="median", tata="quartile")
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    main()
