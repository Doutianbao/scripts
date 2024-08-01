import subprocess
import sys
import importlib

# 检查并安装依赖包
def install(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# 依赖包列表
packages = ['pandas', 'openpyxl', 'tkinter']

# 安装依赖包
for package in packages:
    install(package)

# 继续导入依赖包
import pandas as pd
import io
import tkinter as tk
from tkinter import filedialog

def markdown_to_excel():
    # 获取输入框中的Markdown表格内容
    markdown_table = input_text.get("1.0", tk.END)
    
    # 使用pandas读取Markdown表格
    df = pd.read_csv(io.StringIO(markdown_table), sep='|', skipinitialspace=True)
    
    # 清理列名和数据
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # 删除可能出现的空列（由于Markdown表格格式导致）
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    # 打开文件对话框，选择保存位置
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    
    if file_path:
        # 将DataFrame保存为Excel文件
        df.to_excel(file_path, index=False, engine='openpyxl')
        result_label.config(text="转换成功！文件已保存。")
    else:
        result_label.config(text="转换取消。")

# 创建主窗口
root = tk.Tk()
root.title("Markdown表格转Excel")

# 创建文本输入框和标签
input_label = tk.Label(root, text="请输入Markdown表格：")
input_label.pack()

input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# 创建转换按钮
convert_button = tk.Button(root, text="转换为Excel", command=markdown_to_excel)
convert_button.pack()

# 创建结果标签
result_label = tk.Label(root, text="")
result_label.pack()

# 运行主循环
root.mainloop()
