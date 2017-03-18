# coding=utf-8

from string import Template

t = Template('${village} folk send $$10 to $cause')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    # class BatchNameByYaya(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
print(fmt)
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0}->{1}'.format(filename, newname))
