languages = [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "Go",
    "Rust",
    "C#",
    "Kotlin"
]

print(languages[:3])
print(languages[-3:])
print(languages[2:6])
print(languages[::2])
print(languages[::-1])
print(languages[::])
print(languages[1:-1])
print(languages[1::3])
languages[2:4] = ["SQL", "HTML"]
print(languages)