counter = 0
while counter < 10:
    print(counter)
    counter += 1
    if counter == 5:
        break
print(f"Exited while loop prematurely as value is: {counter}")
