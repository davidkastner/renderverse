import bpy


def set_active_gpus():
    """
    The blender file resources are based on the resources of your local machine.
    If you are using a machine that does not have GPUs, this can be a problem.
    We use this script to use all avaliable GPUs regardless of local resources.

    """

    prop = bpy.context.preferences.addons['cycles'].preferences
    prop.get_devices()
    prop.compute_device_type = 'CUDA'

    for device in prop.devices:
        if device.type == 'CUDA':
            device.use = True
    bpy.context.scene.cycles.device = 'GPU'

    for scene in bpy.data.scenes:
        scene.cycles.device = 'GPU'
