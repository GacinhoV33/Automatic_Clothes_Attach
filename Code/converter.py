#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pymeshlab
ms = pymeshlab.MeshSet()
ms.load_new_mesh('./files/Final_T_Pose.dae')
ms.save_current_mesh(file_name='./files/Final_T_Pose_from_dae.ply')

# import pyassimp
# import trimesh
#
# # Load the FBX file
# scene = pyassimp.load('human_model.fbx')
#
# # Extract the first mesh in the scene
# mesh = scene.meshes[0]
#
# # Convert the mesh to a trimesh object
# tri_mesh = trimesh.Trimesh(vertices=mesh.vertices, faces=mesh.faces)
#
# # Export the trimesh object as a PLY file
# trimesh.exchange.export.export_mesh(tri_mesh, 'human_model_from_fbx.ply', file_type='ply')

#
# import pyfbx
# import numpy as np
# from plyfile import PlyData, PlyElement
#
# # Load the FBX file
# manager = pyfbx.FbxManager.Create()
# scene = fbx.FbxScene.Create(manager, "")
# importer = fbx.FbxImporter.Create(manager, "")
# importer.Initialize("your_file.fbx", -1)
# importer.Import(scene)
# importer.Destroy()
#
# # Extract the first mesh in the scene
# mesh = scene.GetSrcObject(0)
#
# # Get the vertices and faces as numpy arrays
# vertices = np.array(mesh.GetControlPoints())
# faces = []
# for i in range(mesh.GetPolygonCount()):
#     for j in range(3):
#         faces.append(mesh.GetPolygonVertex(i, j))
# faces = np.array(faces).reshape((-1, 3))
#
# # Define the PLY file header
# ply_header = PlyElement.describe(np.hstack((vertices, np.zeros((vertices.shape[0], 3)))), 'vertex')
# ply_header += PlyElement.describe(faces, 'face')
#
# # Write the PLY file
# ply_data = PlyData([ply_header], text=True)
# ply_data.write('your_file.ply')


class Converter:
    def __init__(self, ):
        pass

    def convert_fbx_to_pcd(self, fbx_path: str, destination: str = './convert/fbx') -> bool:
        # TODO
        return True

    def convert_pcd_to_fbx(self, pcd_path, destination: str = './convert/pcd') -> bool:
        # TODO
        return True

    def convert_pcd_to_ply(self) -> bool:
        # TODO - output format doesn't have to be .ply  If there is other good format to display and easier to convert, we may use it
        return True

    def convert_ply_to_pcd(self) -> bool:
        # TODO
        return True

    def open_pcd_file(self):
        pass
