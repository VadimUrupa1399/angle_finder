import cv2
import math

path = 'test.jpg'
img = cv2.imread(path)
points_list = []


def mouse_points(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(points_list)
        if size != 0 and size % 3 !=0:
            cv2.line(img, tuple(points_list[round((size-1)/3)*3]), (x, y), (0, 0, 255), 3)

        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        points_list.append([x, y])
        print(points_list)
        #print(x, y)



def gredient(p1, p2):
    # get the gredient of lines.
    return (p2[1] - p1[1]) / (p2[0] - p1[0])



def get_angle(points_list):
    p1, p2, p3 = points_list[-3:]
    m1 = gredient(p1, p2)
    m2 = gredient(p1, p3)
    angle_r = math.atan((m2 - m1) / (1 + (m2*m1)))
    angle_d = round(math.degrees(angle_r))

    cv2.putText(img, str(angle_d), (p1[0] - 40, p1[1] - 20), cv2.FONT_HERSHEY_COMPLEX,
                1.5, (0, 0, 255), 3)

while True:

    if len(points_list) % 3 == 0 and len(points_list) != 0:
        get_angle(points_list)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mouse_points)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        points_list = []
        img = cv2.imread(path)
    #break
    #cv2.destroyAllWindows()x``