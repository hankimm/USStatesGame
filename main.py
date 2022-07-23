import turtle
import pandas as p

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = p.read_csv("50_states.csv")
all_states = data.state.to_list()
number_of_states = 50
number_correct = 0
guessed_states = []

while len(guessed_states) < 50:
    # .title() method converts OHIO to Ohio
    answer_state = screen.textinput(title=f"{number_correct}/50 States Correct",
                                    prompt="What's another state's name").title()
    print(all_states)
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = p.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        number_correct += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_coord = data[data.state == answer_state]
        t.goto(int(state_coord.x), int(state_coord.y))
        t.write(answer_state)
