@require_basic_auth
class UploadFile(tornado.web.RequestHandler):
    def put(self, params):
        path = calculate_path(params)
        with open(path, 'wb') as out:
            body = self.request.get_argument('data')
            out.write(bytes(body, 'utf8')) 
