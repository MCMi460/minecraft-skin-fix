from . import search, b64decode

class Minecraft:
    def install_proxy(version:str = None):
        """
        Adds the proxy address and port to the most recent
        applicable version available in the default launcher
        """
        raise NotImplementedError
    
    def parse_head_command(command:str):
        """
        Parses a /give command for a player head to take
        its texture. Get these commands from NameMC
        """
        base64 = search(
            r'value:"((?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{4}|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}={2}))"',
            command
        )
        if base64:
            texture = search(
                r'[0-9a-fA-F]{17,}\b',
                b64decode(base64[1]).decode('UTF-8')
            )
            return texture[0]
        else:
            raise Exception('invalid head /give command')

    class Skin:
        """
        Format:
        'name': (type:int, value:str)
        type
            0: username
            1: texture UUID
        """
        names = {}
    class Cape:
        """
        Format: See Minecraft.Skin
        """
        names = {}
        defaults = { # Must be manually updated due to limitations on scraping
            'Migrator': '2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933',
            '15th Anniversary': 'cd9d82ab17fd92022dbd4a86cde4c382a7540e117fae7b9a2853658505a80625',
            'Vanilla': '2b24a33d2e8d9d0572c61ec34e9f86a1cfc4ca49d417d4d51ab085862364785c',
            'Cherry Blossom': 'afd553b39358a24edfe3b8a9a939fa5fa4faa4d9a9c3d6af8eafb377fa05c2bb',
            'Purple Heart': 'cb40a92e32b57fd732a00fc325e7afb00a7ca74936ad50d8e860152e482cfbde',
            'Follower\'s': '569b7f2a1d00d26f30efe3f9ab9ac817b1e6d35f4f3cfb0324ef2d328223d350',
            'Mojang Office': '5c29410057e32abec02d870ecb52ec25fb45ea81e785a7854ae8429d7236ca26',
            'MCC 15th Year': '56c35628fe1c4d59dd52561a3d03bfa4e1a76d397c8b9c476c2f77cb6aebb1df',
            'TikTok Menace': 'b1fc59bc3de3cda3ed4d99c3d65b721c57cec900ece350cbda6f451099e078e7',
            'Twitch Home': '4b5de481e1b41f51c678155ff965c7e9526c7c641aaaf97a501916c7cb101c4b',
            'Minecraft Experience': '7658c5025c77cfac7574aab3af94a46a8886e3b7722a895255fbf22ab8652434',
            'MineCon 2016': 'e7dfea16dc83c97df01a12fabbd1216359c0cd0ea42f9999b6e97c584963e980',
            'MineCon 2015': 'eda49541b93f4ea25ece947638c36d1674ff166077ac0756ebd7df93ea9d9254',
            'MineCon 2013': '153b1a0dfcbae953cdeb6f2c2bf6bf79943239b1372780da44bcbb29273131da',
            'MineCon 2012': 'efd61c3c4ac88f1a3468fbdeef45cec89e5afb87b97a1a845bfb3c64fd0b883',
            'MineCon 2011': 'b767d48325ea5324561406b8c82abbd4e2755f11153cd85ab0545cc2',
            'Realms Mapmaker': '43a51d34b076f9ada555dca562206bd942e46a3c4d5f83c2c29e5b9c3d7dbcb',
            'Mojang': '981d21e07adeab1ca4796b9e2220bfc09ceee5c87ee73547d7eae61d154f98',
            'Mojang Studios': '9e507afc56359978a3eb3e32367042b853cddd0995d17d0da995662913fb00f7',
            'Translator': '1bf91499701404e21bd46b0191d63239a4ef76ebde88d27e4d430ac211df681e',
            'Mojira Moderator': 'f8b55ca322e64a381b6484dac2d8aa42c78c6129336ea3ef4596f1d31b27ef',
            'Mojang (Classic)': '16f3014c6dd1d727521f31848fc6d2c781876b75a282124f3cfbb32370972956',
            'Cobalt': '1672c9f13ece9c4f39a96fe22638ecd513fbe7099ca4354d3176d3793d8e9c7',
            'Scrolls': '3efadf6510961830f9fcc077f19b4daf286d502b5f5aafbd807c7bbffcaca245',
            'Translator (Chinese)': '2262fb1d24912209490586ecae98aca8500df3eff91f2a07da37ee524e7e3cb6',
            'Turtle': '5048ea61566353397247d2b7d946034de926b997d5e66c86483dfb1e031aee95',
            'Valentine': 'e578ef995fabcf0a94768f9651ac3aaba30c59ef85d2438e9b3e0cc1d810652b',
            'Birthday': '2056f2eebd759cce93460907186ef44e9192954ae12b227d817eb4b55627a7fc',
            'dB': 'bcfbe84c6542a4a5c213c1cacf8979b5e913dcb4ad783a8b80e3c4a7d5c8bdac',
            'Millionth Customer': '70efffaf86fe5bc089608d3cb297d3e276b9eb7a8f9f2fe6659c23a2d8b18edf',
            'Prismarine': '746f4f6118ac538db340eb6eddca484dea45b7758391a6aa4fd0149a2f840f1',
            'Snowman': '3d991748ae6e1cfe10f34d532748b1911b1e82b5a110ae89c34f9a2295902e',
            'Spade': 'c08d89a793dcd9815c4b5f4669cd7cfe52d82ba0af7a71690d2d7379e79f368',
            'Translator (Japanese)': 'ca29f5dd9e94fb1748203b92e36b66fda80750c87ebc18d6eafdb0e28cc1d05f'
        }
    Cloak = Cape

    class Player:
        class _Texture:
            def __init__(self, username:str):
                self.username = username
            def replace(self, new:str):
                #namemc_match = search(r'\b[0-9a-fA-F]{16}\b', new)
                cdn_match = search(r'[0-9a-fA-F]{17,}\b', new)
                username_match = search(r'^\w+$', new)
                #if namemc_match: # Note: Accepts just UUID
                # Can't do NameMC support due to Cloudflare
                if cdn_match: # Note: Accepts URL
                    return (1, cdn_match[0])
                elif username_match and 3 <= len(new) <= 16:
                    return (0, new)
                else:
                    raise Exception('invalid replace() input \'%s\'' % new)

        class _Skin(_Texture):
            def replace(self, new:str):
                """
                Replace this user's skin with a specific skin
                Can be defined by username or UUID
                """
                Minecraft.Skin.names[self.username] = super().replace(new)
        class _Cape(_Texture):
            def replace(self, new:str):
                """
                Replace this user's skin with a specific cape
                Can be defined by username or UUID
                """
                Minecraft.Cape.names[self.username] = super().replace(new)
            def choose(self, cape:str):
                """
                Choose a cape from one of Minecraft.Cape.defaults
                """
                Minecraft.Cape.names[self.username] = (1, Minecraft.Cape.defaults[cape])
                
        def __init__(self, username:str):
            self.username = username
            self.Skin = self._Skin(username)
            self.Cape = self._Cape(username)
            self.Cloak = self.Cape
        
        def replace(self, username:str):
            self.Skin.replace(username)
            self.Cape.replace(username)
