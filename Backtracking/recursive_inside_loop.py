def fun(n):
    if n == 0:
        return

    for i in range(2):
        print("Before recursion:", n, i)

        fun(n - 1)

        print("After recursion:", n, i)

fun(2)