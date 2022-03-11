from cruw.visualization.examples import show_dataset_rod2021, show_dataset
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import glob
from cruw import CRUW
from cruw.mapping import ra2idx, idx2ra
import math
data_root='/home/cj4wmz/data/cruw_dataset'

dataset = CRUW(data_root=data_root, sensor_config_name='sensor_config_rod2021')
print(dataset)

# target_dir = '/home/cj4wmz/data/cruw_dataset/sequences/train'
# source_dir = '/home/cj4wmz/data/cruw_dataset/TRAIN_CAM_0'
# image_folder = sorted(os.listdir(source_dir))
# for i in range(len(os.listdir(source_dir))):
#     source_path = os.path.join(source_dir, image_folder[i], 'IMAGES_0')
#     shutil.move(source_path, os.path.join(target_dir, image_folder[i]))
   
print(dataset.sensor_cfg.camera_cfg)
print(dataset.sensor_cfg.radar_cfg)

print('camera intrinsics:')
print(dataset.sensor_cfg.calib_cfg['cam_calib']['2019_04_09']['cam_0']['camera_matrix'])
print('camera to radar translation:')
print(dataset.sensor_cfg.calib_cfg['t_cl2rh'])


# Object classes of interest
print(dataset.object_cfg.classes)

# Map from absolute range(m) and azimuth(rad) to RF indices.
rng = 5.0
azm = math.radians(30)  # degree to radians
rid, aid = ra2idx(rng, azm, dataset.range_grid, dataset.angle_grid)

# Map from RF indices to absolute range(m) and azimuth(rad).

rid = 20
aid = 95
rng, azm = idx2ra(rid, aid, dataset.range_grid, dataset.angle_grid)
print(rng, math.degrees(azm))

#Data Visualization


def get_paths(seq_name, frame_id):
    image_path = os.path.join(data_root, 'sequences', 'train', seq_name,
                              dataset.sensor_cfg.camera_cfg['image_folder'],
                              '%010d.jpg' % frame_id)
    chirp_path = os.path.join(data_root, 'sequences', 'train', seq_name,
                              dataset.sensor_cfg.radar_cfg['chirp_folder'],
                              '%06d_0000.npy' % frame_id)
    anno_path = os.path.join(data_root, 'annotations',
                             'train', seq_name + '.txt')
    return image_path, chirp_path, anno_path

# only cyclist 
seq_name = '2019_04_09_BMS1000'
frame_id = 400
image_path, chirp_path, anno_path = get_paths(seq_name, frame_id)
show_dataset_rod2021(image_path, chirp_path, anno_path, dataset)

# cyclist and pedestrian 
seq_name = '2019_04_09_PMS3000'
frame_id = 200
image_path, chirp_path, anno_path = get_paths(seq_name, frame_id)
show_dataset_rod2021(image_path, chirp_path, anno_path, dataset)

# cclist and pedestrian close to each other 
seq_name = '2019_05_29_PBMS007'
frame_id = 300
image_path, chirp_path, anno_path = get_paths(seq_name, frame_id)
show_dataset_rod2021(image_path, chirp_path, anno_path, dataset)

# three cars at a distance 
seq_name = '2019_09_29_ONRD001'
frame_id = 834
image_path, chirp_path, anno_path = get_paths(seq_name, frame_id)
show_dataset_rod2021(image_path, chirp_path, anno_path, dataset)

# two cars at a distance 
seq_name = '2019_09_29_ONRD002'
frame_id = 900
image_path, chirp_path, anno_path = get_paths(seq_name, frame_id)
show_dataset_rod2021(image_path, chirp_path, anno_path, dataset)


# single car 
seq_name = '2019_09_29_ONRD011'
frame_id = 1000
image_path, chirp_path, anno_path = get_paths(seq_name, frame_id)
show_dataset_rod2021(image_path, chirp_path, anno_path, dataset)

print('done')
