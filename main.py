import time
import random
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

INITIAL_WAIT_TIME = 5
NUMBER_OF_VOTES = 5
REQUIRED_WAIT_TIME = 10


def main() -> None:
    """ 
    A Python script that clicks on or near the position of the mouse NUMBER_OF_VOTES times.
    The user has INITIAL_WAIT_TIME seconds to place their mouse at the desired position.
    """

    time.sleep(INITIAL_WAIT_TIME)

    mouse_coords = get_mouse_coords()

    vote(mouse_coords[0], mouse_coords[1], NUMBER_OF_VOTES)


def get_mouse_coords() -> tuple:
    """ Return the (x, y) coordinates of the mouse. """

    x, y = pyautogui.position()
    print(f"The mouse coordinates are ({x}, {y})")

    return (x, y)


def vote(x: int, y: int, number_of_votes: int) -> None:
    """ 
    Click the mouse approximately at point (x, y) number_of_votes times.
    Wait a short, random amount of time after each click.
    """

    for i in range(1, number_of_votes + 1):
        shifted_x = x + random.randint(-2, 2)
        shifted_y = y + random.randint(-2, 2)

        pyautogui.click(shifted_x, shifted_y)

        if (i % 10) == 0:
            print(f"Clicked {i} times!")

        random_wait_time = REQUIRED_WAIT_TIME + random.randint(1, 5)
        time.sleep(random_wait_time)


if __name__ == '__main__':
    main()
