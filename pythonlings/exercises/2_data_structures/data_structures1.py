# I AM NOT DONE

my_list = [0, "hello", True, ["other list"]] # or my_list = list()

my_list[0] = 1
my_list.append(3)
my_list.append(4)
my_list.pop()

# DON'T EDIT THE TESTS
assert len(my_list) == 4
assert my_list[0] == 1
assert my_list[1] == "world"
assert my_list[2] == False
