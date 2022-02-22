#!/usr/bin/python3
""" A program to ingest and track logs, periodically printing stats.
"""
import sys

if __name__ == "__main__":

    status = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
              "404": 0, "405": 0, "500": 0}
    size = 0
    print10Lines = 0

    try:
        for text in sys.stdin:
            code = text.split('"')[2].split(" ")[0]
            unitSize = int(text.split('"')[2].split(" ")[1])
            size += unitSize
            print10Lines += 1

            for key in sorted(status.keys()):
                if code == key:
                    status[key] += 1

            if print10Lines == 10:
                print("File size: {:d}".format(size))
                for key in sorted(status.keys()):
                    if status[key] and status is int:
                        print("{}: {:d}".format(key, status[key]))
                print10Lines = 0

    except KeyboardInterrupt:
        pass

    finally:
        print("File size: {:d}".format(size))

        for key in sorted(status.keys()):
            if status[key] and status is int:
                print("{}: {:d}".format(key, status[key]))
