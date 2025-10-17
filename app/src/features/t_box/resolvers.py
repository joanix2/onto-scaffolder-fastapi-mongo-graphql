from app.src.features.t_box.types import TBoxType, ClassType, DatatypePropertyType, ObjectPropertyType

def tbox_to_type(tbox_doc):
    return TBoxType(
        id=str(tbox_doc["_id"]),
        classes=[ClassType(**c) for c in tbox_doc.get("classes", [])],
        datatype_properties=[DatatypePropertyType(**p) for p in tbox_doc.get("datatype_properties", [])],
        object_properties=[ObjectPropertyType(**p) for p in tbox_doc.get("object_properties", [])],
    )
