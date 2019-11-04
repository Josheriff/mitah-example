from view.user import UserView
from controller.user import UserController
from model.user import User
from controller.persistence import PersistenceController
from model.persistence import Persistence
from controller.actions import ActionController
from model.actions import Action

persistence_model = Persistence()
persistence = PersistenceController(persistence_model)
actions_model = Action(persistence)
actions_controller = ActionController(actions_model)
user_model = User(persistence, actions_controller)
user_controller = UserController(user_model)
userview = UserView(user_controller)


def welcome():
    return input('''Bienvenido, escoje una opción:
    1.- Log in
    2.- Register
    s.- Salir
    
    ''')

option = welcome()

if option == '2':
    userview.register()
if option == '1':
    userview.login()