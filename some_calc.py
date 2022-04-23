from bisect import bisect_left
import canonical_2_general_converter as ca2gen

class Some_calc:
    def __init__(self, hx_1: float, hx_2: float, fx_1: float, fx_2: float, fx_3: float, lambda_: float):
        self.h_k, self.h_b = ca2gen.up_line_k_b(hx_1, hx_2)
        self.f_k1, self.f_b1 = ca2gen.up_line_k_b(fx_1, fx_2)
        self.f_k2, self.f_b2 = ca2gen.down_line_k_b(fx_2, fx_3)
        self.a = fx_1
        self.b = fx_3
        self.lambda_ = lambda_
        self.err = 10**(-5)

    def h_func(self, x: float) -> float:
        y = self.h_k * x + self.h_b
        if y < 0:
            return 0
        elif y > 1:
            return 1
        else:
            return y

    def f_func(self, x: float):
        y1 = self.f_k1 * x + self.f_b1
        y2 = self.f_k2 * x + self.f_b2
        if y1 < 0 or y2 < 0:
            return 0
        elif y1 > 1:
            return y2
        elif y2 >= 1:
            return y1

    def get_g(self, alpha: float) -> float:
        a = self.a + alpha
        b = self.b - alpha
        return (self.h_func(b) - self.h_func(a)) / (1 + self.lambda_ * self.h_func(a))

    def is_alpha(self, alpha) -> int:
        ex_alpha = self.get_g(alpha)
        if abs(ex_alpha - alpha) < self.err:
            return 0
        elif ex_alpha > alpha:
            return 1
        else:
            return -1


