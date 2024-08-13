
calls = 0


def count_calls() -> None:
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    l: int = len(string)
    upper = string.upper()
    lower = string.lower()
    t = (l, upper, lower)
    return t


def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    for s in list_to_search:
        if type(s) is not str:
            print(f"Input list contained an element ({s}) of type {type(s)}, which is bad. Don't do that, me angry >:(.")
            continue
        if string.lower() == s.lower():
            return True
    return False


print(string_info("Flauxinosinihilipilification"))
print(string_info("Flabbergaster"))
print(string_info("UGANDA"))
print(is_contains("possum", ["branch", "fork", "cease"]))
print(is_contains("fraudulent", ["streamer", "subscription", "FraUdUlEnt", "donation", 100000]))

print("Total calls:", calls)
