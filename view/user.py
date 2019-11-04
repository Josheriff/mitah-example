
class UserView():
    def __init__(self, user_controller):
        self.user_controller = user_controller

    def register(self):
        return self.user_controller.register()
