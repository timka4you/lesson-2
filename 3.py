import cv2
# Завантаження зображення
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Пошук контурів
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Ітерація по контурам
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    # Якщо контур має 4 точки, то це може бути квадрат
    if len(approx) == 4:
        cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)  # Виділення квадрата зеленим
    # Якщо контур має більше 6 точок, то це може бути коло
    elif len(approx) > 6:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(image, center, radius, (0, 255, 0), 2)  # Виділення кола зеленим

# Показ зображення з виділеними патернами
cv2.imshow('Patterns', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
