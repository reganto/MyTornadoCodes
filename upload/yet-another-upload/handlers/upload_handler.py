import tornado.web

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            file1 = self.request.files["morteza"][0]
        except:
            file1 = None

        o_filename = file1["filename"]
        m = o_filename.split('.')
        n = '01.'+m[1]

        output_file = open("static/uploads/"+n, "wb")
        output_file.write(file1["body"])

        self.render("image.html", n=n)
