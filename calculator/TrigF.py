def trigfunctions(x, y):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    def sin(x, y):
        result = 0.0
        for i in range(y):
            result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        return result

    def cos(x, y):
        result = 0.0
        for i in range(y):
            result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        return result

    def tan(x, y):
        return sin(x, y) / cos(x, y)

    def cot_taylor(x, n):
        sin_val = sin(x, n)
        cos_val = cos(x, n)
        return cos_val / sin_val

    print(f"sin({x}) = {sin(x, y)}")
    print(f"cos({x}) = {cos(x, y)}")
    print(f"tan({x}) = {tan(x, y)}")
