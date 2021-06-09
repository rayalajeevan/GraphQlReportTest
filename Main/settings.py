from pydantic import BaseSettings
import os
import logging
from functools import lru_cache
import sys
from dotenv import load_dotenv
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger("app.main")
logger.addHandler(logging.StreamHandler(sys.stdout))

class ConfigurationException(Exception):
    def __init__(self,message="Please provide correct enviroment variable for settings {please use this settings=testing or production or development}"):
        self.message=message
        super().__init__(self.message)

class Settings(BaseSettings):
    app_name: str = "TEST_REPORTS"
    database_user: str
    database_password: str
    database_host:str
    database_port:str
    property:str

    class Config:
        prop=os.getenv("settings")
        if prop!=None and prop.lower().strip()!="":
            if prop.lower()=="dev":
                load_dotenv(dotenv_path=Path("./dev.env"))
                env_file = "./dev.env"
                logger.info(f"Starting the server  using {env_file} configuration")
            elif prop.lower()=="test":
                load_dotenv(dotenv_path=Path("./test.env"))
                env_file = "./test.env"
                logger.info(f"Starting the server  using {env_file} configuration")
            elif prop.lower()=="prod":
                load_dotenv(dotenv_path=Path("./prod.env"))
                env_file="./prod.env"
                logger.info(f"Starting the server  using {env_file} configuration")
            else:
                try:
                    raise ConfigurationException()
                except Exception as exc:
                    logger.exception(str(exc))
                    raise ConfigurationException()
        else:
            try:
                raise ConfigurationException()
            except Exception as exc:
                logger.exception(str(exc))
                raise ConfigurationException()
                
@lru_cache()
def get_settings():
    return Settings()          