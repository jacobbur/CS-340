from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30868
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@localhost:30868/AAC' % ("aacuser", "SNHU1234"))
	
        self.database = self.client["AAC"]
    
# Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save")

# Create method to implement the R in CRUD.
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria, {"_id": False})
        else:
            data = self.database.animals.find({}, {"_id": False})
        return data
    
# Create method to implement the U in CRUD.
    def update(self, updateData):
        if updateData is not None:
            if updateData:
                result = self.database.animals.insert_one(updateData)
            return result;
        else:
            raise Exception("Nothing to update")
    
# Create method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        return result.raw_result


