from app.src.features.model2text.types import ModelToTextType, ClassToTextType, TextTransformationType

def model2text_to_type(doc):
    return ModelToTextType(
        id=str(doc["_id"]),
        tbox_id=doc["tbox_id"],
        abox_id=doc["abox_id"],
        class_mappings=[ClassToTextType(
            model=cm["model"],
            transformations=[TextTransformationType(**tf) for tf in cm.get("transformations", [])]
        ) for cm in doc.get("class_mappings", [])]
    )
