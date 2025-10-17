from motor.motor_asyncio import AsyncIOMotorClient

# Collection names
TBOX_COLLECTION = "tbox"
ABOX_COLLECTION = "abox"
TEMPLATES_COLLECTION = "templates"
M2T_COLLECTION = "model2text"

# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["ontology_db"]

async def ensure_collections_exist():
    collections = [TBOX_COLLECTION, ABOX_COLLECTION, TEMPLATES_COLLECTION, M2T_COLLECTION]
    existing = await db.list_collection_names()
    for name in collections:
        if name not in existing:
            await db.create_collection(name)

def get_tbox_collection():
    return db[TBOX_COLLECTION]

def get_abox_collection():
    return db[ABOX_COLLECTION]

def get_templates_collection():
    return db[TEMPLATES_COLLECTION]

def get_m2t_collection():
    return db[M2T_COLLECTION]