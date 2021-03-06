import hashlib

import web
from os import urandom
from model.user_repository import UserRepository, MongoWrapper, UserExists


class Register:
    def __init__(self):
        self.register_form = web.form.Form(
            web.form.Textbox('username', web.form.notnull, description="Username"),
            web.form.Password('password', description="Password"),
            web.form.Password('retype_password', description="Retype Password"),
            web.form.Button('register', html='Register')
        )

    def render_registration_page(self, error=None):
        return web.template.render('templates', globals()).register(error, self.register_form)

    def GET(self):
        return self.render_registration_page()

    def POST(self):
        if not self.register_form.validates():
            return self.render_registration_page()

        username = self.register_form.d.username
        password = self.register_form.d.password
        repassword = self.register_form.d.retype_password

        if password != repassword:
            error = "Passwords do not match"
            return self.render_registration_page(error)

        salt = urandom(64).encode('hex')
        hexdigest = hashlib.sha256(salt + password).hexdigest()

        user_repository = UserRepository(MongoWrapper())
        try:
            user_repository.create_user(username, hexdigest, salt)
        except UserExists:
            return self.render_registration_page(error="Username already exists")

        raise web.seeother('/login')
