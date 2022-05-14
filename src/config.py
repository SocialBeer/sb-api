from pydantic import BaseSettings
import datetime


class Config(BaseSettings):    
    port:int = 8080
    host:str = '127.0.0.1'
    reload:bool = True
    # db_url:str = 'postgresql://zxndrufdblkifj:8fc253fc980bdb20ca4f68fcf57126b4a2aed75207bb5af04a5c2d77d7008aa9@ec2-176-34-211-0.eu-west-1.compute.amazonaws.com:5432/da4r5j8g8p0p62'
    # TEST DB URL
    db_url:str = 'postgresql://postgres:06082003@localhost:5432/Sb-sb-test'
    secret_access_token_key: str = 'd86c828583c5c6160e8acfee88ba1590'
    secret_refresh_token_key: str = 'e57941dbe1246fe97a4ffc16e85b5df9'
    access_token_time = datetime.timedelta(minutes = 20)
    refresh_token_time = datetime.timedelta(hours = 24)

config = Config()
