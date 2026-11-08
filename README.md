# Image Info Exporter
## 项目简介
批量遍历文件夹内图片，读取图片宽高尺寸，按像素大小排序，导出信息到CSV表格。
## 功能
- 自动遍历图片文件夹，支持jpg/png/bmp
- 获取图片宽度、高度、总像素
- 按图片像素从大到小自动排序
- 导出csv，Excel直接打开查看
## 依赖
- Python3
- Pillow
## 安装依赖
```bash
pip install pillow