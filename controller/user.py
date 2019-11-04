class UserController():
    def __init__(self, user_model):
        self.user_model = user_model
    def register(self):
        self.user_model.register()