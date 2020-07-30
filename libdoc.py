import os
from robot.libdoc import libdoc

time_to_wait = 10
time_counter = 0

directory = "keywords"
directory_path = "./" + directory + "/"
html = "keywords.html"
xml = "keywords.xml"

if not os.path.exists(directory):
    os.mkdir(directory)

libdoc("./src/FlaUILibrary", directory_path  + html)
libdoc("./src/FlaUILibrary", directory_path  + xml)
