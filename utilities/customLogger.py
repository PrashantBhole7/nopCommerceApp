import logging

from importlib import reload # python 2.x don't need to import reload, use it directly
reload(logging)
class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="Logs/automation_search_customer.log",
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%m%d%Y %I%M%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

