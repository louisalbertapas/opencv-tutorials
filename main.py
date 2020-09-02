import cv2
import numpy as np
import datetime


def wait_for_key():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def read_image():
    img = cv2.imread('lena.jpg', 0)  # 1 -> color, 0 -> grayscale, -1 -> unchanged

    # display image
    cv2.imshow('Tutorial 1', img)

    # wait for key
    wait_for_key()


def write_image():
    img = cv2.imread('lena.jpg', 0)  # 1 -> color, 0 -> grayscale, -1 -> unchanged
    cv2.imwrite('lena_copy.png', img)


def capture_video():
    cap = cv2.VideoCapture(0)  # 0 default camera, if not working, use -1
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # ("X", "V", "I", "D")
    out = cv2.VideoWriter('myoutput.avi', fourcc, 20.0, (640, 480))  # filename, fourcc, 20 fps, size of video

    # prints the frame widht and height
    # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # set properties
    # camera will only set up to its maximum resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while cap.isOpened():  # run indefinitely
        ret, frame = cap.read()  # if frame is available, ret will be true, otherwise false

        if ret:

            # save video
            out.write(frame)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('My camera', gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


# drawing geometric shapes
def draw_shapes():
    img = cv2.imread('lena.jpg', 1)  # get image using opencv2
    # img = np.zeros([512, 512, 3], np.uint8)  # black image

    # draw line
    # src image, pt1, pt2, color in BGR format, thickness
    img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

    # arrowed line
    img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

    # draw rectangle
    # pt 1 = top left
    # pt 2 = bottom right
    img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5)  # -1 is fill

    # draw circle
    img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)  # -1 thick is fill

    # add text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

    cv2.imshow('Draw shapes', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_date_time():
    cap = cv2.VideoCapture(0)  # 0 default camera, if not working, use -1

    # prints the frame widht and height
    # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # set properties
    # camera will only set up to its maximum resolution
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while cap.isOpened():  # run indefinitely
        ret, frame = cap.read()  # if frame is available, ret will be true, otherwise false

        if ret:
            # add text to video
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' '\
                   + 'Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            datet = str(datetime.datetime.now())
            frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('My camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


# handle mouse events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        img2 = np.zeros((512, 512, 3), np.uint8)
        # fill img2 with the color we clicked
        img2[:] = [blue, green, red]  # fills all channel BGR
        cv2.imshow('image', img)
        cv2.imshow('color image', img2)
        # make a line
        '''
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # fill circle
        points.append((x, y))  # save it to array
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)  # [-1] index is last element, [-2] second last
        cv2.imshow('image', img)
        '''


'''
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ', ' + str(y)
        cv2.putText(img, text, (x, y), font, .5, (255, 255, 255), 2)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, text, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
'''


# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('lena.jpg', 1)
points = []


def handle_mouse_event():
    # events = [i for i in dir(cv2) if 'EVENT' in i]  # gets all event in cv2 dir
    # print(events)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def arithmetic_methods():
    img = cv2.imread('messi5.jpg')
    img2 = cv2.imread('opencv-logo.png')

    print(img.shape)  # returns a tuple with # of rows, columns, and channel
    print(img.size)  # returns total number of pixels
    print(img.dtype)  # returns image datatype
    b, g, r = cv2.split(img)  # split the image into channels
    img = cv2.merge((b, g, r))  # merge the channels to an image

    #  ROI = region of interest
    #  gets all the pixel of the ball
    ball = img[280:340, 330:390]  # upper left of the ball, lower right of the ball
    # print (ball)
    img[280:340, 100:160] = ball  # place the ball to other place

    # add an image to an image
    # to add images, arrays should have same size, so resize first
    # resizing
    img = cv2.resize(img, (512, 512))  # resize to 512x512
    img2 = cv2.resize(img2, (512, 512))
    dst = cv2.add(img, img2)

    # add weighted
    dst = cv2.addWeighted(img, .6, img2, .4, 0)

    cv2.imshow('image', img)
    cv2.imshow('image2', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def bitwise_operations():
    # mask is a binary pixel
    img1 = np.zeros((250, 500, 3), np.uint8)
    img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
    img2 = cv2.imread('image_1.png')

    # bitwise and
    # only 1 and 1, it will yield to true
    bitAnd = cv2.bitwise_and(img2, img1)
    bitOr = cv2.bitwise_or(img2, img1)
    bitXor = cv2.bitwise_xor(img2, img1)
    bitNot1 = cv2.bitwise_not(img1)
    bitNot2 = cv2.bitwise_not(img2)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('bitAnd', bitAnd)
    cv2.imshow('bitOr', bitOr)
    cv2.imshow('bitXor', bitXor)
    cv2.imshow('bitNot1', bitNot1)
    cv2.imshow('bitNot2', bitNot2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# x = current position of trackbar
def nothing(x):
    print(x)


def trackbar():
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('image')
    cv2.createTrackbar('B', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('R', 'image', 0, 255, nothing)

    switch = '0 : OFF\n 1 : ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while True:
        b = cv2.getTrackbarPos('B', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        r = cv2.getTrackbarPos('R', 'image')
        s = cv2.getTrackbarPos(switch, 'image')
        if s == 0:
            img[:] = 0  # don't do anything
        else:
            img[:] = [b, g, r]
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # esc key
            break

    cv2.destroyAllWindows()


def gray_color():
    cv2.namedWindow('image')
    cv2.createTrackbar('CP', 'image', 10, 400, nothing)

    switch = 'color/gray'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while True:
        img = cv2.imread('lena.jpg')
        pos = cv2.getTrackbarPos('CP', 'image')
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 10)
        s = cv2.getTrackbarPos(switch, 'image')
        if s == 0:
            pass
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # esc key
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("OpenCV")
    gray_color()
