#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


class Converter:
    def __init__(self, ):
        pass

    def convert_fbx_to_pcd(self, fbx_path: str, destination: str = './convert/fbx') -> bool:
        #TODO
        return True

    def convert_pcd_to_fbx(self, pcd_path, destination: str ='./convert/pcd') -> bool:
        #TODO
        return True

    def convert_pcd_to_ply(self) -> bool:
        #TODO - output format doesn't have to be .ply  If there is other good format to display and easier to convert, we may use it
        return True

    def convert_ply_to_pcd(self) -> bool:
        #TODO
        return True

    def open_pcd_file(self):
        pass