#!/usr/bin/python3
show = ""
for i in range(0, 8):
    for j in range(i+1, 10):
        print(f"{i}{j}", end=", ")
print(f"{i+1}{j}")

