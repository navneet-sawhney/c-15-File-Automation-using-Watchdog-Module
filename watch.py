"""Imports the sys module, which provides access to some variables used or 
maintained by the interpreter and functions that interact with the interpreter."""
import sys

"""Imports the time module, which provides various time-related functions."""
import time

# Imports the random module, which provides functions for generating random numbers.
import random

# Imports the os module, which provides a way to use operating system-dependent functionality.
import os

# Imports the shutil module, which offers a higher level of file operations.
import shutil

# Imports the Observer class from the watchdog.observers module. watchdog is a Python library for monitoring file system events.
from watchdog.observers import Observer

# Imports the FileSystemEventHandler class from the watchdog.events module. This class is a base class for file system event handlers.
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/navne/Downloads"            # Add the path of you "Downloads" folder.
to_dir = "C:/Users/navne/OneDrive/Desktop/BB Data Science/Destination" #Create "Document_Files" folder in your Desktop and update the path accordingly.

# A dictionary that defines the directory structure for different file types. Each key represents a directory name, and the corresponding value is a list of file extensions associated with that directory.
dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Handler Class
# Defines a custom class FileMovementHandler that inherits from FileSystemEventHandler. This class will handle the file system events, such as file creation.
class FileMovementHandler(FileSystemEventHandler):
# Overrides the on_created method of the base class. This method is called when a file or directory is created.
    def on_created(self, event):
        #Extracts the file name and extension from the source path of the created file.
        name, extension = os.path.splitext(event.src_path)
       
        # Pauses the execution for 1 second.
        time.sleep(1)

        # Iterates over the items of the dir_tree dictionary.
        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()