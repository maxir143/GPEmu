from GPEmu import GamePad


def main():
    # create game pad
    gamepad = GamePad()
    # start game pad
    gamepad.connect()

    # check if 'RT' is a trigger
    if 'RT' in gamepad.triggers:
        # set the trigger <'RT'> to <0.5> and update is <true> (so, don't need to call GamePad.update() later)
        gamepad.set_trigger('RT', .5, True)
    # Press button <'A'> and <'B'>
    gamepad.press_button('A')
    gamepad.press_button('B')

    # Update all the changes made that hasn't been updated to the controller at one
    gamepad.update()

    # set button <'B'> press to <False> and update the controller
    gamepad.button('B', False, True)

    # Gamepad disconnect
    gamepad.disconnect()


if __name__ == '__main__':
    main()