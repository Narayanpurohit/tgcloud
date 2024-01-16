import os

class Config:
    API_ID = int( os.getenv("api_id","15191874") )
    API_HASH = os.getenv("api_hash","3037d39233c6fad9b80d83bb8a339a07")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1002029287584") )
    CHANNEL_USERNAME = os.getenv("channel_username","irish_family")
    TOKEN = os.getenv("token","6808668384:AAGKNPT24tLupcU_rKEys4JK-U3Yi2jLloc")
    DOMAIN  = os.getenv("domain","https://ytdlbot-e25fc23a1ac0.herokuapp.com/")
 
