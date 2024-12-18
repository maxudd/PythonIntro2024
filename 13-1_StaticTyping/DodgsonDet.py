def minor_det(minor: list[list[int]]) -> int:
    return minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]


def minor(mat: list[list[int]], i: int, j: int) -> int:
    return minor_det([[mat[0][0], mat[i][0]],
                      [mat[0][j], mat[i][j]]])


def one_step(mat: list[list[int]]) -> list[list[int]]:
    new_mat = []
    for j in range(len(mat) - 1):
        new_row = []
        for i in range(len(mat) - 1):
            new_row.append(minor(mat, i + 1, j + 1))
        new_mat.append(new_row)
    return new_mat


mat: list[list[int]] = []
first: list[int] = list(eval(input()))
mat.append(first)
n: int = len(first)
for _ in range(1, n):
    mat.append(list(eval(input())))

d: list[int] = []
first_elems: list[int] = []
sign: int = 1
swapped: bool
det: int = 0

while len(mat) != 2:
    swapped = False
    if not mat[0][0]:
        for i, v in enumerate(mat[1::]):
            if v[0] != 0:
                mat[0], mat[i + 1] = mat[i + 1], mat[0]
                swapped = True
                break
        else:
            break
    if swapped:
        sign *= -1
    first_elems.append(mat[0][0])
    d += first_elems
    mat = one_step(mat)
else:
    result_d = 1
    for i in d:
        result_d *= i
    det = sign * minor_det(mat) // result_d

print(det)
