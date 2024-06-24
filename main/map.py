from tkinter import *
import tkintermapview
import cv2 
from PIL import Image, ImageTk 


root = Tk()
root.title("Map")
root.geometry("1280x720")
vid = cv2.VideoCapture(0)

# Create a frame for the map
map_frame = Frame(root)
map_frame.grid(row=0, column=0, sticky="nsew")

my_label = LabelFrame(map_frame, text="Map")
my_label.pack(fill="both", expand=True)

map_widget = tkintermapview.TkinterMapView(my_label, width=600, height=720)
map_widget.set_position(21.003541,105.8423387)
marker_1 = map_widget.set_marker(21.0035212,105.8423548, "Marker 1")
map_widget.set_zoom(20)
map_widget.pack(fill="both", expand=True)

# Create a frame for the camera
camera_frame = Frame(root)
camera_frame.grid(row=0, column=1, sticky="nsew")

camera_label = Label(camera_frame, text="Camera will be displayed here")
camera_label.pack(fill="both", expand=True)
def update_image():
    # Capture a frame from the webcam
    ret, frame = vid.read()

    # Convert the frame to a format that can be displayed in tkinter
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    photo_image = ImageTk.PhotoImage(image)

    # Display the frame in the label
    camera_label.config(image=photo_image)
    camera_label.image = photo_image

    # Schedule the next update
    root.after(10, update_image)

# Start the webcam updates
update_image()
root.mainloop()