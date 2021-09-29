def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(100)
    basic.show_icon(IconNames.SAD)
    basic.pause(100)
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(100)
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    basic.show_icon(IconNames.HOUSE)
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . # . # .
                # # # # #
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.clear_screen()
    basic.pause(100)
basic.forever(on_forever2)

def on_forever3():
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        . # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        . # # # #
                . . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.show_leds("""
        . # # # #
                . . . . #
                . . . . #
                # . . . #
                # # # # #
    """)
basic.forever(on_forever3)
