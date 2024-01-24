import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

cap = cv.VideoCapture(r"C:\Users\dimri\Downloads\WhatsApp Video 2024-01-24 at 15.31.43_e2e6edc6.mp4")

def rescaling_fn(frame, scale=0.75): 
    width = int(frame.shape[1] * scale)  # 1 for rows
    height = int(frame.shape[0] * scale)  # 2 for columns
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

previous_center = []  # announce a list to store centers of all detected objects

fig, ax = plt.subplots()  # to plot trajectory on the graph 

while True: 
    isTrue, frame = cap.read() 
    if not isTrue: 
        break

    rescaled_dim_frame = rescaling_fn(frame, scale=1)

    # OpenCV by default has BGR color space, convert to HSV for better ball detection
    hsv = cv.cvtColor(rescaled_dim_frame, cv.COLOR_BGR2HSV)

    # Define the color range for the basketball (adjust these values accordingly)
    orange_lower = np.array([5, 100, 100])
    orange_upper = np.array([15, 255, 255])

    mask = cv.inRange(hsv, orange_lower, orange_upper)  # binary masking

    # Contours in MASK
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw boxes around the basketball
    for contour in contours: 
        if cv.contourArea(contour) > 1000:  # Adjust the area threshold
            x, y, w, h = cv.boundingRect(contour)
            center = (int(x + w/2), int(y + h/2))
            cv.rectangle(rescaled_dim_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            previous_center.append(center)

            # Draw the red trajectory line from all stored centers 
            if len(previous_center) > 1:
                cv.polylines(rescaled_dim_frame, [np.array(previous_center)], False, (0, 0, 255), 2)

    # For plotting the trajectory
    if len(previous_center) > 1: 
        x, y = zip(*previous_center)
        ax.plot(x, y, 'ro-')

    cv.imshow('newvid', rescaled_dim_frame)

    if cv.waitKey(30) & 0xFF == ord('q'):
        break

plt.show()  # shows the trajectory plot after the video ends
cap.release() 
cv.destroyAllWindows() 



# import cv2 as cv 
# import numpy as np 
# import matplotlib.pyplot as plt 

# cap = cv.VideoCapture(r"C:\Users\dimri\Downloads\WhatsApp Video 2024-01-24 at 15.31.43_e2e6edc6.mp4")

# def rescaling_fn(frame, scale=0.75): 
#     width = int(frame.shape[1] * scale)  # 1 for rows
#     height = int(frame.shape[0] * scale)  # 2 for columns
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# previous_centers = []  # a list to store centers of all detected objects

# fig, ax = plt.subplots()  # to plot trajectory on the graph 

# while True: 
#     isTrue, frame = cap.read() 
#     if not isTrue: 
#         break

#     rescaled_dim_frame = rescaling_fn(frame, scale=0.5)

#     # OpenCV by default has BGR color space, convert to HSV for better ball detection
#     hsv = cv.cvtColor(rescaled_dim_frame, cv.COLOR_BGR2HSV)

#     # Define the color range for the basketball (adjust these values accordingly)
#     orange_lower = np.array([5, 100, 100])
#     orange_upper = np.array([15, 255, 255])

#     mask = cv.inRange(hsv, orange_lower, orange_upper)  # binary masking

#     # Contours in MASK
#     contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#     # Draw boxes around the basketball
#     for contour in contours: 
#         if cv.contourArea(contour) > 1000:  # Adjust the area threshold
#             x, y, w, h = cv.boundingRect(contour)
#             center = (int(x + w/2), int(y + h/2))
#             cv.rectangle(rescaled_dim_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             previous_centers.append(center)

#             # Draw the fading red trail
#             for i in range(len(previous_centers)):
#                 alpha = int(255 * (1 - i/len(previous_centers)))  # Decrease alpha for fading effect
#                 cv.circle(rescaled_dim_frame, previous_centers[i], 5, (0, 0, 255, alpha), -1)

#     # For plotting the trajectory
#     if len(previous_centers) > 1: 
#         x, y = zip(*previous_centers)
#         ax.plot(x, y, 'ro-')

#     cv.imshow('newvid', rescaled_dim_frame)

#     if cv.waitKey(30) & 0xFF == ord('q'):
#         break

# plt.show()  # shows the trajectory plot after the video ends
# cap.release() 
# cv.destroyAllWindows() 


# import cv2 as cv 
# import numpy as np 
# import matplotlib.pyplot as plt 

# cap = cv.VideoCapture(r"C:\Users\dimri\Downloads\WhatsApp Video 2024-01-24 at 15.31.43_e2e6edc6.mp4")

# def rescaling_fn(frame, scale=0.75): 
#     width = int(frame.shape[1] * scale)  # 1 for rows
#     height = int(frame.shape[0] * scale)  # 2 for columns
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# max_centers_length = 50  # Maximum number of points to store in the trajectory
# previous_centers = []    # A list to store centers of all detected objects

# fig, ax = plt.subplots()  # To plot the trajectory on the graph 

# while True: 
#     isTrue, frame = cap.read() 
#     if not isTrue: 
#         break

#     rescaled_dim_frame = rescaling_fn(frame, scale=0.5)

#     # OpenCV by default has BGR color space, convert to HSV for better ball detection
#     hsv = cv.cvtColor(rescaled_dim_frame, cv.COLOR_BGR2HSV)

#     # Define the color range for the basketball (adjust these values accordingly)
#     orange_lower = np.array([5, 100, 100])
#     orange_upper = np.array([15, 255, 255])

#     mask = cv.inRange(hsv, orange_lower, orange_upper)  # Binary masking

#     # Contours in MASK
#     contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#     # Draw boxes around the basketball
#     for contour in contours: 
#         if cv.contourArea(contour) > 1000:  # Adjust the area threshold
#             x, y, w, h = cv.boundingRect(contour)
#             center = (int(x + w/2), int(y + h/2))
#             cv.rectangle(rescaled_dim_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             previous_centers.append(center)

#             # Limit the number of points in the trajectory to create a tail effect
#             if len(previous_centers) > max_centers_length:
#                 previous_centers = previous_centers[-max_centers_length:]

#             # Draw the fading red trail
#             for i in range(len(previous_centers)):
#                 alpha = int(255 * (1 - i / len(previous_centers)))  # Decrease alpha for fading effect
#                 cv.circle(rescaled_dim_frame, previous_centers[i], 5, (0, 0, 255, alpha), -1)

#     # For plotting the trajectory as a line
#     if len(previous_centers) > 1: 
#         x, y = zip(*previous_centers)
#         ax.plot(x, y, 'r-')

#     cv.imshow('newvid', rescaled_dim_frame)

#     if cv.waitKey(30) & 0xFF == ord('q'):
#         break

# plt.show()  # Shows the trajectory plot after the video ends
# cap.release() 
# cv.destroyAllWindows()
