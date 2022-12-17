import turtle
import pandas

screen = turtle.Screen()
screen.title("USA STATES GAME")

# image background
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# IMPORTANT: code for getting thre chick coors!!!
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
score = 0

prompt = "Whats another state name"

data = pandas.read_csv('50_states.csv')

all_states = data.state.to_list()
print(all_states)


def pin_state(state, x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(state)


while all_states:

    guess = f"Guess a states: {score}/50"

    answer = screen.textinput(title=guess, prompt=prompt)
    answer = answer.title()

    if answer == 'Exit':  # not working yet, stops and need to be rewiten 'exit'
        # TODO: when user gets out of the game pin all states missing
        for estado in all_states:
            state_data = data[data.state == estado]
            print(state_data)
            pin_state(estado, int(state_data.x), int(state_data.y))
            all_states.remove(estado)

    if answer in all_states:
        state_data = data[data.state == answer]
        pin_state(answer, int(state_data.x), int(state_data.y))

        all_states.remove(answer)
        score += 1

turtle.mainloop()
