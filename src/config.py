from pydantic import BaseSettings

class Config(BaseSettings):    
    port:int = 8080
    host:str = '127.0.0.1'
    reload:bool = True
    db_url:str = 'postgresql://zxndrufdblkifj:8fc253fc980bdb20ca4f68fcf57126b4a2aed75207bb5af04a5c2d77d7008aa9@ec2-176-34-211-0.eu-west-1.compute.amazonaws.com:5432/da4r5j8g8p0p62'

config = Config()
