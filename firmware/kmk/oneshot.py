from micropython import const
from kmk.keys import make_argumented_key
from kmk.modules import Module


class OneShotKeyMeta:
    def __init__(self, kc):
        self.kc = kc


class OneShot(Module):
    def __init__(self):
        self.ignore_keys = []
        self.cancel_keys = []
        self.oneshot_active = False
        self.pressed_oneshot_keys = set()
        self.queued_oneshot_keys = set()
        self.interrupt_keys = set()
        make_argumented_key(validator=OneShotKeyMeta, names=('OS',), on_press=self.osk_pressed, on_release=self.osk_released)

    def set_ignore_keys(self, ignore_keys):
        self.ignore_keys = ignore_keys

    def set_cancel_keys(self, cancel_keys):
        self.cancel_keys = cancel_keys

    def process_key(self, keyboard, current_key, is_pressed, int_coord):
        if self.oneshot_active:
            if is_pressed and current_key in self.cancel_keys:
                self.release_oneshot_keys(keyboard)
            elif current_key not in self.ignore_keys:
                if is_pressed:
                    self.interrupt_keys.add(current_key)
                elif current_key in self.interrupt_keys:
                    self.release_oneshot_keys(keyboard)
        return current_key

    def osk_pressed(self, key, keyboard, *args, **kwargs):
        self.oneshot_active = True
        self.pressed_oneshot_keys.add(key)
        keyboard.process_key(key.meta.kc, True)
        return keyboard

    def osk_released(self, key, keyboard, *args, **kwargs):
        if self.oneshot_active:
            self.queued_oneshot_keys.add(key)
        else:
            keyboard.process_key(key.meta.kc, False)
        return keyboard

    def release_oneshot_keys(self, keyboard):
        self.oneshot_active = False
        for key in self.queued_oneshot_keys:
            keyboard.process_key(key.meta.kc, False)
        self.pressed_oneshot_keys.clear()
        self.queued_oneshot_keys.clear()
        self.interrupt_keys.clear()