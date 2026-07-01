languages = ["Python", "Java", "Go"]

languagess = iter(languages)

for _ in range(len(languages)):
    print(next(languagess))