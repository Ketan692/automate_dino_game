import pyautogui, time
from PIL import ImageGrab


def hit(key):
    pyautogui.keyDown(key)


def screenshot():
    image = ImageGrab.grab().convert("L")
    return image


def is_collide(data):
    for i in range(300, 620):
        for j in range(640, 670):
            if data[i, j] < 100:
                hit("Up")
                return True

    for i in range(300, 400):
        for j in range(550, 630):
            if data[i, j] < 0:
                hit("down")
                return True
    return False


if __name__ == "__main__":
    time.sleep(3)
    while True:
        image = screenshot()
        data = image.load()
        is_collide(data)
