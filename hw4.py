import mujoco
import numpy as np
import mujoco_viewer
import time
from mujoco import viewer
import dm_control.mujoco as dm

# Load the model
m = mujoco.MjModel.from_xml_path('hw3.xml')
d = mujoco.MjData(m)

# mujoco.viewer.launch(m,d)
pi = np.pi
idx = 0

with mujoco.viewer.launch_passive(m,d) as viewer:
    for i in range(10000):
        
        if i%50 == 0:
           for j in range(len(d.ctrl)):
               div = np.random.randint(-10, 11) / 10.0
               d.ctrl[j] = np.cos(pi)*div
        dm.mj_step(m,d)
        
        viewer.sync()
        time.sleep(0.01)
    

# viewer = mujoco_viewer.MujocoViewer(m,d)

# for i in range(10000):
#     if viewer.is_alive:
#         mujoco.mj_step(m,d)
#         viewer.render()
#     else:
#         break

# viewer.close()
