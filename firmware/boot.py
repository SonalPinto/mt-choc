import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

# =============================================================
# Dev Mode entry
#
# If the COL1 x ROW1 (top-left key, usually ESC) was pressed, then enter CircuitPython Dev Mode
# Else, turn off all USB enumerations except HID
#

COL = digitalio.DigitalInOut(board.GP28)
COL.switch_to_input(pull=digitalio.Pull.UP)

ROW = digitalio.DigitalInOut(board.GP0)
ROW.switch_to_output(value=False, drive_mode=digitalio.DriveMode.PUSH_PULL)

print(COL.value)

if COL.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_midi.disable()
    usb_hid.enable(boot_device=1)

COL.deinit()
ROW.deinit()
