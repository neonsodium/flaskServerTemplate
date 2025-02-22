import os
import platform


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "you-will-never-guess:6d667eac81ee0897e67cecbaf10a801ee789f06a2e9849e46cd28728"
    )
    DEBUG = False
    HOST = "127.0.0.1"

    if platform.system() == "Darwin":  # macOS coz i work on
        ENV = "development"
    elif platform.system() == "Linux":  # Linux
        ENV = "production"
    else:
        ENV = "testing"


class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 8080
    LOGIN_REQUIRED = True
    PASSWORD = "p"
    USERNAME = "p"


class ProductionConfig(Config):
    DEBUG = False
    LOGIN_REQUIRED = False
    PORT = 8009  # 8009 to 80 on the internet on the server idk
    USERNAME = "girish_pvl"
    PASSWORD = "HelloML"


class TestingConfig(Config):
    DEBUG = True
    LOGIN_REQUIRED = False
    PORT = 8080
    USERNAME = "p"
    PASSWORD = "p"
