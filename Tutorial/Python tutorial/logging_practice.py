import logging
# ''' Logging contain Debug10,Info20,Warning30,Error40,Critical50'''

# '''Now configure the basic logging it contain level,filename,filemode,format'''

# Create custom logger

logger = logging.getLogger(__name__)
# create handler
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log',mode='w')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.ERROR)
# create formater and add to handlers

c_format = logging.Formatter('%(asctime)s %(levelname)s - %(message)s',datefmt="%d-%m-%Y %I:%M %p")
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt="%d-%m-%Y %I:%M %p")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handler to logger

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.info('This is Info')
logger.warning('This is a Warning')
logger.error('This is a Error')
logger.critical('This is a Critical')




