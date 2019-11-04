class PersistenceController():
    def __init__(self, persistence_model):
        self.persistence_model = persistence_model
    def save_user(self, user):
        return self.persistence_model.save_user(user)
    def get_user(self, name):
        return self.persistence_model.get_user(name)
    def add_friend(self, user, name):
        return self.persistence_model.add_friend(user, name)