#!/usr/bin/python
# -*- coding: utf-8 -*-
import open3d as o3d
from Code.down_sample_pcd import down_sample_pcd
import numpy as np


def down_sample_and_display_pcd(file_path: str, write=False, filename="downsampled_file.pcd"):
    pcd = o3d.io.read_point_cloud(file_path)
    new_pcd = down_sample_pcd(pcd)
    # pcd_array = pcd_to_NN_input(new_pcd)
    o3d.visualization.draw([new_pcd], point_size=1)

    if write:
        write_pcd(new_pcd, filename)


def write_pcd(pcd, filename, write_ascii=True):
    o3d.io.write_point_cloud("./files/pcd/downsampled/" + filename, pcd, write_ascii=write_ascii)


def pcd_to_NN_input(pcd):
    return np.asarray(pcd.points)


down_sample_and_display_pcd('./files/ply/shirt_from_fbx.ply', False)
