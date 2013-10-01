import logging
import os.path
import sys
import time
import tempfile

mm_start = time.time()

logging.raiseExceptions = False
logging.basicConfig(level=logging.INFO)

#logging_handler = logging.FileHandler(os.path.join(tempfile.gettempdir(),"mm.log"))
logging_handler = logging.FileHandler("/Users/asrivatsa/Desktop/"+"mm.log")

#suds log setup
suds_logger = logging.getLogger('suds.client')
suds_logger.setLevel(logging.WARN)
suds_logger.propagate = False
suds_logger.addHandler(logging_handler) 

#mm log setup
logger = logging.getLogger('mm')
logger.setLevel(logging.ERROR)
logger.propagate = False 
logger.addHandler(logging_handler)

#request log setup
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.ERROR)

def __get_base_path():
    if hasattr(sys, 'frozen'):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.dirname(__file__))

def __get_is_frozen():
    if hasattr(sys, 'frozen'):
        return True
    else:
        return False
frozen = __get_is_frozen()
base_path = __get_base_path()
connection = None

windows_platforms = ["win32","win64","cygwin"]
linux_platforms = ["linux2"]
osx_platforms = ["darwin"]
user_platform = sys.platform

is_windows   = user_platform in windows_platforms
is_linux     = user_platform in windows_platforms
is_osx       = user_platform in windows_platforms
