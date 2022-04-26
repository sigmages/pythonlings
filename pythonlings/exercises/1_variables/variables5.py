# I AM NOT DONE

hello_immutable_string = "Hello"
hello_mutable_list = ["H", "e", "l", "l", "o"]
hello_mutable_dict = {"Hello": "World"}
hello_mutable_set = {1, 2, 3}

hello_immutable_string[0] = "H"
hello_mutable_list[0] = "I WORK"

# DON'T EDIT THE TESTS
assert "".join(hello_mutable_list) == "I WORKello"
