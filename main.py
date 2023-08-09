import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "harta-oarba-judete-romania.gif" #turtle works with only .gif format
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("42_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 42:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 Guess state",
                                    prompt="What is another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in data.state if state not in guess_states]
        print(f"States to lean more about:\n{missing_states}")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

# states_df
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()