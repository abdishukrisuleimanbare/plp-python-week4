count = 1
total = 0

# BUG: The while condition was missing a colon, so I added ":".
# BUG: The loop stopped before processing 5, so I changed "<" to "<=".
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The print statement tried to concatenate a string with an integer, so I changed it to an f-string.
print(f"Sum of 1 to 5 is: {total}")