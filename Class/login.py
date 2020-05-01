class login(): 

    def __init__(self, *args, **kwargs):
        self.__username = kwargs.get('username', 'admin') 
        self.__password = kwargs.get('password', 'admin123') 
        
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, username):
        self.__username = username
        
    @property
    def password(self):
        return self.__password
        
    @password.setter
    def password(self, password):
        self.__password = password
        
