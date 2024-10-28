import logging
import logging.handlers
import os
from datetime import datetime as dt

class SetupLogger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.log_dir = os.path.abspath("question_4/logs")

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.handlers.WatchedFileHandler(
            filename=os.path.join(
                self.log_dir,
                f"{dt.now().strftime('%Y-%m-%d')}_execution.log",
            )
        )

        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)