input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.temperature())
})
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
    basic.pause(100)
    basic.showIcon(IconNames.Sad)
    basic.pause(100)
    basic.showIcon(IconNames.Surprised)
    basic.pause(100)
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    basic.showIcon(IconNames.House)
})
basic.forever(function () {
    basic.showLeds(`
        . # . # .
        # # # # #
        . # # # .
        . . # . .
        . . . . .
        `)
    basic.clearScreen()
    basic.pause(100)
})
basic.forever(function () {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        . # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        . # # # #
        . . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    basic.showLeds(`
        . # # # #
        . . . . #
        . . . . #
        # . . . #
        # # # # #
        `)
})
