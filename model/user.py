import os
from customerror.user import (UserAlreadyExists,
                              PasswordTooSort,
                              PasswordsAreNotEqual,
                              IncorrectPassword)

class User():
    def __init__(self, persistence, actions):
        self.persistence = persistence
        self.actions = actions
        
    def register(self):
        name = self._ask_for_name()
        password = self._ask_for_password()        
        self._save_user({'name':name, 'password':password})
    
    def loging(self):
        name = input('introduce tu nombre de usuario')
        password = input('introduce tu contraseña')
        self._check_user_password(name, password)
        self.actions.begin()
    
    def _check_user_password(self, name, password):
        user = self.persistence.get_user(name)
        if user[password] == password:
            return True
        raise IncorrectPassword
    
    def _ask_for_name(self):
        name = input('Digame su nombre de usuario  ')
        self._check_user_name(name)
        return name
    
    def _check_user_name(self, name):
        existing_users = self.persistence.get_all_users()
        if f'{name}.json' in existing_users:
            print('El usuario ya existe  ')
            raise UserAlreadyExists

    def _ask_for_password(self):
        first_password = input('Escribe una contraseña de mínimo 8 caracteres  ')
        self._check_password_len(first_password) 
        second_password = input('Vuelve a escribir la contraseña  ')
        if first_password == second_password:
            return first_password
        else:
            print('las contraseñas no coinciden')
            self._ask_for_password()

    def _check_password_len(self, password):
        if len(password) < 8:
            raise PasswordTooSort

    def _check_equal(self, first_password, second_password):
        if first_password != second_password:
            raise PasswordsAreNotEqual
    
    def _save_user(self, user):
        self.persistence.save_user(user)
