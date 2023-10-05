#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    res_add = add(a, b)
    res_sub = sub(a, b)
    res_mul = mul(a, b)
    res_div = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, res_add))
    print("{:d} - {:d} = {:d}".format(a, b, res_sub))
    print("{:d} * {:d} = {:d}".format(a, b, res_mul))
    print("{:d} / {:d} = {:d}".format(a, b, res_div))
