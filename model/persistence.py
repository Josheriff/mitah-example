import json
import os
class Persistence():
    def save_user(self, user):
        name = user['name']
        with open(f'./persistence/{name}.json', 'w') as file:
            json.dump(user,file)
    
    def get_all_users(self):
        return os.listdir('./persistence')
            