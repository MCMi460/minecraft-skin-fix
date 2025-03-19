from . import get

class Minecraft:
    class Skin:
        names = {}
    class Cape:
        names = {}
    Cloak = Cape
    
    class Player:
        class _Skin:
            def __init__(self, username:str):
                self.username = username
            def replace(self, new:str):
                """
                Replace this user's skin with another user's skin
                """
                Minecraft.Skin.names[self.username] = new
        class _Cape:
            def __init__(self, username:str):
                self.username = username
            def replace(self, new:str):
                """
                Replace this user's cape with another user's cape
                """
                Minecraft.Cape.names[self.username] = new
                
        def __init__(self, username:str):
            self.username = username
            self.Skin = self._Skin(username)
            self.Cape = self._Cape(username)
            self.Cloak = self.Cape
        
        def replace(self, username:str):
            self.Skin.replace(username)
            self.Cape.replace(username)
