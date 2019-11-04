import json
import os
class Persistence():
    def save_user(self, user):
        name = user['name']
        with open(f'./persistence/{name}.json', 'w') as file:
            json.dump(user,file)
    
    def get_all_users(self):
        return os.listdir('./persistence')
    
    def get_user(self, name):
        with open(f'./persistence/{name}.json', 'r') as file:
            return json.load(file)