from modules.stdlib.utils.SettingsHelper import helper
from os import name
from modules.settings.promt import promt


appereance_settings = {
#Setting:look
    "prompt":promt
#Settings:look-end
}

system_settings = {
#Settings:system
    "base-shell":helper("/bin/sh -c '"), # start of the call of the base shell which is executed
    "base-shell-end":helper("'")         # end of the call of the base shell which is executed ( in the middle is the actual command
#Setting:system-end
}

if name == "nt":
    system_settings["base-shell"] = helper("cmd /c \"")
    system_settings["base-shell-end"] = helper("\"")

class Root_Settings:


    root_settings = {"look":appereance_settings, "system":system_settings}
    def get_Setting(self, dict, name):
        return self.root_settings[dict][name]()
