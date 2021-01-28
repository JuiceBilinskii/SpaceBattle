from data.icommand import ICommand


class MainMenuCommand(ICommand):
    @staticmethod
    def execute():
        return 'main_menu'


class SettingsMenuCommand(ICommand):
    @staticmethod
    def execute():
        return 'settings_menu'


class GameCommand(ICommand):
    @staticmethod
    def execute():
        return 'game'


class QuitCommand(ICommand):
    @staticmethod
    def execute():
        return 'quit'
