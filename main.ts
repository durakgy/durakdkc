input.onButtonPressed(Button.A, function () {
    text_list = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "G",
    "K",
    "L",
    "I",
    "J",
    "k"
    ]
    basic.showString("" + (text_list._pickRandom()))
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
})
let text_list: string[] = []
basic.showIcon(IconNames.Heart)
