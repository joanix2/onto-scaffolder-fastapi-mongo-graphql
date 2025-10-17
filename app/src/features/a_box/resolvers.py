from app.src.features.a_box.types import ABoxType, InstanceType, RelationType

def abox_to_type(abox_doc):
    return ABoxType(
        id=str(abox_doc["_id"]),
        instances=[InstanceType(**i) for i in abox_doc.get("instances", [])],
        relations=[RelationType(**r) for r in abox_doc.get("relations", [])],
    )
