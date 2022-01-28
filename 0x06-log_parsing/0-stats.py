#!/usr/bin/python3
""" Python script that reads stdin line by line and computes metrics
"""


from sys import stdin, exit


def printCodeTracking(T_File_Size, Tracker):
    """ Print formatted log stats.
    """
    # Print total size of data passed to date
    print('File size: ' + str(T_File_Size))

    codeList = sorted(Tracker.keys())

    # Print formatted count of requests by status code
    for code in codeList:
        if Tracker[code] != 0:
            print(code + ': ' + str(Tracker[code]))


Tracker = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
T_File_Size = 0
Counter = 0

try:
    for line in stdin:
        lineSplit = line.split()
        # Pull necessary fields from log line
        if len(lineSplit) >= 2:
            statusCode, fileSize = [part for part in lineSplit[-2:]]

            # Update persistent size and status counters
            T_File_Size += int(fileSize)
            if statusCode in Tracker:
                Tracker[statusCode] += 1

                # Keep track of how many logs have been read in print loop
                if Counter == 9:
                    printCodeTracking(T_File_Size, Tracker)
                    Counter = 0
                else:
                    Counter += 1
    # Print stats at end of input stream
    printCodeTracking(T_File_Size, Tracker)

except KeyboardInterrupt:
    printCodeTracking(T_File_Size, Tracker)
