# GBTI-Grasping-Dataset
Grasping Dataset collected for grasping several objects with various types of grasps.

Managed by Brendan Hertel (brendan_hertel@student.uml.edu)

Provides 3 versions of the grasping dataset. The dataset is taken for three objects (cube, plate, mug) across 4 users and 5 different positions. All demonstrations were taken using a Universal Robots UR5e manipulator arm. Note that to read this dataset, you will need to be able to read the hdf5 file format. This can be done in Python with h5py, which can be found here: https://www.h5py.org/. The hdf5 file structure is as follows:

![Grasping Dataset](https://github.com/brenhertel/GBTI-Grasping-Dataset/blob/main/grasping_dataset.png)

The shape of the stored arrays is as follows:
- joint_time: n x {time_secs, time_nsecs}
- joint_positions: n x {shoulder_pan_joint, shoulder_lift_joint, elbow_joint, wrist_1_joint, wrist_2_joint, wrist_3_joint}
- joint_velocities: n x {shoulder_pan_joint, shoulder_lift_joint, elbow_joint, wrist_1_joint, wrist_2_joint, wrist_3_joint}
- joint_effort: n x {shoulder_pan_joint, shoulder_lift_joint, elbow_joint, wrist_1_joint, wrist_2_joint, wrist_3_joint}
- transform_time: n x {time_secs, time_nsecs}
- transform_positions: n x {transformX, transformY, transformZ}
- transform_orientations: n x {rotationX, rotationY, rotationZ, rotationW}
- wrench_time: n x {time_secs, time_nsecs}
- wrench_force: n x {x, y, z}
- wrench_torque: n x {x, y, z}
- gripper_time: n x {time_secs, time_nsecs}
- gripper_vals: n x {x}
- force_time: n x {time_secs, time_nsecs}
- forces: n x {x}

Note that the `Grasping_Demos.h5` file provides raw demo data, `Grasping_Demos_DS.h5` provides demonstrations downsampled using the Ramer-Douglas-Peucker algorithm, and `Grasping_Demos_RS.h5` provides demonstrations resampled using a spline for each data stream, with a smoothing factor of 0.1 (see https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html for details). For the DS and RS datasets, all demonstrations are sampled to a length of 1000 samples. For the RS dataset, all time fields are replaced be an n x {time} array, where time includes both seconds and nanoseconds. Additionally, all times in the RS dataset are the same, and start from time t=0.

To view examples of how to read and plot the provided data, see `read_demos.py` and `plot_demos.py` files.
