import os

mode = os.getenv("APP_MODE","development")
print(f"Режим приложения: {mode}")