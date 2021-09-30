import logging
import logging.config


class Logger:
    """
    A class to handle logging for the modules
    """

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.format = '[%(asctime)s:%(levelname)s][%(name)s]%(message)s'
        self.log_file = 'C:/Users/Kaustubh Bhalerao/Work/Python/SeleniumDemo/reports/Log_'+name+'.log'
        logging.basicConfig(filename=self.log_file, format=self.format, filemode='w')
