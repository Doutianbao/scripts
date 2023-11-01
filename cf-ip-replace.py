import re
import os

def replace_ips(filename, ip_list):
    # 读取源文本文件
    with open(filename, 'r') as file :
        original_text = file.read()

    all_replaced_texts = []  # 用于存储所有替换后的文本

    for i, ip in enumerate(ip_list):
        # 使用正则表达式替换
        replaced_text = re.sub(r'(?<=@).+?(?=:)', ip, original_text)
        all_replaced_texts.append(replaced_text)

        # 写入到新的文本文件中
        with open(f'replaced_{i}.txt', 'w') as file:
            file.write(replaced_text)
    
    # 合并所有替换后的文本，并写入到一个新的文件中
    with open('all_replaced.txt', 'w') as file:
        file.write(os.linesep.join(all_replaced_texts))

def main():
    filename = 'original_links.txt'
    ip_input = input("Enter new IPs, separated by commas: ")
    ip_list = [ip.strip() for ip in ip_input.split(',')]
    
    replace_ips(filename, ip_list)

if __name__ == "__main__":
    main()
