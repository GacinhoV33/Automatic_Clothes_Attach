#!/usr/bin/python
# -*- coding: utf-8 -*-

# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# import pygame
# from pygame.locals import *
#
# from OpenGL.GL import *
# from OpenGL.GLU import *
# pygame.init()
# display = (800, 600)
# pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
# glClearColor(0.5, 0.5, 0.5, 0.5)
# glClearDepth(1.0)
# glDepthFunc(GL_LESS)
# glEnable(GL_DEPTH_TEST)
# glShadeModel(GL_SMOOTH)
#
# glMatrixMode(GL_PROJECTION)
# glLoadIdentity()
# gluPerspective(45.0, float(display[0])/float(display[1]), 0.1, 100.0)
#
# # glMatrixMode(GL_MODELVIEW)
# # glLoadIdentity()
# # glTranslatef(0.0,0.0,-5.0)
#
# # glBegin(GL_TRIANGLES)
# # for face in faces:
# #     for vertex in face:
# #         glVertex3fv(vertices[vertex-1])
# # glEnd()
# def load_obj(filename):
#     vertices = []
#     faces = []
#
#     with open(filename) as f:
#         for line in f:
#             if line.startswith('v '):
#                 vertex = list(map(float, line.split()[1:]))
#                 vertices.append(vertex)
#             elif line.startswith('f '):
#                 face = list(map(int, [i.split('/')[0] for i in line.split()[1:]]))
#                 faces.append(face)
#
#     return vertices, faces
#
# vertices, faces = load_obj('./files/fbx/shirt.obj')
# glLoadIdentity()
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#     glRotatef(1, 3, 1, 1)
#     glBegin(GL_TRIANGLES)
#     for face in faces:
#         print("Im in")
#         for vertex in face:
#
#             glVertex3fv(vertices[vertex])
#     glEnd()
#     pygame.display.flip()
#     pygame.time.wait(10)
#
#


# my_conv = Converter('./files/fbx/shirt3.obj')
# manager = fbx.FbxManager.Create()
# importer = fbx.FbxImporter.Create(manager, '')
# importer.Initialize('./files/shirt3.ply', -1)
# scene = fbx.FbxScene.Create(manager, 'scene')
#
# importer.Import(scene)
# importer.Destroy()
# textureArray = fbx.FbxTextureArray()
# scene.FillTextureArray(textureArray)
# # scene = load_fbx('./files/fbx/shirt.fbx')
# print(textureArray.GetCount())
# # print()
# texture = textureArray.GetAt(1)
# textureFileName = texture.GetFileName()
# image = Image.open(textureFileName)
# width, height = image.size
# print(width, height)

# --------------------------------------------OLD PCD DISPLAYING ---------------------------------------------------
# def load_fbx(filename):
#     manager = fbx.FbxManager.Create()
#     importer = fbx.FbxImporter.Create(manager, '')
#     importer.Initialize(filename, -1)
#     scene = fbx.FbxScene.Create(manager, 'scene')
#
#     importer.Import(scene)
#     importer.Destroy()
#     textureArray = fbx.FbxTextureArray()
#     scene.FillTextureArray(textureArray)
#     return scene
#
#
# def display_pcd(path: str, color_paint: Union[None, Tuple]=None):
#     pcd = o3d.io.read_point_cloud(path)
#     print(pcd)
#     points = np.asarray(pcd.points)
#     colors = None
#     if pcd.has_colors():
#         colors = np.asarray(pcd.colors)
#         print("Im in 1")
#     elif pcd.has_normals():
#         colors = (0.5, 0.5, 0.5) + np.asarray(pcd.normals) * 0.5
#         print("Im in 2")
#     else:
#         colors = np.asarray(pcd.colors)
#         print("Im in 3")
#
#     if color_paint:
#         o3d.geometry.PointCloud.paint_uniform_color(pcd, color=color_paint)
#
#     fig = go.Figure(
#         data=[
#             go.Scatter3d(
#                 x=points[:, 0], y=points[:, 1], z=points[:, 2],
#                 mode='markers',
#                 marker=dict(size=1, color=colors)
#             )
#         ],
#         layout=dict(
#             scene=dict(
#                 xaxis=dict(visible=False),
#                 yaxis=dict(visible=False),
#                 zaxis=dict(visible=False)
#             )
#         )
#     )
#     fig.show()
#
#
# def display_ply(ply_path: str) -> None:
#     # NOTE -> Not all ply files are able to display. To display it, there is need to have triangles counted. Not all ply
#     # files has triangles counted, especially files after conversion from PCD to PLY
#     # http://www.open3d.org/docs/latest/tutorial/Advanced/surface_reconstruction.html
#     #TODO -> check how to count triangles for files without them
#     mesh = o3d.io.read_triangle_mesh(ply_path)
#     if not mesh.has_vertex_normals(): mesh.compute_vertex_normals()
#     if not mesh.has_triangle_normals(): mesh.compute_triangle_normals()
#     triangles = np.asarray(mesh.triangles)
#     vertices = np.asarray(mesh.vertices)
#     colors = None
#     if mesh.has_triangle_normals():
#         colors = (0.5, 0.5, 0.5) + np.asarray(mesh.triangle_normals) * 0.5
#         colors = tuple(map(tuple, colors))
#     else:
#         colors = (1.0, 0.0, 0.0)
#     fig = go.Figure(
#         data=[
#             go.Mesh3d(
#                 x=vertices[:, 0],
#                 y=vertices[:, 1],
#                 z=vertices[:, 2],
#                 i=triangles[:, 0],
#                 j=triangles[:, 1],
#                 k=triangles[:, 2],
#                 facecolor=colors,
#                 opacity=0.50)
#         ],
#         layout=dict(
#             scene=dict(
#                 xaxis=dict(visible=False),
#                 yaxis=dict(visible=False),
#                 zaxis=dict(visible=False)
#             )
#         )
#     )
#     fig.show()
#
#
# def display_fbx(path: str) -> None:
#     scene = load_fbx('./files/fbx/shirt.fbx')
#
#
# def obj_data_to_mesh3d(odata):
#     # odata is the string read from an obj file
#     vertices = []
#     faces = []
#     lines = odata.splitlines()
#
#     for line in lines:
#         slist = line.split()
#         if slist:
#             if slist[0] == 'v':
#                 vertex = np.array(slist[1:], dtype=float)
#                 vertices.append(vertex)
#             elif slist[0] == 'f':
#                 face = []
#                 for k in range(1, len(slist)):
#                     face.append([int(s) for s in slist[k].replace('//','/').split('/')])
#                 if len(face) > 3: # triangulate the n-polyonal face, n>3
#                     faces.extend([[face[0][0]-1, face[k][0]-1, face[k+1][0]-1] for k in range(1, len(face)-1)])
#                 else:
#                     faces.append([face[j][0]-1 for j in range(len(face))])
#             else:
#                 pass
#
#     return np.array(vertices), np.array(faces)
