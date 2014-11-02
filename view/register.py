import web
import hashlib
import re
from os import urandom
from model.repositories.user_repository import UserRepository
from model.repositories.mongo_wrapper import MongoWrapper


class Register:
    def __init__(self):
        self.user_repository = UserRepository(MongoWrapper())
        self.register_form = web.form.Form(
            web.form.Textbox('username', description="Username"),
            web.form.Password('password', description="Password"),
            web.form.Password('retype_password', description="Retype Password"),
            web.form.Button('register', html='Register')
        )
        self.render = web.template.render('templates', globals())

    def GET(self):
        return self.render.register(self.register_form)

    def POST(self):
        if not self.register_form.validates():
            return self.render.register(self.register_form)

        username = self.register_form.d.username
        password = self.register_form.d.password
        salt = urandom(64).encode('hex')
        hexdigest = hashlib.sha256(salt + password).hexdigest()

        self.user_repository.create_user(username, hexdigest, salt)
        raise web.seeother('/login')
