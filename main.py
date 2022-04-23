# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
from some_calc import Some_calc


def get_alpha(calck: Some_calc) -> float:
    start = 0
    end = 1
    step = 0
    while (start <= end):
        step = step + 1
        alpha = start + (end - start) / 2
        print(f'alpha is: {alpha}, is alpha: {calck.is_alpha(alpha)}')
        compare = calck.is_alpha(alpha)
        if compare == 0:
            return alpha
        if compare < 0:
            end = alpha
        else:
            start = alpha
    return -1


def sup(alpha: float, calck: Some_calc) -> float:
    max = -1
    if alpha < calck.get_g(alpha):
        i = 0
        while abs(alpha - i) > calck.err:
            if alpha > max:
                max = alpha
            i += calck.err
    else:
        i = alpha
        while abs(1 - i) > calck.err:
            g = calck.get_g(alpha)
            if g > max:
                max = g
            i += calck.err
    return max


if __name__ == '__main__':
    # print("Enter h_1, x_2, x_3, step and freq!")
    # print("hx_1 (y1 = 0): ")
    # hx_1 = float(input())
    # print("hx_2 (y2 = 1): ")
    # hx_2 = float(input())
    # print("fx_1 (y1 = 0): ")
    # fx_1 = float(input())
    # print("fx_2 (y2 = 1): ")
    # fx_2 = float(input())
    # print("fx_3 (y3 = 0): ")
    # fx_3 = float(input())
    # print("lambda_ : ")
    # lambda_ = float(input())

    hx_1 = 1
    hx_2 = 2
    fx_1 = 1
    fx_2 = 2
    fx_3 = 3
    lambda_ = 5
    calck = Some_calc(hx_1, hx_2, fx_1, fx_2, fx_3, lambda_)
    alpha = get_alpha(calck)
    res = sup(alpha, calck)
    print(f'result: {res}')

    a = round(min(hx_1, fx_1) - 10)
    b = round(max(hx_2, fx_3) + 10)
    y = [y for y in range(a, b)]
    alpha_x = [alpha for _ in range(a, b)]
    x_H = [calck.h_func(x) for x in range(a, b)]
    x_F = [calck.f_func(x) for x in range(a, b)]

    plt.plot(y, x_F, 'g')
    plt.plot(y, x_H, 'k--', linewidth=4)
    plt.hlines(alpha, a, b)
    plt.xlabel('y')
    plt.ylabel('x')
    plt.title('pyramid')
    plt.show()
