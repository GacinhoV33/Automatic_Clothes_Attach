#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np


def down_sample_pcd(pcd_obj, output_shape) -> np.array:
    # TODO Think a way to reduce/maximize size to specific Neural Network input shape
    # This is needed to have one format of files that will train NN model
    downpcd = pcd_obj.voxel_down_sample(voxel_size=0.02)
    return downpcd
