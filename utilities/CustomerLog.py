import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()#initialize a logger instance
        fhandler = logging.FileHandler(filename='./Logs/Automation.Log',mode = 'a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

if __name__=='__main__':
    logger = LogGen.loggen()
    logger.info('test')