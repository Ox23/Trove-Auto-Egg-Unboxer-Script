import time
from pynput.mouse import Button, Controller

mouse = Controller()


def current_mouse_pose():
    print('The current pointer position is {0}'.format(mouse.position))


def move_pose(x, y):
    mouse.position = (x, y)
    print('The pointer was moved to {0}'.format(mouse.position))


def click_left():
    mouse.press(Button.left)
    mouse.release(Button.left)
    print('Clicked the left mouse button')


def click_right():
    mouse.press(Button.right)
    wait(1)
    mouse.release(Button.right)
    print('Clicked the right mouse button')


def wait(time_s):
    time.sleep(time_s)
    print('waited {0} seconds'.format(time_s))


def action():
    # put all the eggs in the incubator
    wait(2)
    move_pose(1846, 154)
    wait(0.5)
    for x in range(10):
        wait(0.2)
        click_left()
    wait(0.5)
    for x in range(10):
        wait(0.2)
        click_right()
    # hatch all eggs
    wait(3.5)
    move_pose(640, 452)
    wait(0.5)
    click_left()
    move_pose(961, 453)
    wait(0.5)
    click_left()
    move_pose(1275, 456)
    wait(0.5)
    click_left()

    wait(3)
    '''
    # click OK
    move_pose(610, 666)
    click_left()

    move_pose(966, 661)
    click_left()

    move_pose(1295, 662)
    click_left()
    '''
    # reset attempt
    move_pose(1766, 156)
    for x in range(5):
        wait(0.2)
        click_left()


while True:
    action()
