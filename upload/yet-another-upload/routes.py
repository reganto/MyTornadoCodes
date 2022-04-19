from handlers.index_handler import *
from handlers.upload_handler import *

urlList = [
    (r"/", IndexHandler),
    (r"/upload", UploadHandler)
]
