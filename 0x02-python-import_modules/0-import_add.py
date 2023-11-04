import importlib

add_module = importlib.import_module("0-add")
result = add_module.add(1, 2)
print(f"1 + 2 = {result}")
