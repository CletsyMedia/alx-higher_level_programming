#!/usr/bin/python3
import sys


def print_metrics(stats):
    print("File size: {}".format(stats['total_size']))
    sorted_codes = sorted(stats['status_codes'].items())
    for code, count in sorted_codes:
        if count > 0:
            print("{}: {}".format(code, count))


def main():
    stats = {
        'total_size': 0,
        'status_codes': {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    }
    line_number = 0

    try:
        for line in sys.stdin:
            line_number += 1
            tokens = line.split()
            if len(tokens) > 1:
                size = int(tokens[-1])
                status_code = int(tokens[-2])
                stats['total_size'] += size
                if status_code in stats['status_codes']:
                    stats['status_codes'][status_code] += 1
            if line_number % 10 == 0:
                print_metrics(stats)

    except KeyboardInterrupt:
        print_metrics(stats)


if __name__ == "__main__":
    main()
