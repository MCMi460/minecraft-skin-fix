from skin_fix import Proxy, Minecraft

if __name__ == '__main__':
    ### Optional ###
    player = Minecraft.Player('Arten') # Your username here
    player.Skin.replace('Technoblade') # The replacement skin you want
    player.Cape.replace('Drullkus') # The replacement cape you want
    player.replace('Marc') # Or, replace them both at once

    ### Necessary ###
    server = Proxy() # Create the localhost proxy
    server.start() # Then start the server!
