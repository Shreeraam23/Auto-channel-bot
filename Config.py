import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 28036362
    API_HASH = "84e4bd8457dab2f065801bde8874842a"
    BOT_TOKEN = "8189822314:AAGpd4guRLI1zRskAjIk5Dh6ERcfcFviiJU"
    DATABASE_URL = "mongodb+srv://dafeh64648:dxkiXApD489QKbjN@ramsingh.o0kha.mongodb.net/?retryWrites=true&w=majority&appName=Ramsingh"
    DATABASE_URL = DATABASE_URL.replace("postgres", "Ramsingh")
    MUST_JOIN = "myserver23"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
