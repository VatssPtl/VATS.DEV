import bpy, os
ROOT = r'F:\VATS.DEV\Scarecrow'
MASTER = os.path.join(ROOT,'01_Blender','Master','scarecrow_master.blend')
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
scene = bpy.context.scene
for c in list(scene.collection.children): scene.collection.children.unlink(c)
def create_collection(name,parent):
    c=bpy.data.collections.new(name); parent.children.link(c); return c
root=create_collection('VATS_DEV_SCARECROW',scene.collection)
reference=create_collection('00_REFERENCE',root)
for n in ['01_CHARACTER_BIBLE','02_EMOTION_LIBRARY','03_RIGGING_REFERENCE']: create_collection(n,reference)
character=create_collection('01_CHARACTER',root)
for n in ['01_BODY','02_HEAD','03_FACE','04_HAIR','05_CLOTHING','06_ACCESSORIES']: create_collection(n,character)
for n in ['02_RIG','03_MATERIALS','04_LIGHTING','05_CAMERAS','06_ENVIRONMENT']: create_collection(n,root)
scene.unit_settings.system='METRIC'; scene.unit_settings.scale_length=1.0; scene.unit_settings.length_unit='METERS'
scene.render.fps=30; scene.render.fps_base=1.0; scene.frame_start=1; scene.frame_end=250; scene.frame_set(1)
scene.render.engine='CYCLES'; scene.cycles.device='CPU'; scene.cycles.samples=64; scene.cycles.preview_samples=16; scene.cycles.use_denoising=True
scene.render.resolution_x=1920; scene.render.resolution_y=1080; scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'; scene.render.image_settings.color_mode='RGBA'; scene.render.filepath='//../../08_Render/'
scene.view_settings.view_transform='AgX'
scene['project_name']='VATS.DEV Scarecrow'; scene['project_version']='1.0'; scene['blender_baseline']=bpy.app.version_string; scene['project_stage']='Foundation'; scene['character_height_reference']='6.8 head-heights'; scene['character_orientation']='Front-facing along -Y'
os.makedirs(os.path.dirname(MASTER),exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=MASTER)
print('='*55)
print('VATS.DEV SCARECROW FOUNDATION CREATED')
print('Blender:',bpy.app.version_string)
print('Master:',MASTER)
print('Collections:',len(bpy.data.collections))
print('Objects:',len(scene.objects))
print('Render Engine:',scene.render.engine)
print('Units:',scene.unit_settings.system)
print('='*55)
