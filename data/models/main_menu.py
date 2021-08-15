from data.models.model import Model, ActionsCapturer
from data.widgets.widget_models import Button


class MainMenu(Model):
    def __init__(self):
        self._commands = {
            'game': lambda: 'game',
            'settings_menu': lambda: 'settings_menu',
            'score_menu': lambda: 'score_menu',
            'quit': lambda: 'quit'
        }

        self._buttons = [
            Button(self._commands['game']),
            Button(self._commands['settings_menu']),
            Button(self._commands['score_menu']),
            Button(self._commands['quit'])
        ]
        self._buttons[0].active = True

    def update(self, actions: ActionsCapturer):
        if actions.key_left:
            for i, button in enumerate(self._buttons):
                if self._buttons[i].active:
                    if i == 0:
                        break
                    self._buttons[i].active = False
                    self._buttons[i - 1].active = True
                    break
        elif actions.key_right:
            for i, button in enumerate(self._buttons):
                if self._buttons[i].active:
                    if i == len(self._buttons) - 1:
                        break
                    self._buttons[i].active = False
                    self._buttons[i + 1].active = True
                    break
        elif actions.key_a:
            for button in self._buttons:
                if button.active:
                    return button.execute()

    @property
    def buttons(self):
        return self._buttons
