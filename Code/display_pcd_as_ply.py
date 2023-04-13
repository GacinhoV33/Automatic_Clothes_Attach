#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.down_sample_pcd import down_sample_pcd
import open3d as o3d
import numpy as np

def convert_pcd_to_ply(pcd):
    # normals = o3d.geometry.PointCloud.estimate_normals(pcd, search_param=o3d.geometry.KDTreeSearchParamHybrid(
    #     radius=0.1, max_nn=30))
    # print(pcd.has_normals())
    # print(np.asarray(pcd.normals).shape)
    pcd.estimate_normals()

    mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd)
    print(mesh)
    o3d.visualization.draw_geometries([mesh])


test_pcd = o3d.io.read_point_cloud('./files/pcd/downsampled/downsampled_shirt.pcd')
convert_pcd_to_ply(test_pcd)
