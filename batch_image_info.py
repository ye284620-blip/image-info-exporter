import os
import csv
from PIL import Image

# 配置路径
IMAGE_FOLDER = "./images"
OUTPUT_CSV = "./image_report.csv"

image_data = []

# 遍历文件夹
for file_name in os.listdir(IMAGE_FOLDER):
    # 筛选图片后缀
    ext = file_name.lower()
    if ext.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        full_path = os.path.join(IMAGE_FOLDER, file_name)
        try:
            img = Image.open(full_path)
            w, h = img.size
            total_pixel = w * h
            image_data.append({
                "文件名": file_name,
                "宽度": w,
                "高度": h,
                "总像素": total_pixel
            })
        except Exception as err:
            print(f"读取失败：{file_name}，错误：{err}")

# 按总像素从大到小排序
image_data.sort(key=lambda item: item["总像素"], reverse=True)

# 写入csv，utf-8-sig保证Excel打开不乱码
with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
    headers = ["文件名", "宽度", "高度", "总像素"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(image_data)

print(f"✅ 完成！一共处理 {len(image_data)} 张图片")
print(f"结果文件：{OUTPUT_CSV}")