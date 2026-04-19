from callLimit import callLimit

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
