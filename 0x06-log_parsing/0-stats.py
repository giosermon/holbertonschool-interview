#!/usr/bin/python3
"""
module for log parsing
"""

from sys import stdin

if __name__ == "__main__":
    total = 0
    codes = {"200": 0, "301": 0, "400": 0,
             "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for count, line in enumerate(stdin):
            args = line.split(" ")
            if len(args) < 2:
                continue
            if args[-2] in codes:
                codes[args[-2]] += 1
            try:
                total += int(args[-1])
            except:
                pass
            if (count + 1) % 10 == 0:
                print("File size: {}".format(total))
                for status in sorted(codes.keys()):
                    if codes[status] != 0:
                        print("{}: {}".format(status, codes[status]))
        print("File size: {}".format(total))
        for status in sorted(codes.keys()):
            if codes[status] != 0:
                print("{}: {}".format(status, codes[status]))
    except KeyboardInterrupt:
        print("File size: {}".format(total))
        for status in sorted(codes.keys()):
            if codes[status] != 0:
                print("{}: {}".format(status, codes[status]))
