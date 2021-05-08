'''
把 MD 里面形如 "[206. Reverse Linked List](206. Reverse Linked List.md)"的超链接的"()"里的空格用"%20"替换掉
'''
import re
import os

pattern = re.compile(r'\[.*\](\([0-9]+\. [a-zA-Z0-9 \-\.]*\))')

filename = '代表性题目.md'
tmpfile = open(filename + '.tmp', 'w', encoding='utf8')
file = open(filename, encoding='utf8')
for line in file.readlines():
  while True:  # 把 line 里面匹配的部分全部处理完
    res = re.search(pattern, line)
    if res is None: break
    group1 = res.group(1)
    line = line.replace(group1, group1.replace(' ', '%20'))

  tmpfile.write(line)

file.close()
tmpfile.close()

os.remove(filename)
os.rename(filename + '.tmp', filename)
