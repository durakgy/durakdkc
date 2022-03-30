def on_button_pressed_a():
    global text_list
    text_list = ["A",
        "b",
        "c",
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
        "k"]
    basic.show_string("" + (text_list._pick_random()))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

text_list: List[str] = []
basic.show_icon(IconNames.HEART)