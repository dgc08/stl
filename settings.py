from modules.stdlib.utils import SettingsHelper

helper = SettingsHelper.helper

from modules.settings.promt import promt

class Root_Settings:
    appereance_settings = {"promt":promt}

    root_settings = {"look":appereance_settings}
    def get_Setting(self, dict, name):
        return self.root_settings[dict][name]()
