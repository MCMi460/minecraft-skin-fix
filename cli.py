from skin_fix import Minecraft, SkinFixer

if __name__ == '__main__':
    ### Optional ###
    player = Minecraft.Player('Notch') # Your username here
    player.Skin.replace('Technoblade') # The replacement skin you want
    player.Cape.replace('Drullkus') # The replacement cape you want
    player.replace('Marc') # Or, replace them both at once
    player.Skin.replace('535bdd7eff11c87d52a113c2efb4ca45775e56735dc4b38d7fa1db708458') # You can use a texture UUID
    player.Cape.choose('Cobalt') # Or, for capes, just use its name! (See namemc.com/capes)

    ### Necessary ###
    SkinFixer.start()
