# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:36:04 2021
Task: search XML files and zip them.
@author: shaybex
"""

import os, zipfile

compression = zipfile.ZIP_DEFLATED

dirname = r'C:\Users\shaybex\Downloads\archive_msmf'

for (root, dirs, files) in os.walk(dirname):

    for file in files:
        if file.endswith('.xml'):
            os.chdir(root)
            path = os.path.join(root, file)
            with zipfile.ZipFile(file +'.zip', 'w') as zf:
                zf.write(path, compress_type=compression)
            try:
                x = zipfile.ZipFile(file + '.zip')
                print ("% opened ok {}.zip".format(file))
                os.remove(file)
                print("File {} is removed".format(file))
                x.close()
            except:
                print ("File {}.zip is corrupt".format(file))
                continue
        print  ('-'*70)