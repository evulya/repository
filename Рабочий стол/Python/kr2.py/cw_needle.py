def find_needle(haystack: list)->str:
    return f'found the needle at position {haystack.index("needle")}' if "needle" in haystack else 'There is no needle'
print(find_needle(["something", "something2", "something3"]))