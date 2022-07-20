from micropython import const

from kmk.keys import make_argumented_key
from kmk.modules import Module


class OneShotModKeyMeta:
    def __init__(self, kc):
        self.kc = kc


class OneShotModKeyStatus:
    PHYSICALLY_PRESSED = const(0) # Key is physically pressed
    HELD_UNTIL_INTERRUPTED = const(1) # Key is physically released, and mod is logically held until interrupted


class OneShotModReleaseMode:
    ON_INTERRUPT_PRESS = const(0), # Release oneshot mods when first interrupt key is pressed
    ON_INTERRUPT_RELEASE = const(1), # Release oneshot mods when any interrupt key is released
    ON_ALL_INTERRUPT_RELEASE = const(2) # Release oneshot mods when ALL interrupt keys are released


class OneShotMod(Module):
    def __init__(
        self,
        timeout=1000,
        release_mode=OneShotModReleaseMode.ON_INTERRUPT_PRESS,
        cancel_on_repress=False,
        is_ignored_interrupt_key=lambda key: isinstance(key.meta, OneShotModKeyMeta),
    ):
        self.timeout = timeout
        self.release_mode = release_mode
        self.cancel_on_repress = cancel_on_repress
        self.is_ignored_interrupt_key = is_ignored_interrupt_key
        self.timeout_key = None
        self.active_oneshot_mod_keys = {}
        self.active_interrupt_keys = set()
        make_argumented_key(
            validator=OneShotModKeyMeta,
            names=('OSM',),
            on_press=self.osm_pressed,
            on_release=self.osm_released,
        )

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, current_key, is_pressed, int_coord):
        if (self.active_oneshot_mod_keys
            and is_pressed
            and current_key not in self.active_interrupt_keys
            and not self.is_ignored_interrupt_key(current_key)
        ):
            # New interrupt key pressed
            self.active_interrupt_keys.add(current_key)
            if self.timeout_key:
                keyboard.cancel_timeout(self.timeout_key)
            if self.release_mode == OneShotModReleaseMode.ON_INTERRUPT_PRESS:
                keyboard.pre_process_key(current_key, True)
                keyboard._send_hid()
                self.release_oneshot_mods(keyboard)
                return None
        elif current_key in self.active_interrupt_keys and not is_pressed:
            # Active interrupt key released
            self.active_interrupt_keys.remove(current_key)
            if (self.release_mode == OneShotModReleaseMode.ON_INTERRUPT_RELEASE or not self.active_interrupt_keys):
                keyboard.pre_process_key(current_key, False)
                keyboard._send_hid()
                self.release_oneshot_mods(keyboard)
                return None

        return current_key

    def osm_pressed(self, key, keyboard, *args, **kwargs):
        if (self.cancel_on_repress and key in self.active_oneshot_mod_keys):
            del self.active_oneshot_mod_keys[key]
        else:
            self.active_oneshot_mod_keys[key] = OneShotModKeyStatus.PHYSICALLY_PRESSED

        keyboard.process_key(key.meta.kc, True)
        return keyboard

    def osm_released(self, key, keyboard, *args, **kwargs):
        if key not in self.active_oneshot_mod_keys:
            # If the oneshot mod key is no longer active, then ensure its mod is released
            keyboard.process_key(key.meta.kc, False)
        else:
            # If oneshot mod key is still active, then track it as held until interrupted
            self.active_oneshot_mod_keys[key] = OneShotModKeyStatus.HELD_UNTIL_INTERRUPTED
            if self.timeout_key:
                keyboard.cancel_timeout(self.timeout_key)
            # If there are no active interrupt keys, then reset the oneshot mod timeout
            if not self.active_interrupt_keys:
                self.tieout_key = keyboard.set_timeout(self.timeout, lambda: self.release_oneshot_mods(keyboard))

        return keyboard

    def release_oneshot_mods(self, keyboard):
        for key, state in self.active_oneshot_mod_keys.items():
            if state == OneShotModKeyStatus.HELD_UNTIL_INTERRUPTED:
                    keyboard.process_key(key.meta.kc, False)
        self.active_interrupt_keys.clear()
        self.active_oneshot_mod_keys.clear()