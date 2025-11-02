def on_button_pressed_a():
    global Clicks
    Clicks += 1
    basic.show_number(Clicks)
input.on_button_pressed(Button.A, on_button_pressed_a)

Clicks = 0
Clicks = 0

