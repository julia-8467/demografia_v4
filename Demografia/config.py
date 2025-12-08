import os

APP_ENV = os.getenv('APP_ENV', 'development')

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'demografia')

TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'demografia_test')

