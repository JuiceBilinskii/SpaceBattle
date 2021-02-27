from data.models.imodel import IModel, ActionsCapturer
from data.jump_commands import GameCommand, SettingsMenuCommand, QuitCommand
from data.widgets.interface_elements import Button


class MainMenu(IModel):
    def __init__(self):
        self.buttons = [
            Button(GameCommand),
            Button(SettingsMenuCommand),
            Button(None),
            Button(QuitCommand)
        ]
        self.buttons[0].active = True

    def update(self, actions: ActionsCapturer):
        if actions.key_left:
            for i in range(1, len(self.buttons)):
                if self.buttons[i].active:
                    self.buttons[i].active = False
                    self.buttons[i - 1].active = True
                    break
        elif actions.key_right:
            for i in range(0, len(self.buttons) - 1):
                if self.buttons[i].active:
                    self.buttons[i].active = False
                    self.buttons[i + 1].active = True
                    break
        elif actions.key_a:
            # return GameCommand.execute()
            for button in self.buttons:
                if button.active:
                    return button.execute()
