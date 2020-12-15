from python_imagesearch.imagesearch import imagesearch
import pyautogui
import cv2
import numpy as np


def get_total():
    point = pyautogui.locateCenterOnScreen(f".\\images\\calculador\\found_result.png", confidence=0.7)
    y = point.y + 43
    x = point.x - 277
    return [x, y, 292, 30]


clear = pyautogui.locateCenterOnScreen(f".\\images\\calculador\\C.png")
pyautogui.click(clear.x, clear.y)

conta = input()
for char in list(conta):
    if not char or char == ' ':
        continue
    box = pyautogui.locateCenterOnScreen(f".\\images\\calculador\\{char}.png")
    pyautogui.click(box.x, box.y)

equal = pyautogui.locateCenterOnScreen(f".\\images\\calculador\\=.png", confidence=0.7)
pyautogui.click(equal.x, equal.y)


image = pyautogui.screenshot(region=get_total())
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

cv2.imshow("Screenshot", image)
cv2.waitKey(0)
