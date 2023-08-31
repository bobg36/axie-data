from flask import Flask, render_template
import os
import sys

folder_path = 'flask\\static'  # New path to the folder
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    folder_paths_list = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            contents = os.listdir(item_path)
            content_paths = [os.path.join(item, content) for content in contents]
            new_content_paths = []
            for thing in content_paths:
                thing = thing.replace('\\', '/')
                new_content_paths.append(thing)
            folder_paths_list.append(new_content_paths)

i = 0
image_list = []
while i<(len(folder_paths_list)):
    curr_img = folder_paths_list[i][0]
    image_list.append(curr_img)
    i = i + 1

for folder_images in folder_paths_list:
    folder_images.pop(0)



# sys.exit()

app = Flask(__name__)
@app.route('/')
@app.route('/<int:folder_index>')
def index(folder_index=0):
    
    if folder_index < len(folder_paths_list):
        image_filenames = folder_paths_list[folder_index]
    else:
        image_filenames = []  # Handle invalid folder_index

    return render_template('images.html', image_filenames=image_filenames, folder_paths_list=folder_paths_list, image_list=image_list)
    

if __name__ == '__main__':
    app.run(debug=True)
