import numpy as np
from PIL import Image
from Line import Line
from Point import Point
from Figure import Figure
import matplotlib.pyplot as plt

# Образцы изображений
PLUS = 'img/plus.png'
LITTLE_PLUS = 'img/9pixplus.png'
MINUS = 'img/minus.png'
DIVIDE = ''
MULTIPLY = ''

# Изображения для сопоставления
BLACK = 'img/black.png'
WHITE = 'img/white.png'
RED_PLUS = 'img/9pix_redplus.png'
NIKE = 'img/nike.png'


def get_pixels(image):
    """Все пиксели изображения"""
    img = Image.open(image)
    pixels = np.array(img)
    return pixels


def get_image_size(image):
    """Размеры изображения"""
    img = Image.open(image)
    width, height = img.size
    return width, height


def img_from_pixels(pixels):
    """Создание изображения по массиву пикселей"""
    array = np.array(pixels, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save('img/new.png')


def grey_calc(pixels):
    """Вычисление оттенка серого"""
    grey_image = []
    for row in pixels:
        new_row = []
        for pix in row:
            greyR, greyG, greyB = (0.3 * pix[0] + 0.59 * pix[1] + 0.11 * pix[2]), \
                                  (0.3 * pix[0] + 0.59 * pix[1] + 0.11 * pix[2]),\
                                  (0.3 * pix[0] + 0.59 * pix[1] + 0.11 * pix[2])
            new_row.append([greyR, greyG, greyB])
        grey_image.append(new_row)
    return grey_image


black_rule = Figure(Line(Point(0.0, 1.0), Point(70.0, 1.0)), Line(Point(70.0, 1.0), Point(200.0, 0.0)))
black_rignt_border = 200  # Крайняя правая граница графика правила для черного цвета
white_rule = Figure(Line(Point(180.0, 0.0), Point(230.0, 1.0)), Line(Point(230.0, 1.0), Point(255.0, 1.0)))
white_rignt_border = 256  # Крайняя правая граница графика правила для белого цвета
white_left_border = 180   # Крайняя левая граница графика правила для белого цвета
figures = [black_rule, white_rule]

# Построение графиков правил для черного и белого цветов
fig, ax = plt.subplots()
all_points = []
for f in figures:
    x = []
    y = []
    for line in f.get_lines():
        for point in line.get_points():
            all_points.append(point)
            x.append(point.get_x())
            y.append(point.get_y())
    ax.plot(x, y)
# plt.show()

# Менять картинки в следующих 4 строчках
ideal = get_pixels(PLUS)  # образец
sample = get_pixels(MINUS)  # картинка для сопоставления
ideal_size = get_image_size(PLUS)  # размер образца
sample_size = get_image_size(MINUS)  # размер картинки для сопоставления
resolution = ideal_size[0] * ideal_size[1]  # разрешение образца
print(resolution)
grey_ideal = grey_calc(ideal)  # вычисление оттенков серого для пикселей образца(приводит к серому)
grey_sample = grey_calc(sample)  # вычисление оттенков серого для пикселей картинки для сопоставления(приводит к серому)

grey_sample_appraisal_black = []  # оценка черности всех черных пикселей картинки для сопоставления
grey_sample_appraisal_white = []  # оценка белости всех белых пикселей картинки для сопоставления
for row in grey_sample:
    for pix in row:
        if pix[0] <= black_rignt_border:
            for line in black_rule.get_lines():
                if line.start.get_x() <= pix[0] <= line.end.get_x():
                    grey_sample_appraisal_black.append(line.get_value(pix[0]))
        else:
            grey_sample_appraisal_black.append(0)

for row in grey_sample:
    for pix in row:
        if (pix[0] >= white_left_border) and (pix[0] <= white_rignt_border):
            for line in white_rule.get_lines():
                if line.start.get_x() <= pix[0] <= line.end.get_x():
                    grey_sample_appraisal_white.append(line.get_value(pix[0]))
        else:
            grey_sample_appraisal_white.append(0)

grey_ideal_appraisal_black = []  # оценка черности всех черных пикселей образца
grey_ideal_appraisal_white = []  # оценка белости всех белых пикселей образца
for row in grey_ideal:
    for pix in row:
        if pix[0] <= black_rignt_border:
            for line in black_rule.get_lines():
                if line.start.get_x() <= pix[0] <= line.end.get_x():
                    grey_ideal_appraisal_black.append(line.get_value(pix[0]))
        else:
            grey_ideal_appraisal_black.append(0)

for row in grey_ideal:
    for pix in row:
        if (pix[0] >= white_left_border) and (pix[0] <= white_rignt_border):
            for line in white_rule.get_lines():
                if line.start.get_x() <= pix[0] <= line.end.get_x():
                    grey_ideal_appraisal_white.append(line.get_value(pix[0]))
        else:
            grey_ideal_appraisal_white.append(0)


result = 0  # оценка схожести образца с картинкой для сопоставления
for i in range(len(grey_sample_appraisal_white)):
    result += grey_ideal_appraisal_black[i] * grey_sample_appraisal_black[i] + \
              grey_ideal_appraisal_white[i] * grey_sample_appraisal_white[i]

print(result/resolution)  # ответ
