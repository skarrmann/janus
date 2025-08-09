from kmk.keys import Key, make_argumented_key
from kmk.modules import Module


class OneShotKey(Key):
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        self.key = key


class OneShot(Module):
    def __init__(self):
        self.ignore_keys = []
        self.oneshot_active = False
        self.queued_oneshot_keys = set()
        make_argumented_key(names=('OS',), constructor=OneShotKey, on_press=self.osk_pressed, on_release=self.osk_released)

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return
    
    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def set_ignore_keys(self, ignore_keys):
        self.ignore_keys = ignore_keys

    def set_cancel_keys(self, cancel_keys):
        self.cancel_keys = cancel_keys

    def process_key(self, keyboard, current_key, is_pressed, int_coord):
        if self.oneshot_active and not isinstance(current_key, OneShotKey) and current_key not in self.ignore_keys and is_pressed:
            self.oneshot_active = False
            for key in self.queued_oneshot_keys:
                keyboard.resume_process_key(self, key.key, False)
            self.queued_oneshot_keys.clear()
        return current_key

    def osk_pressed(self, key, keyboard, *args, **kwargs):
        self.oneshot_active = True
        keyboard.resume_process_key(self, key.key, True)
        return keyboard

    def osk_released(self, key, keyboard, *args, **kwargs):
        if self.oneshot_active:
            self.queued_oneshot_keys.add(key)
        else:
            keyboard.resume_process_key(self, key.key, False)
        return keyboard