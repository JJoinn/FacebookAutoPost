import re

# 新建一个空列表用于存储匹配到的字符串
matches_list = []

# 打开文件
with open("D:/Project/FacebookAutoPost/Facebook.html", "r", encoding="utf-8") as file:
    # 逐行读取文件内容
    for line in file:
        # 使用正则表达式查找符合条件的字符串，并捕获需要的部分
        matches = re.finditer(r'href="https://www\.facebook\.com/groups/([^"]+)/"', line)
        # 将匹配到的字符串的捕获组添加到列表中
        for match in matches:
            matches_list.append(match.group(1))

# 去重
unique_matches = list(set(matches_list))

# 打印去重后的结果
for item in unique_matches:
    print(item)