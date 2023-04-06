#!/usr/bin/python
# -*- coding: utf-8 -*-
import open3d as o3d
import plotly.graph_objects as go
import numpy as np
from typing import Tuple, Union


def display_pcd(path: str, color_paint: Union[None, Tuple]=None):
    pcd = o3d.io.read_point_cloud(path)
    print(pcd)
    points = np.asarray(pcd.points)
    colors = None
    if pcd.has_colors():
        colors = np.asarray(pcd.colors)
        print("Im in 1")
    elif pcd.has_normals():
        colors = (0.5, 0.5, 0.5) + np.asarray(pcd.normals) * 0.5
        print("Im in 2")
    else:
        colors = np.asarray(pcd.colors)
        print("Im in 3")

    if color_paint:
        o3d.geometry.PointCloud.paint_uniform_color(pcd, color=color_paint)

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=points[:, 0], y=points[:, 1], z=points[:, 2],
                mode='markers',
                marker=dict(size=1, color=colors)
            )
        ],
        layout=dict(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            )
        )
    )
    fig.show()


def display_ply(ply_path: str) -> None:
    # NOTE -> Not all ply files are able to display. To display it, there is need to have triangles counted. Not all ply
    # files has triangles counted, especially files after conversion from PCD to PLY
    # http://www.open3d.org/docs/latest/tutorial/Advanced/surface_reconstruction.html
    #TODO -> check how to count triangles for files without them
    mesh = o3d.io.read_triangle_mesh(ply_path)
    if not mesh.has_vertex_normals(): mesh.compute_vertex_normals()
    if not mesh.has_triangle_normals(): mesh.compute_triangle_normals()
    triangles = np.asarray(mesh.triangles)
    vertices = np.asarray(mesh.vertices)
    colors = None
    if mesh.has_triangle_normals():
        colors = (0.5, 0.5, 0.5) + np.asarray(mesh.triangle_normals) * 0.5
        colors = tuple(map(tuple, colors))
    else:
        colors = (1.0, 0.0, 0.0)
    fig = go.Figure(
        data=[
            go.Mesh3d(
                x=vertices[:, 0],
                y=vertices[:, 1],
                z=vertices[:, 2],
                i=triangles[:, 0],
                j=triangles[:, 1],
                k=triangles[:, 2],
                facecolor=colors,
                opacity=0.50)
        ],
        layout=dict(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            )
        )
    )
    fig.show()



display_pcd('./files/test_pcd.pcd', (0.1, 0.3, 0.5))
display_ply('./files/knot.ply')