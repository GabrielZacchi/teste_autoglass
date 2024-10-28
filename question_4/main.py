from src.ola_mundo import ola_mundo
from src.logger import SetupLogger

if __name__ == "__main__":
    logger = SetupLogger().logger
    msg = ola_mundo()
    logger.info(msg)