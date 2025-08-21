import bpy
import bmesh
import json
import sys
import os

vmj = 4
vmm = 0
vmn = 0

def is_bpy_400():
    version = bpy.app.version
    return version >= (vmj, vmm, vmn)

def process_object(obj, faces_to_select, vg_name):
    max_index = len(obj.data.polygons) - 1
    valid_faces = [i for i in faces_to_select if i <= max_index]

    if not valid_faces:
        print(f"No valid faces for object {obj.name}")
        return

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(obj.data)

    for f in bm.faces:
        if f.select and f.index not in valid_faces:
            f.select = False

    bmesh.update_edit_mesh(obj.data)
    bpy.ops.object.mode_set(mode='OBJECT')

    vg = obj.vertex_groups.new(name=vg_name)
    verts = set()
    for idx in valid_faces:
        verts.update(obj.data.polygons[idx].vertices)
    vg.add(list(verts), 1.0, 'ADD')
    
    if False:
        vg_verts = {v.index for v in obj.data.vertices if vg.index in [g.group for g in v.groups]}
        faces_in_vg = [f.index for f in obj.data.polygons if any(v in vg_verts for v in f.vertices)]
        print(f"Faces associated with vertex group '{vg_name}':", faces_in_vg)

def import_obj(input_path):
    if is_bpy_400():
        bpy.ops.wm.obj_import(
            filepath=input_path,
            import_vertex_groups=True,
            use_split_objects=True,
            validate_meshes=True,
        )
    else:
        bpy.ops.import_scene.obj(
            filepath=input_path,
            use_split_objects=True,
            use_groups_as_vgroups=True,
            split_mode='OFF',
        )

def export_obj(output_path):
    if is_bpy_400():
        bpy.ops.wm.obj_export(
            filepath=output_path,
            export_selected_objects=True,
            export_vertex_groups=True,
            export_object_groups=True,
        )
    else:
        bpy.ops.export_scene.obj(
            filepath=output_path,
            use_selection=True,
            use_vertex_groups=True,
            group_by_object=True,
            keep_vertex_order=True,
        )

def main():
    m = None
    if bpy.app.version < (2, 80, 0):
        m = "This script requires Blender 2.80 or higher.\n"
    if is_bpy_400():
        # doesn't export our new vertex group for some reason
        # tell them to get an older version for now
        v = f"{vmj}.{vmm}.{vmn}"
        m = f"Exporting polygroups is not working if you're on {v} or newer.\nPlease use blender older than {v} to use script.\n"
    if m != None:
        print(f"{m}You are running {bpy.app.version_string}")
        return
    argv = sys.argv
    u = "<input.obj> <output.obj> <faces.json or list.txt>"
    if "--" not in argv:
        print(f"Usage: {argv[0]} --background --python ExcludeFaces.py -- {u}")
        return
    argv = argv[argv.index("--") + 1:]
    if len(argv) != 3:
        print(f"Provide 3 arguments: {u}")
        return

    input_path, output_path, faces_arg = argv

    if not os.path.exists(input_path):
        print(f"Input file does not exist: {input_path}")
        return

    faces_to_select = []

    if faces_arg.lower().endswith(".txt"):
        if not os.path.exists(faces_arg):
            print(f"Faces list file does not exist: {faces_arg}")
            return
        json_files = []
        with open(faces_arg, "r") as list_file:
            for line in list_file:
                line = line.strip()
                if not line:
                    continue
                # Skip comments
                isTxtJson = (line.lower().endswith(".txt") or line.lower().endswith(".json")) is False
                if line.startswith((";", "#", "//", "--")) or isTxtJson:
                    print(f"skip line `{line}`")
                    continue
                print(f"append `{line}`")
                json_files.append(line)
    else:
        json_files = [faces_arg]

    for faces_json in json_files:
        print(f"open `{faces_json}`")
        if not os.path.exists(faces_json):
            print(f"Faces JSON file does not exist: {faces_json}")
            return
        with open(faces_json, "r") as f:
            data = json.load(f)
            if not isinstance(data, list):
                print(f"Faces JSON must contain a list of indices: {faces_json}")
                return
            faces_to_select.extend(data)

    import_obj(input_path)

    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            process_object(obj, faces_to_select, "wrap_exclude")

    export_obj(output_path)

if __name__ == "__main__":
    main()
