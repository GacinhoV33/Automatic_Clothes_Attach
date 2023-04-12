#!/usr/bin/python
# -*- coding: utf-8 -*-
import open3d as o3d
from Code.down_sample_pcd import down_sample_pcd


def down_sample_and_display_pcd(file_path: str):
    pcd = o3d.io.read_point_cloud(file_path)
    downsampled_pcd = down_sample_pcd(pcd)
    o3d.visualization.draw([downsampled_pcd], point_size=1)


def write_pcd(pcd, filename, write_ascii=True):
    o3d.io.write_point_cloud("./files/pcd/downsampled/" + filename, pcd, write_ascii=write_ascii)


down_sample_and_display_pcd('test_pcd_write.pcd')
