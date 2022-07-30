import bpy


# get list of root objects in curent scene
# and prin object name in console
def getRootObject():
    objects = []
    for obj in bpy.data.objects:
        if obj.parent is None:
            objects.append(obj)
    return objects




# iterate over objects and put object in collection viz same name as object
def putObjectsInCollection(objects):
    for obj in objects:
        if obj.name not in bpy.data.collections:
            print(obj.name)

            collection = bpy.data.collections.new(obj.name)
            # add collection to scene
            bpy.context.scene.collection.children.link(collection)

        # if object in colletion not mache object name unlink and link to new collection
        if obj.name not in bpy.data.collections[obj.name].objects:
            bpy.data.collections[obj.name].objects.link(obj)

# get root object in curent scene and put all objects in collection viz same name as object
def putAllObjectsInCollection():
    putObjectsInCollection(getRootObject())

#call function to put all objects in collection
putAllObjectsInCollection()


