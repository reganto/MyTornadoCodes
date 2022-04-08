import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from PIL import Image
from io import StringIO,BytesIO
def test():
 x = Image.new('RGB',(400,400))
 output = StringIO()
 x.save(output, "PNG")
 contents = output.getvalue().encode("base64")
 output.close()
 return HttpResponse('<img src="data:image/png;base64,' + contents + ' />')

