import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Define font parameters
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (255, 255, 255)
thickness = 1

# Add text for each planet
cv2.putText(img, "Mercury", (50, 70), font, font_scale, font_color, thickness)
cv2.putText(img, "Venus", (220, 60), font, font_scale, font_color, thickness)
cv2.putText(img, "Earth", (370, 75), font, font_scale, font_color, thickness)
cv2.putText(img, "Mars", (540, 70), font, font_scale, font_color, thickness)
cv2.putText(img, "Jupiter", (720, 60), font, font_scale, font_color, thickness)
cv2.putText(img, "Saturn", (890, 70), font, font_scale, font_color, thickness)
cv2.putText(img, "Uranus", (1080, 75), font, font_scale, font_color, thickness)
cv2.putText(img, "Neptune", (1230, 60), font, font_scale, font_color, thickness)

# Display the image
cv2.imshow("Solar System with Names", img)
cv2.waitKey(0)

# Save the image with names
cv2.imwrite("Solar_system_with_name.jpg", img)

# Close all windows
cv2.destroyAllWindows()
