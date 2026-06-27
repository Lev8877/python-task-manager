import copy 

original = [
    ["Python", "FastAPI"],
    ["PostgreSQL", "Redis"]
]

copyy = original.copy()

original[0].append("Django")

print(original)
print(copyy)

original = [
    ["Python", "FastAPI"],
    ["PostgreSQL", "Redis"]
]

True_copy = copy.deepcopy(original)

original[0].append("Django")

print(original)
print(True_copy)