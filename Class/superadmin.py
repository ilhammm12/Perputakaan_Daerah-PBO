class Superadmin:

    def __init__(self, *args, **kwargs):
        self.__username = kwargs.get('username','admin')
        self.__password = kwargs.get('password','admin321')

    def set_petugas(self,):
        return

    def username(self, value):
        self.__username = value

    def password(self, value):
        self.__password = value
