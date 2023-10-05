#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    result = 0

    for i in range(1, argc + 1):
        result += int(sys.argv[i])

    print(result)
