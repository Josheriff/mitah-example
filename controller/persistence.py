class PersistenceController():
    def __init__(self, persistence_model):
        self.persistence_model = persistence_model
    def save_user(self, user):
        self.persistence_model.save_user(user)