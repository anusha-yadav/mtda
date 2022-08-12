# ---------------------------------------------------------------------------
# MTDA Scripts for IPC227E
# ---------------------------------------------------------------------------
#
# This software is a part of MTDA.
# Copyright (C) 2022 Siemens Digital Industries Software
#
# ---------------------------------------------------------------------------
# SPDX-License-Identifier: MIT
# ---------------------------------------------------------------------------


def ipc227e_enter_bios():
    sleep(5)
    mtda.keyboard.esc()
    mtda.keyboard.esc()
    mtda.keyboard.esc()
    mtda.keyboard.esc()
    mtda.keyboard.esc()
    sleep(1)


def ipc227e_enter_secure_boot_option():
    mtda.keyboard.right()
    mtda.keyboard.down()
    mtda.keyboard.enter()
    sleep(10)


def ipc227e_disable_secure_boot():
    mtda.keyboard.down(3)
    mtda.keyboard.up(2)
    mtda.keyboard.enter()
    mtda.keyboard.up()
    sleep(1)
    mtda.keyboard.enter()


def ipc227e_enable_secure_boot():
    mtda.keyboard.down(3)
    mtda.keyboard.up(2)
    mtda.keyboard.enter()
    mtda.keyboard.down()
    sleep(1)
    mtda.keyboard.enter()


def ipc227e_erase_secure_boot_settings():
    mtda.keyboard.down(3)
    mtda.keyboard.up()
    mtda.keyboard.enter()
    mtda.keyboard.down()
    sleep(1)
    mtda.keyboard.enter()


def ipc227e_apply_secure_boot_settings():
    mtda.keyboard.f10()
    sleep(1)
    mtda.keyboard.enter()
    sleep(1)
    mtda.keyboard.enter()
    sleep(5)


def ipc227e_reset_tpm():
    ipc227e_enter_bios()
    ipc227e_enter_secure_boot_option()
    ipc227e_disable_secure_boot()
    ipc227e_erase_secure_boot_settings()
    ipc227e_apply_secure_boot_settings()
    return 0


def ipc227e_enable_secureboot():
    ipc227e_enter_bios()
    ipc227e_enter_secure_boot_option()
    ipc227e_enable_secure_boot()
    ipc227e_apply_secure_boot_settings()
    return 0


def ipc227e_disable_secureboot():
    ipc227e_enter_bios()
    ipc227e_enter_secure_boot_option()
    ipc227e_disable_secure_boot()
    ipc227e_apply_secure_boot_settings()
    return 0


def ipc227e_boot_from_usb():
    ipc227e_enter_bios()
    mtda.keyboard.right()
    mtda.keyboard.enter()
    sleep(0.5)
    mtda.keyboard.down(10)
    mtda.keyboard.enter()
    mtda.keyboard.idle()
    return 0


def ipc227e_power_on():
    scripts.check_reset_tpm() or \
        scripts.check_disable_secureboot() or \
        scripts.check_enable_secureboot() or \
        scripts.check_boot_from_usb()