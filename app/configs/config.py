from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = 'sqlite:///sqlite3.db'

    SECRET_KEY: str = 'secret_key_value'

    class Config:
        env_file = '.env'


settings = Settings()
