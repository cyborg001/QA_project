import logging

class Logger:
    '''This class sets a logging configuration and has 
    a method which creates logs messages and save them to a file'''
    
    # logging.basicConfig()
    logging.root.setLevel(logging.INFO)
    # logging.basicConfig(level=logging.NOTSET)
    # logging.basicConfig(filename='mylog.txt')
    logger = logging.getLogger('Selenium Test')
    logFile = 'mylog.txt'
    fileHandler = logging.FileHandler(logFile)
    logger.addHandler(fileHandler)

    formato = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    formatter = logging.Formatter(formato)
    fileHandler.setFormatter(formatter)

    def setLog(self,level,message):
        f'''Accept 2 arguments: 
        level: is the level of the logger ex. "debug"
        message: is some output from the app
        
        create the log and send it to the {self.logFile} '''
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.error(message)
        else:
            raise Exception('Level incorrecto, introduzca un level')
