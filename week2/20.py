from abc import ABC,abstractmethod
class UserAuthentication:
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in using Google Auth")
    def logout(self):
        print("Logged out using Google Auth")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in using Facebook Auth")
    def logout(self):
        print("Logged out using Facebook Auth")
g=GoogleAuth()
f=FacebookAuth()
g.login()
g.logout()
f.login()
f.logout()