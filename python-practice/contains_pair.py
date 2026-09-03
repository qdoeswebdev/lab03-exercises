# I used https://www.w3schools.com/ to relearn the python syntax for this program.
def check(l: list):
    seen = set()
    for value in l:
        if value in seen:
            return True
        else:
            seen.add(value)
    return False


print(check([1, 2, 3, 2]))          # should print True
print(check([5, 2, -10, 44, 90]))   # should print False