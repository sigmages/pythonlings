# I AM NOT DONE

hello_immutable = "Hello"
hello_mutable = ["H", "e", "l", "l", "o"]

hello_immutable[0] = "H"
hello_mutable[0] = "I WORK"

assert "".join(hello_mutable) == "I WORKello"
