#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class BallDetector:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.image_callback)
        self.image_pub = rospy.Publisher("processed_image", Image, queue_size=1)
        self.padding = 100
        self.silo_threshold = 10
        self.radius_threshold = 4 
        self.min_circle_count_for_silo = 10 


    def cluster_circles(self, circles, min_dist):
        clusters = []
        cluster_sizes = [] 
        for i in range(len(circles)):
            cluster_found = False
            for j, cluster in enumerate(clusters):
                if np.min(np.linalg.norm(circles[i] - cluster, axis=1)) < min_dist:
                    cluster.append(circles[i])
                    cluster_sizes[j] += 1
                    cluster_found = True
                    break
            if not cluster_found:
                clusters.append([circles[i]])
                cluster_sizes.append(1)
        return clusters, cluster_sizes








        

    # def cluster_circles(self, circles, min_dist):
    #     clusters = []
    #     for i in range(len(circles)):
    #         cluster_found = False
    #         for cluster in clusters:
    #             if np.min(np.linalg.norm(circles[i] - cluster, axis=1)) < min_dist:
    #                 cluster.append(circles[i])
    #                 cluster_found = True
    #                 break
    #         if not cluster_found:
    #             clusters.append([circles[i]])
    #     return clusters

    def is_silo(self, cluster):
        y_coords = [circle[1] for circle in cluster]
        radii = [circle[2] for circle in cluster]
        y_std = np.std(y_coords)
        radius_std = np.std(radii)
        num_circles = len(cluster)
        return y_std < self.silo_threshold and radius_std < self.radius_threshold and num_circles >= self.min_circle_count_for_silo

        # return y_std < self.silo_threshold and radius_std < self.radius_threshold

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)
            return



        # try:
        #     cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        # except CvBridgeError as e:
        #     print(e)
        #     return

        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist=10,
                                   param1=35, param2=20, minRadius=7, maxRadius=50)
        




    #        if circles is not None:
    #    circles = np.uint16(np.around(circles))
    #    clusters = self.cluster_circles(circles[0, :], 10)
    # # Check if any cluster qualifies as a silo
    #    silo_detected = False
    #    for cluster in clusters:
    #         if self.is_silo(cluster):
    #            silo_detected = True
    #            min_x = min(i[0] for i in cluster) - self.padding
    #            min_y = min(i[1] for i in cluster) - self.padding
    #            max_x = max(i[0] for i in cluster) + self.padding
    #            max_y = max(i[1] for i in cluster) + self.padding
    #            cv2.rectangle(cv_image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
    #            cv2.putText(cv_image, "Silo", (min_x, min_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    #         
    #            break
    # 
    #     if not silo_detected:
    #         for cluster in clusters:
    #             for circle in cluster:
    #                cv2.circle(cv_image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
    #                cv2.circle(cv_image, (circle[0], circle[1]), 2, (0, 0, 255), 3)
    #                cv2.putText(cv_image, "Ball", (circle[0], circle[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        if circles is not None:
            circles = np.uint16(np.around(circles))
            #clusters = self.cluster_circles(circles[0, :], 10)
            clusters, cluster_sizes = self.cluster_circles(circles[0, :], 10)
            density_threshold = 0.5 
            # silo_detected = False
            for cluster, size in zip(clusters, cluster_sizes):
                if size >= self.min_circle_count_for_silo and self.is_silo(cluster):
                    # Draw bounding box for silo
                    min_x = min(i[0] for i in cluster) - self.padding
                    min_y = min(i[1] for i in cluster) - self.padding
                    max_x = max(i[0] for i in cluster) + self.padding
                    max_y = max(i[1] for i in cluster) + self.padding
                                # Calculate the area of the bounding box
                    area = (max_x - min_x) * (max_y - min_y)
            # Calculate the density of circles in the cluster
                    density = size / area
                    if density >density_threshold: 
                        cv2.rectangle(cv_image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
                        cv2.putText(cv_image, "Silo", (min_x, min_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        break




            
            # for cluster in clusters:
            #     if self.is_silo(cluster):
            #         # silo_detected = True
            #         min_x = min(i[0] for i in cluster) - self.padding
            #         min_y = min(i[1] for i in cluster) - self.padding
            #         max_x = max(i[0] for i in cluster) + self.padding
            #         max_y = max(i[1] for i in cluster) + self.padding
            #         cv2.rectangle(cv_image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
            #         cv2.putText(cv_image, "Silo", (min_x, min_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    

            # if not silo_detected : 
            #         for circle in circles[0, : ]:
            #             center = (circle[0],circle[1])
            #             radius = circle[2]

            #         # for cluster in clusters : 
            #         #     for circle in cluster: 
            #             cv2.circle(cv_image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            #             cv2.circle(cv_image, (circle[0], circle[1]), 2, (0, 0, 255), 3)
            #             cv2.putText(cv_image, "Ball", (circle[0], circle[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


                else:
                    for circle in cluster:
                        cv2.circle(cv_image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
                        cv2.circle(cv_image, (circle[0], circle[1]), 2, (0, 0, 255), 3)
                        cv2.putText(cv_image, "Ball", (circle[0], circle[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        except CvBridgeError as e:
            rospy.logerr(e)

if __name__ == '__main__':
    rospy.init_node('ball_detector', anonymous=True)
    detector = BallDetector()
    rospy.spin()








