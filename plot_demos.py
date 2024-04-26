import numpy as np
import matplotlib.pyplot as plt

from read_demos import *

def display_data(joint_data, tf_data, wrench_data, gripper_data):
    print('joint_time: ' + str(np.shape(joint_data[0])))
    print('joint_positions: ' + str(np.shape(joint_data[1])))
    print('joint_velocities: ' + str(np.shape(joint_data[2])))
    print('joint_effort: ' + str(np.shape(joint_data[3])))
    
    print('transform_time: ' + str(np.shape(tf_data[0])))
    print('transform_positions: ' + str(np.shape(tf_data[1])))
    print('transform_orientations: ' + str(np.shape(tf_data[2])))
    
    print('wrench_time: ' + str(np.shape(wrench_data[0])))
    print('wrench_force: ' + str(np.shape(wrench_data[1])))
    print('wrench_torque: ' + str(np.shape(wrench_data[2])))
    
    print('gripper_time: ' + str(np.shape(gripper_data[0])))
    print('gripper_vals: ' + str(np.shape(gripper_data[1])))
    print('force_time: ' + str(np.shape(gripper_data[2])))
    print('force_vals: ' + str(np.shape(gripper_data[3])))
    return

def plot_joint_data(joint_data, resampled=False):
	js_fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
	js_fig.suptitle('Joints')
	if resampled:
	    time = joint_data[0]
	else:
	    time = joint_data[0][:, 0] + joint_data[0][:, 1] * (10.0**-9)
	for ax, data in [(ax1, joint_data[1]), (ax2, joint_data[2]), (ax3, joint_data[3])]:
		for i in range(np.shape(data)[1]):
			ax.plot(time, data[:, i], label= 'joint' + str(i))
		ax.legend()
	ax3.set_xlabel('time')
	ax1.set_ylabel('positions (rad)')
	ax2.set_ylabel('velocities (rad/s)')
	ax3.set_ylabel('effort')
	
def plot_tf_data(tf_data, resampled=False):
	tf_fig, (ax1, ax2) = plt.subplots(2, 1)
	tf_fig.suptitle('tf')
	if resampled:
	    time = tf_data[0]
	else:
	    time = tf_data[0][:, 0] + tf_data[0][:, 1] * (10.0**-9)
	ax1.plot(time, tf_data[1][:, 0], label='x')
	ax1.plot(time, tf_data[1][:, 1], label='y')
	ax1.plot(time, tf_data[1][:, 2], label='z')
	ax2.plot(time, tf_data[2][:, 0], label='x')
	ax2.plot(time, tf_data[2][:, 1], label='y')
	ax2.plot(time, tf_data[2][:, 2], label='z')
	ax2.plot(time, tf_data[2][:, 3], label='w')
	
	ax1.legend()
	ax2.legend()
	
	ax2.set_xlabel('time')
	ax1.set_ylabel('position')
	ax2.set_ylabel('orientation')
	
	fig = plt.figure()
	fig.suptitle('Trajectory')
	ax = plt.axes(projection='3d')
	ax.plot3D(tf_data[1][:, 0], tf_data[1][:, 1], tf_data[1][:, 2], 'k')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	
	
def plot_wrench_data(wrench_data, resampled=False):
	wr_fig, (ax1, ax2) = plt.subplots(2, 1)
	wr_fig.suptitle('Wrench')
	if resampled:
	    time = wrench_data[0]
	else:
	    time = wrench_data[0][:, 0] + wrench_data[0][:, 1] * (10.0**-9)
	
	ax1.plot(time, wrench_data[1][:, 0], label='x')
	ax1.plot(time, wrench_data[1][:, 1], label='y')
	ax1.plot(time, wrench_data[1][:, 2], label='z')
	ax2.plot(time, wrench_data[2][:, 0], label='x')
	ax2.plot(time, wrench_data[2][:, 1], label='y')
	ax2.plot(time, wrench_data[2][:, 2], label='z')
	
	ax1.legend()
	ax2.legend()
	
	ax2.set_xlabel('time')
	ax1.set_ylabel('force')
	ax2.set_ylabel('torque')
	
def plot_gripper_data(gripper_data, resampled=False):
	gp_fig, (ax1, ax2) = plt.subplots(2, 1)
	gp_fig.suptitle('Gripper')
	if resampled:
	    time = gripper_data[0]
	else:
	    time = gripper_data[0][:, 0] + gripper_data[0][:, 1] * (10.0**-9)
	
	ax1.plot(time, gripper_data[1][:], label="position")
	
	if resampled:
	    ftime = gripper_data[0]
	else:
	    ftime = gripper_data[2][:, 0] + gripper_data[2][:, 1] * (10.0**-9)
	ax2.plot(ftime, gripper_data[3][:], label="force")
	
	ax1.legend()
	ax2.legend()
	
	ax2.set_xlabel('time')
	ax1.set_ylabel('vals')
	ax2.set_ylabel('forces')
	
def plot_data(data, resampled=False):
    joint_data, tf_data, wrench_data, gripper_data = data
    display_data(joint_data, tf_data, wrench_data, gripper_data)
    plot_joint_data(joint_data, resampled)
    plot_tf_data(tf_data, resampled)
    plot_wrench_data(wrench_data, resampled)
    plot_gripper_data(gripper_data, resampled)
    plt.show()
    return
    
if __name__ == '__main__':
    data = pull_data('Mug', 3, 2, downsampled=True, resampled=False)
    plot_data(data)
