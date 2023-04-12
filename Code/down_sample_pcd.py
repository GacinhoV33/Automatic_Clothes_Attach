#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np

DESIRED_SIZE = 5000


def down_sample_pcd(pcd, output_size=DESIRED_SIZE) -> np.array:
    num_points = len(pcd.points)
    ratio = output_size / num_points
    if ratio < 1:
        downsampled_pcd = pcd.uniform_down_sample(every_k_points=int(1 / ratio))
        downsampled_num_points = len(downsampled_pcd.points)
        num_to_drop = downsampled_num_points - output_size

        if num_to_drop > 0:
            desired_pcd = drop_points(downsampled_pcd, num_to_drop, output_size)
        else:
            raise ValueError()
    elif ratio > 1:
        #TODO implement logic that adds points
        raise NotImplementedError()
    else:
        desired_pcd = pcd

    return desired_pcd


def drop_points(pcd, num_to_drop, output_size):
    indices_to_drop = np.random.choice(output_size, num_to_drop, replace=False)
    desired_pcd = pcd.select_by_index(indices_to_drop, invert=True)
    return desired_pcd

