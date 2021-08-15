class WidgetModel:
    def __init__(self, command):
        self._command = command
        self._active = False

    def execute(self):
        return self._command()

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value


class Button(WidgetModel):
    def __init__(self, command):
        super().__init__(command)


class ToggleButton(WidgetModel):
    def __init__(self, command, state: bool):
        super().__init__(command)
        self._enabled = state

    def execute(self):
        self._enabled = not self._enabled
        return super().execute()

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
