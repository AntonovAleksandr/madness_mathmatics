def get_k_b(x1: float, x2: float, y1: float, y2: float) -> tuple[float, float]:
    assert x1 < x2
    if y1 < y2:
        return 1 / (x2 - x1), -x1 / (x2 - x1)
    else:
        return -1 / (x2 - x1), x2 / (x2 - x1)


def up_line_k_b(x1: float, x2: float) -> tuple[float, float]:
    return get_k_b(x1, x2, 0, 1)


def down_line_k_b(x1: float, x2: float) -> tuple[float, float]:
    return get_k_b(x1, x2, 1, 0)