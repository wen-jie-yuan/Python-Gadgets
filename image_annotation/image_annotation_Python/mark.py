# -*-coding:utf-8-*-
"""
Name : tt.py
Author  : ywj
Contect : 1185500656@qq.com
Time    : 2021/7/15 22:24
Desc: pillow=8.0.1  、  opencv=4.5.0
"""
import cv2
from PIL import Image

path_input = 'woman_GT.bmp'
path_output = 'output.png'
img = Image.open(path_input)  # image_path
img_w = img.size[0]  # 原图的长
img_h = img.size[1]  # 原图的高

x = 70  # 标注的起始横坐标
y = 80  # 标注的起始纵坐标
w = 50  # 标注的框的长度大小
h = 50  # 标注的框的高度大小
enlarge_factor = 2  # 放大倍数
x1 = x + w  # 标注区域终点横坐标
y1 = y + h  # 标注区域终点纵坐标
# 选中区域（minx，miny，maxx，maxy）
box = (x, y, x1, y1)
# 选中区域裁剪
img_area = img.crop(box)
# 裁剪区域放大
img_area = img_area.resize((w * enlarge_factor, h * enlarge_factor), Image.ANTIALIAS)
# 粘贴，第二个参数指定粘贴位置（根据需要调节）
img.paste(img_area, (img_w - w * enlarge_factor-1, img_h - h * enlarge_factor-1))
# 保存图片
img.save(path_output)
img = cv2.imread(path_output)
# 绘制边框，第二第三个参数元祖表示指定框选区域，第四个参数指定线条颜色，第五个参数指定线条宽度
cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
cv2.rectangle(img, (img_w - w * enlarge_factor-1, img_h - h * enlarge_factor-1), (img_w-2, img_h-2), (0, 0, 255), 2)
cv2.imshow("Image", img)
cv2.imwrite(path_output, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

