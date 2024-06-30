# -*- coding: utf-8 -*-
# @Time: 3/18 7:06
# @DESC:
import base64
image_path = r"F:\data_edgeai-app\train\番茄\image.1.jpg"
with open(image_path,'rb')as f:
    base64_data = base64.b64encode(f.read())
    print(str(base64_data))