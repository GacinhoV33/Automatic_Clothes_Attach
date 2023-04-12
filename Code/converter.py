#!/usr/bin/python
# -*- coding: utf-8 -*-
import aspose.threed as a3d

class Converter:
    def __init__(self, file_path: str, output_name='obj_file.obj'):
        self.file_path = file_path
        self.output_path = output_name
        if self.file_path.split('.')[-1] == "obj":
            self.convert_obj_to_ply()

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

    def convert_obj_to_ply(self,):
        a3d.TrialException = False
        scene = a3d.Scene.from_file(self.file_path)
        scene.save('./converted_files/' + self.output_path)

    def open_pcd_file(self):
        pass
