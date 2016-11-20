# -*- coding: utf-8 -*-

# given some structure like ![pool](http://ww1.sinaimg.cn/large/006tNc79gw1f9k6ilaabuj30hg0eo76b.jpg), output its centered image md instance like:
# <img src="http://ww4.sinaimg.cn/large/006tNc79gw1f9z8nk1m0fj31kw23ue81.jpg" style="display: block; margin: 0 auto;">

import os
import re
from sys import argv


# Match image in Markdown pattern
INSERT_IMAGE_PATTERN = re.compile('(\!\[.*?\]\((.*?)\))', re.DOTALL)

# Find image list in Markdown file
def get_image_list_from_md(md_path):
    md_file = open(md_path)
    content = md_file.read()
    image_list = re.findall(INSERT_IMAGE_PATTERN, content)
    return image_list

# def replace_img(source_md, target_md, conn):
def replace_img(source_md, target_md):
    image_list = get_image_list_from_md(source_md)
    md_content = open(source_md).read()
    fb = open(target_md, 'w')

    print 'start >>>>>\n'

    for image in image_list:
        print image[0]
        md_content = md_content.replace(image[0], '<img src="' + image[1] + '" style="display: block; margin: 0 auto;">');
    print '\n<<<<< end'

    fb.write(md_content)
    fb.close()


def main(script_file, source, target):
    if os.path.exists(source):
        replace_img(source, target)
    else:
        print 'source file not exist'


if __name__ == '__main__':
    if len(argv) > 2:
        script, source_file, target_file = argv
        main(script, source_file, target_file)
    else:
        print 'please enter source file and target file'
