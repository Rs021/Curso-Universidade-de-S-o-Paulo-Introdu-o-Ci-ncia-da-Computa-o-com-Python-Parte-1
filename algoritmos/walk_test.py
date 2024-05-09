def is_valid_walk(walk):
    if len(walk) == 10:
        return walk.count("w") == walk.count("e") and walk.count("s") == walk.count("n")
    return False


def test():
    assert is_valid_walk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]) == True
    assert is_valid_walk(["w", "e", "w", "e", "w", "e", "w", "e", "w", "e", "w", "e"]) == False
    assert is_valid_walk(["w"]) == False
    assert is_valid_walk(["n", "n", "n", "s", "n", "s", "n", "s", "n", "s"]) == False
