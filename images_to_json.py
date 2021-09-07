import os
import json
import imageio

image_list = os.listdir("images")

output_list = []
for file_name in image_list:
    im = imageio.imread(f"images/{file_name}").reshape(-1) / 255
    imlist = im.tolist()
    clazz = 1 if file_name.startswith("one") else - 1
    output_list.append({'file': file_name, 'data': imlist, 'class': clazz})

print(f"var image_data = {json.dumps(output_list)};")
