#!/usr/bin/python3
print("".join("{}".format(chr(122 - i + 32 * (i % 2))) for i in range(26)))
