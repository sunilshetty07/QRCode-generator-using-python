# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:12:39 2018

@author: Sunil
"""

import pyqrcode
import png
import cv2
from pyqrcode import QRCode

s=input("enter website: ");
url=pyqrcode.create(s)

url.svg("myqr.svg",scale=8)

url.png("myqrcode.png",scale=6)
