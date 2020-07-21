import os
#import pdfkit
import time
from robot.libdoc import libdoc

time_to_wait = 10
time_counter = 0

directory = "keywords"
directory_path = "./" + directory + "/"
html = "keywords.html"
pdf = "keywords.pdf"

if not os.path.exists(directory):
    os.mkdir(directory)

libdoc("./src/FlaUILibrary", directory_path  + html)
#while not os.path.exists(directory_path  + html):
#    time.sleep(1)
#    time_counter += 1
#    if time_counter > time_to_wait:break

# Optional feature to create automatic pdf file from generated html
# https://wkhtmltopdf.org
# pdfkit.from_file(directory_path + html, directory_path + pdf)
