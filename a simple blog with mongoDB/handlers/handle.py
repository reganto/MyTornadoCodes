#*****************************A Simple Blog*************************************
# -*- coding:UTF-8 -*-
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import json
from pymongo import MongoClient
#**************************
# #from bson import ObjectId
# from tornado.options import define, options
#
#
#
# #************************ connect to mongodb************************************
# #*************************create client for mongo*******************************
# client = MongoClient('localhost', 27017)
# #*********************** create a new database**********************************
# db = client.pyblogdb
# #*******************************end*********************************************
#
#
#
# #************************** define port*****************************************
#
# define("port", default=8888, help="run on the given port", type=int)
#
# #*********************************end*******************************************


#*********************************Main******************************************

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "index.html",
        page_title = "Reganto Blog | Home",
        index_header = "Python Blog",
        intro_text = "",
        primary_paragraph = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
        soton1_p1 = "The interp is typing Control-P to the first Python prompt you get.",
        soton1_p2 = "If you’re a professional software developer, you may have to work with several C,C++,Java libraries.",
        soton1_p3 = "Python is an interpreted language, which can save you considerable time during program development.",
        soton2_p1 = "Python allows you to split your program into modules that can be reused in other Python programs.",
        soton2_p2 = "Python is extensible if you know how to program in C it is easy to add a new built-in function or module to the interpreter.",
        soton2_p3 = "Examine Python in some more detail  extensible if you know how to program in C it is easy to add a new built-in function.",
        soton3_p1 = "By default, Python source files are Python source files are Python source files are treated as encoded in UTF-8.",
        soton3_p2 = "The interprete  extensible if you know how to program in C it is easy to add a new built-in function.",
        soton3_p3 = "The interp is typing Control-P to the first Python prompt you get.",
        )


#************************************end****************************************



# ***********************************Login**************************************

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "login.html",
        )

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        coll = self.application.db.user
        information = coll.find_one()
        #self.write(username)
        #self.write(password)

        if password == str(information["password"]) and username == str(information["username"]):
            self.render(
                "dashboard.html",
                page_title = "Dashboard"
                )
        else:
            #******************************************
            self.redirect('/login')

# ***********************************end****************************************




# ************handle data that sent from contact form in contact page***********

class ContactHandler(tornado.web.RequestHandler):

    # render contact page
    def get(self):
        self.render(
        "contact_page.html",
        page_title = "Reganto Blog | Contact Us",
        )

    def post(self):
        # get name and email and comment from contact form
        x = self.get_argument('name')
        y = self.get_argument('email')
        z = self.get_argument('txt')
        # create a collection named contacts
        contacts = self.application.db.contacts
        # create a dict from user information to insert in database
        info_doc = {"name":x, "email":y, "comment":z}
        contacts.insert_one(info_doc)
        # get a query from db to show current info to current user
        contact_query = contacts.find_one({"name":x, "email":y})
        # del primary key from query
        del contact_query["_id"]
        # create a log file
        #                   **************************
        #print(ObjectId())
        log_file = open("comments.json", "a")
        log_file.write(json.dumps(contact_query)+"\n")
        log_file.close()
        # render contact_result.html
        # self.render(
        # "contact_result.html",
        # page_title = "...",
        # user_info=contact_query,
        # )
        self.redirect("/")

# **********************************end*****************************************



# *****************************handle aside links*******************************

class WhettingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "whetting.html",
        page_title = "Reganto Blog | Whetting Your Appetite",
        )

class InterpreterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "py_interpreter.html",
        page_title = "Reganto Blog | Python Interpreter",
        )

class IntroHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "intro.html",
        page_title = "Reganto Blog | An Informal Introduction to Python",
        )

class ControlFlowHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "control_flow.html",
        page_title = "reganto Blog | More Control Flow Tools",
        )

class ModulesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'modules.html',
            page_title = 'Reganto Blog | modules',
        )

class DSHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'data_structure.html',
            page_title = "Reganto Blog | Data Structures",
        )


class IOHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'io.html',
            page_title = 'Reganto Blog | I/O',
        )

class ErrorHander(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'error.html',
            page_title = 'Reganto Blog | Error And Exceptions',
        )

class ClassesHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            'classes.html',
            page_title = 'Reganto Blog | Classes',
        )

# **********************************end*****************************************




# ****************************handle bottom links*******************************

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "about_page.html",
        page_title = "Reganto Blog | About",
        index_header = "About us",
        intro_text = "",
        primary_paragraph = "",
        )

class LatestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "latest_python.html",
        page_title = "Reganto Blog | Download",
        py_ver = "python3-6-3.deb",
        )


class LegalHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "legal.html",
        page_title = "Reganto Blog | Legal Information",
        )

class CopyrightHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "copyright.html",
        page_title = "Reganto Blog | Copyright",
        )

class PrivacyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
        "privacy.html",
        page_title = "Reganto Blog | Privacy Policy",
        )

# ***********************************end****************************************




# **********************************CommentsHandler*****************************


class CommentsHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.contacts
        comments = coll.find()
        self.render(
        "view_comments.html",
        comments = comments,
        page_title = " ",
        )

class View_commentModule(tornado.web.UIModule):
    def render(self, comment):
        return self.render_string(
        "modules/comment.html",
        comment = comment,
        page_title = " ",
        )

#class DelComHandler(tornado.web.RequestHandler):
#    def post(self):
#        self.render(
#
#        )
#        name = self.get_argument("name")

# *********************************end******************************************




# *********************************Modify Password******************************

class ModifyPassword(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "password_mod.html",
        )

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        newpasswd = self.get_argument("newpasswd")

        coll = self.application.db.user
        information = coll.find_one()
        #self.write(username)
        #self.write(password)

        if password == str(information["password"]) and username == str(information["username"]):
            information["password"] == newpasswd
            coll.save(information)
            self.render(
                "dashboard.html",
                page_title = "dashboard",
            )
        else:
            self.redirect('/password')

# *************************************end**************************************




# **********************************post edit***********************************

class PostEditHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "post_edit.html",
            page_title = "post edit",
        )

# ************************************end***************************************




# ********************************Compose***************************************
#
class ComposeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "newpost.html",
            page_title = "Compose",
        )

    def post(self):
        p_title = self.get_argument('post_title')
        p_content = self.get_argument('post_content')
        coll = self.application.db.pages
        coll.insert_one(p_title, p_content)

        # coll = self.application.db.pages
        # sample = [p_title, p_content]
        # coll.insert_one(sample)
        # self.write(sample)
        # self.render(
        #     'index.html',
        #     soton1_p1 = p_title,
        #     page_title = 'POST',
        #     index_header = ' ',
        #     intro_text = ' ',
        #     primary_paragraph = ' ',
        # )


#     def post(self):
#         post_title = self.get_argument("post_title")
#         post_content = self.get_argument("post_content")
#         self.render(
#         "index.html",
#         page_title = "Reganto Blog | Home",
#         index_header = "Python Blog",
#         intro_text = "",
#         primary_paragraph = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.",
#         soton1_p1 = post_title,
#         soton1_p2 = "If you’re a professional software developer, you may have to work with several C,C++,Java libraries.",
#         soton1_p3 = "Python is an interpreted language, which can save you considerable time during program development.",
#         soton2_p1 = "Python allows you to split your program into modules that can be reused in other Python programs.",
#         soton2_p2 = "Python is extensible if you know how to program in C it is easy to add a new built-in function or module to the interpreter.",
#         soton2_p3 = "Examine Python in some more detail  extensible if you know how to program in C it is easy to add a new built-in function.",
#         soton3_p1 = "By default, Python source files are Python source files are Python source files are treated as encoded in UTF-8.",
#         soton3_p2 = "The interprete  extensible if you know how to program in C it is easy to add a new built-in function.",
#         soton3_p3 = "The interp is typing Control-P to the first Python prompt you get.",
#         )

# ************************************end***************************************
