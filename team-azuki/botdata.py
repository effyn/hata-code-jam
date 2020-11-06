import json
import threading
import time


class BotData(dict):
    def __init__(self, path: str, min_wait: int = 10, force_save_mods: int = 5):
        self.path = path
        self.min_wait = min_wait
        self._force_save_mods = force_save_mods
        self._last_save = 0
        self._mods = 0

        try:
            with open(self.path) as f:
                super().__init__(**json.load(f))
        except FileNotFoundError:
            with open(self.path, 'w') as f:
                super().__init__()
                f.write('{}')
        
        self._last_save = time.time()

    def __setitem__(self, key, value):
        try:
            if self[key] != value:
                if value is None:
                    del self[key]
                else:
                    super().__setitem__(key, value)
                self._mods += 1
                self._check_save()
        except KeyError:
            if value is not None:
                super().__setitem__(key, value)
                self._mods += 1
                self._check_save()

    def __delitem__(self, key):
        try:
            del self[key]
            self._mods += 1
            self._check_save()
        except KeyError:
            pass

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return None

    def __missing__(self, key):
        return None

    def _check_save(self):
        now = time.time()
        if self._mods >= self._force_save_mods or now >= self._last_save + self.min_wait:
            self.save()
            self._last_save = now

    def save(self):
        if self._mods > 0:
            with open(self.path, 'w') as f:
                json.dump(self, f)
            self._mods = 0
