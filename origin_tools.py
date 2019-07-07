
bl_info = {
    "name": "Snap/Set origin Tools",
    "author": "Wilson Romero",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Snap/Set origin Tools",
    "description": "Add set origin/snap options to the right pannel",
    "category": "Object",
}

import bpy


######################################################
######################################################
#####            origin classes
######################################################
######################################################

#cursor to geometry calculated by the center of the object
class wilsoft_origin_to_geometry(bpy.types.Operator):
    bl_idname = "object.set_origin_center_object"
    bl_label = "Geometry"
    
    def execute(self, context):
        try:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}
        
        
#cursor to 3d cursor
class wilsoft_origin_to_centermass(bpy.types.Operator):
    bl_idname = "object.set_origin_centermass"
    bl_label = "Center of mass"
    
    def execute(self, context):
        try:
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}
        
#cursor to center of mass
class wilsoft_origin_to_3dcursor(bpy.types.Operator):
    bl_idname = "object.set_origin_3dcursor"
    bl_label = "3d Cursor"
    
    def execute(self, context):
        try:
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}

#cursor to center of mass surface
class wilsoft_origin_to_centermass_surf(bpy.types.Operator):
    bl_idname = "object.set_origin_centermass_surf"
    bl_label = "Center of mass (surface)"
    
    def execute(self, context):
        try:
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}
        
#cursor to center of mass volume
class wilsoft_origin_to_centermass_vol(bpy.types.Operator):
    bl_idname = "object.set_origin_centermass_vol"
    bl_label = "Center of mass (volume)"
    
    def execute(self, context):
        try:
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}
        
#object to 3d cursor
class wilsoft_geometry_to_origin(bpy.types.Operator):
    bl_idname = "object.set_geometry_to_origin"
    bl_label = "Object to origin"
    
    def execute(self, context):
        try:
            bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}
        
        
######################################################
######################################################
#####            3d cursor classes
######################################################
######################################################

#cursor to selected
class wilsoft_cursor_to_selected(bpy.types.Operator):
    bl_idname = "object.set_cursor_to_selected"
    bl_label = "Selected"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_cursor_to_selected()
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}


#cursor to world center
class wilsoft_cursor_to_world_center(bpy.types.Operator):
    bl_idname = "object.set_cursor_to_world_center"
    bl_label = "World center"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_cursor_to_center()
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}


#cursor to grid
class wilsoft_cursor_to_grid(bpy.types.Operator):
    bl_idname = "object.set_cursor_to_grid"
    bl_label = "Grid"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_cursor_to_grid()
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}

#cursor to active
class wilsoft_cursor_to_active(bpy.types.Operator):
    bl_idname = "object.set_cursor_to_active"
    bl_label = "Active"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_cursor_to_active()
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}
        
        
        
######################################################
######################################################
#####            Selected classes
######################################################
######################################################

#selection to grid
class wilsoft_selected_to_grid(bpy.types.Operator):
    bl_idname = "object.set_selected_to_grid"
    bl_label = "Grid"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_selected_to_grid()
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}

#selection to cursor
class wilsoft_selected_to_cursor(bpy.types.Operator):
    bl_idname = "object.set_selected_to_cursor"
    bl_label = "Cursor"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}

#selection to cursor offset
class wilsoft_selected_to_cursor_offset(bpy.types.Operator):
    bl_idname = "object.set_selected_to_cursor_offset"
    bl_label = "Cursor (with offset)"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}

#selection to active
class wilsoft_selected_to_active(bpy.types.Operator):
    bl_idname = "object.set_selected_to_active"
    bl_label = "Active"
    
    def execute(self, context):
        try:
            bpy.ops.view3d.snap_selected_to_active()
            return {'FINISHED'}
        except:
            print('Object without a center')
            return{'CANCELLED'}




######################################################
######################################################
#####            layout
######################################################
######################################################
class wilsoft_tools_origin(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Object Origin"
    bl_idname = "OBJECT_PT_WILSOFT_ORIGIN"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Snap/Set origin Tools"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.label(text="Set origin to:", icon='OBJECT_ORIGIN')

        col = layout.column(align=True)
        col.operator("object.set_geometry_to_origin")
        col.operator("object.set_origin_center_object")
        col.operator("object.set_origin_3dcursor")
        col.operator("object.set_origin_centermass")
        col.operator("object.set_origin_centermass_surf")
        col.operator("object.set_origin_centermass_vol")
        
        
class wilsoft_tools_3dcursor(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "3d cursor"
    bl_idname = "OBJECT_PT_WILSOFT_3DCURSOR"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Snap/Set origin Tools"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.label(text="Snap 3D cursor to:", icon='PIVOT_CURSOR')


        col = layout.column(align=True)
        col.operator("object.set_cursor_to_selected")
        col.operator("object.set_cursor_to_world_center")
        col.operator("object.set_cursor_to_grid")
        col.operator("object.set_cursor_to_active")
        
        
class wilsoft_tools_selected(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Selected"
    bl_idname = "OBJECT_PT_WILSOFT_SELECTED"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Snap/Set origin Tools"

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.label(text="Snap selection to:", icon='RESTRICT_SELECT_OFF')


        col = layout.column(align=True)
        col.operator("object.set_selected_to_grid")
        col.operator("object.set_selected_to_cursor")
        col.operator("object.set_selected_to_cursor_offset")
        col.operator("object.set_selected_to_active")
        
        

classes = (
    wilsoft_tools_3dcursor,
    wilsoft_tools_origin,
    wilsoft_tools_selected,
    wilsoft_geometry_to_origin,
    wilsoft_origin_to_3dcursor,
    wilsoft_origin_to_geometry,
    wilsoft_origin_to_centermass,
    wilsoft_origin_to_centermass_surf,
    wilsoft_origin_to_centermass_vol,
    wilsoft_cursor_to_selected,
    wilsoft_cursor_to_world_center,
    wilsoft_cursor_to_grid,
    wilsoft_cursor_to_active,
    wilsoft_selected_to_grid,
    wilsoft_selected_to_cursor,
    wilsoft_selected_to_cursor_offset,
    wilsoft_selected_to_active    
    
)


def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    # Register QueryProps
    #bpy.types.Scene.QueryProps = bpy.props.PointerProperty(type=QueryProps)


def unregister():

    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    # $ delete QueryProps on unregister
    #del(bpy.types.Scene.QueryProps)

if __name__ == "__main__":
    register()