import pyautogui, time
from PIL import ImageGrab


def hit(key):
    pyautogui.keyDown(key)


def is_collide(key):
    for i in range(400, 415):
        for j in range(530, 555):
            if key[i, j] < 100:
                hit("Down")
                return

    for i in range(300, 620):
        for j in range(640, 670):
            if key[i, j] < 100:
                hit("Up")
                return

    return


if __name__ == "__main__":
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        is_collide(data)

    # for i in range(300, 620):
    #     for j in range(530, 565):
    #         data[i, j] = 0
    # for i in range(300, 620):
    #     for j in range(640, 670):
    #         data[i, j] = 100
    # #
    # image.show()



