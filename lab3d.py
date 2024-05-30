#!/usr/bin/env python3
'''Lab 3 - Disk Space Check'''
# Author ID: [your_seneca_id]

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE,shell=True)
    output = p.communicate()[0]
    free_space_str = output.decode('utf-8').strip()
    return free_space_str

if __name__ == '__main__':
    print(free_space())
