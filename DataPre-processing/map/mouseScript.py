from pynput import mouse
from pynput import keyboard
from pynput.mouse import Button, Controller
import time
import os


def on_press(key):
    try:
        print('alphanumeric key  {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


# ==========================================================


def on_move(x, y):
    print('Pointer moved to {o}'.format(
        (x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False


def on_scroll(x, y, dx, dy):
    print('scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


def ckck(a, b):
    mouse.position = (a, b)
    mouse.press(Button.left)
    mouse.release(Button.left)


def one_round_map(dirname):
    ckck(1382, 435)
    ckck(1519, 728)
    ckck(1878, 580)
    keyboard.type(
        'C:\\Users\\Dadada\\Documents\\wgeWorldHistory\\DataPre-processing\\map\\allOKmaps\\'+dirname+'map.png')
    time.sleep(2)
    ckck(1800, 740)
    ckck(1648, 644)
    ckck(1880, 572)
    ckck(1796, 746)
    ckck(1656, 643)
    ckck(1523, 604)
    ckck(1970, 1069)
    ckck(1626, 715)
    ckck(1626, 715)
    ckck(1946, 1078)
    keyboard.type(
        'C:\\Users\\Dadada\\Documents\\wgeWorldHistory\\DataPre-processing\\map\\mapball\\'+dirname)
    time.sleep(2)
    ckck(1069, 549)
    ckck(1865, 577)
    time.sleep(20)
    ckck(1848, 1081)
    ckck(1849, 1070)
    ckck(1177, 1006)
    ckck(1193, 992)
    ckck(1797, 1067)


if __name__ == '__main__':
    allyears = os.listdir('mapballs')
    # mouseScript
    mouse = mouse.Controller()
    keyboard = keyboard.Controller()
    thexthball = 1
    for i in allyears:
        one_round_map(i)
        print(thexthball, 'ball,', i, 'ok!!')
        with open('log.txt', 'a') as the_file:
            the_file.write(i+'\n')
        thexthball += 1
    # mouseScript

    # print(mouse.position)

    # # 監控滑鼠
    # while True:
    #     with mouse.Listener(no_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    #         listener.join()
    # # 監控滑鼠
