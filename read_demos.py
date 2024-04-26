import numpy as np
import h5py

def pull_data(object_type, user_num, position_num, downsampled=True, resampled=False):
    if downsampled:
        hf = h5py.File('Grasping_Demos_DS.h5', 'r')
    elif resampled:
        hf = h5py.File('Grasping_Demos_RS.h5', 'r')
    else: 
        hf = h5py.File('Grasping_Demos.h5', 'r')
    print(list(hf.keys()))
    obj = hf.get(object_type)
    print(list(obj.keys()))
    user = obj.get('User' + str(user_num))
    print(list(user.keys()))
    pos = user.get('Position' + str(position_num))
    print(list(pos.keys()))
    js = pos.get('joint_state_info')
    jt, jp, jv, je = np.array(js.get('joint_time')), np.array(js.get('joint_positions')), np.array(js.get('joint_velocities')), np.array(js.get('joint_effort'))
    tf = pos.get('transform_info')
    tt, tp, tr = np.array(tf.get('transform_time')), np.array(tf.get('transform_positions')), np.array(tf.get('transform_orientations'))
    wr = pos.get('wrench_info')
    wt, wf, wm = np.array(wr.get('wrench_time')), np.array(wr.get('wrench_force')), np.array(wr.get('wrench_torque'))
    gf = pos.get('gripper_info')
    gt, gp, ft, fp = np.array(gf.get('gripper_time')), np.array(gf.get('gripper_vals')), np.array(gf.get('force_time')), np.array(gf.get('forces'))
    hf.close()
    return [[jt, jp, jv, je], [tt, tp, tr], [wt, wf, wm], [gt, gp, ft, fp]]

def pull_data_across_users(object_type, position_num, downsampled=True, resampled=False):
    data = []
    for user_num in range(1, 5):
        data.append(pull_data(object_type, user_num, position_num, downsampled, resampled))
    return data
    
if __name__ == '__main__':
    pull_data('Cube', 3, 2, downsampled=False, resampled=True)
    data = pull_data_across_users('Plate', 1)
    print(data)
