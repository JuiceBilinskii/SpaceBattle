from tortilla.models.model import Model, ActionsCapturer
from tortilla.widgets.widget_models import Button, ToggleButton
from tortilla.constants import *


class SettingsMenu(Model):
    def __init__(self):
        self._config = {
            'FULL SCREEN': FULL_SCREEN
        }

        self._config_file = 'tortilla\\config.json'

        self._buttons = [
            ToggleButton(self.__change_screen_mode, self._config['FULL SCREEN']),
            Button(self.__accept_changes),
            Button(lambda: 'main_menu')
        ]
        self._buttons[2].active = True

    def __change_screen_mode(self):
        self._config['FULL SCREEN'] = not self._config['FULL SCREEN']

    def __accept_changes(self):
        with open(self._config_file, 'w') as fp:
            json.dump(self._config, fp, indent=4)

    def update(self, actions: ActionsCapturer):
        if actions.key_a:
            for button in self._buttons:
                if button.active:
                    return button.execute()
        elif actions.key_down:
            for i, button in enumerate(self._buttons):
                if self._buttons[i].active:
                    if i == len(self._buttons) - 1:
                        break
                    self._buttons[i].active = False
                    self._buttons[i + 1].active = True
                    break
        elif actions.key_up:
            for i, button in enumerate(self._buttons):
                if self._buttons[i].active:
                    if i == 0:
                        break
                    self._buttons[i].active = False
                    self._buttons[i - 1].active = True
                    break

    @property
    def buttons(self):
        return self._buttons
