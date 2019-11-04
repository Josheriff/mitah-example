class ActionController():
    def __init__(self, action_model):
        self.action_model = action_model
        
    def begin(self):
        return self.action_model.begin()
    
    def ask_accept(self, user):
        return self.action_model.ask_accept(user)