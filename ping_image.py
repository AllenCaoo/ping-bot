import random
import cv2

qping = cv2.imread('images/ping.png')


def draw_pings(img_path):
    img = cv2.imread(img_path)
    min_x_size = min(int(img.shape[1] / 3), int(qping.shape[1]))
    min_y_size = min(int(img.shape[0] / 3), int(qping.shape[0]))
    ping = cv2.resize(qping, (min_x_size, min_y_size))
    x_range = (0, img.shape[1] - ping.shape[1])
    y_range = (0, img.shape[0] - ping.shape[0])
    for _ in range(10):
        x = random.randint(0, x_range[1] - 1)
        y = random.randint(0, y_range[1] - 1)
        img[y: y + ping.shape[0], x: x + ping.shape[1]] = \
            cv2.bitwise_or(img[y: y + ping.shape[0], x: x + ping.shape[1]], ping)
    cv2.imwrite('images/recent_out.jpg', img)