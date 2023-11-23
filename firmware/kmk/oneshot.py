from kmk.keys import make_argumented_key
from kmk.modules import Module


class OneShotKeyMeta:
    def __init__(self, kc):
        self.kc = kc


class OneShot(Module):
    def __init__(self):
        self.ignore_keys = []
        self.oneshot_active = False
        self.queued_oneshot_keys = set()
        make_argumented_key(validator=OneShotKeyMeta, names=('OS',), on_press=self.osk_pressed, on_release=self.osk_released)

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
        if self.oneshot_active and not isinstance(current_key.meta, OneShotKeyMeta) and current_key not in self.ignore_keys and is_pressed:
            self.oneshot_active = False
            for key in self.queued_oneshot_keys:
                keyboard.resume_process_key(self, key.meta.kc, False)
            self.queued_oneshot_keys.clear()
        return current_key

    def osk_pressed(self, key, keyboard, *args, **kwargs):
        self.oneshot_active = True
        keyboard.resume_process_key(self, key.meta.kc, True)
        return keyboard

    def osk_released(self, key, keyboard, *args, **kwargs):
        if self.oneshot_active:
            self.queued_oneshot_keys.add(key)
        else:
            keyboard.resume_process_key(self, key.meta.kc, False)
        return keyboard