import sys
import logging

logger = logging.getLogger('Reganto')



# Define handlers for specific outputs
file_handler = logging.FileHandler(filename='/tmp/auth.log', mode='a')
stream_handler = logging.StreamHandler(sys.stderr)

# Define formatters for format LogRecords
file_formatter = logging.Formatter('%(process)d - %(levelname)s - %(name)s - %(asctime)s - %(message)s')
stream_formatter = logging.Formatter('%(process)d - %(levelname)s - %(name)s - %(asctime)s - %(message)s')

# Add formatters to handlers
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

# file_handler.setLevel(logging.DEBUG)
# stream_handler.setLevel(logging.DEBUG)


# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
