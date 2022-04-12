import random

from handlers.base import BaseHandler

class ManageAlphaHandler(BaseHandler):
    def prepare(self):
        if "Firefox" in self.request.headers['user-agent']:
            pass
        else:
            exit(0)
    
    def get(self):
        self.render('alpha/alpha.html')

    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped
    
    def post(self):
        source_text = self.get_body_argument('source')
        text_to_change = self.get_body_argument('change')
        source_map = self.map_by_first_letter(source_text)
        # self.write(str(source_map))
        change_lines = text_to_change.split('\r\n')

        self.render(
            'alpha/munged.html',
            source_map=source_map,
            change_lines=change_lines,
            choice=random.choice
        )