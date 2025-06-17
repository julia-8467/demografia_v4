import os

APP_ENV = os.getenv('APP_ENV', 'development')

# Dane produkcyjne
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', )
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', )
DATABASE_HOST = os.getenv('DATABASE_HOST', )
DATABASE_PORT = os.getenv('DATABASE_PORT', )
DATABASE_NAME = os.getenv('DATABASE_NAME', )

# Dane testowe (osobna baza na testy)
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'postgres_test')
