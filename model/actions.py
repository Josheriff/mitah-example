class Action():
    def __init__(self, persistence_controller):
        self.persistence_controller = persistence_controller

    def begin(self):
        print(' LOGUEADO CORRECTAMENTE ESTAS SON TUS OPCIONES')
    
    def ask_accept(self, user):
        for name in user['friend_request']:
            friendship = input(f'¿Quieres aceptar a {name} como amigo?')
            if friendship.upper() == 'S':
                self.persistence_controller.add_friend(user, name)