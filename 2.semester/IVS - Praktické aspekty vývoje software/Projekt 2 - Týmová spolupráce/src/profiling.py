import fileinput
import math_lib


def deviation():
    nmbrs = []
    sum = 0
    squaresum = 0
    count = 0
    average = 0

    for line in fileinput.input():
        nmbrs.append(float(line))

        sum = math_lib.add(sum, float(line))
        squaresum = math_lib.add(squaresum, math_lib.square(float(line)))
        count = count + 1

    x = math_lib.mul(sum, math_lib.div(1, count))  # 1/N * sum

    return math_lib.sqroot(math_lib.mul(math_lib.div(1, math_lib.sub(count, 1)),
                                        math_lib.sub(squaresum, math_lib.mul(count, math_lib.square(x)))))


if __name__ == '__main__':
    s = deviation()
    print(s)
