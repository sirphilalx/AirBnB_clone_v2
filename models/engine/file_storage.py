#!/usr/bin/python3
""" A FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ A class FileStorage that serializes instances to a
        JSON file and deserializes JSON file to instances:

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns the list of objects of one type of class if class is
            specified, else it returns the dictionary __objects """
        if cls is not None:
            if (type(cls) == str):
                cls = eval(cls)
            cls_dict = {k: v for k, v in self.__objects.items()
                        if type(v) == cls}
            return cls_dict
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        oc_name = obj.__class__.__name__
        self.__objects["{}.{}".format(oc_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        json_data = {}
        for k, v in self.__objects.items():
            json_data[k] = v.to_dict()
        with open(self.__file_path, 'w') as jsonf:
            json.dump(json_data, jsonf)

    def delete(self, obj=None):
        """ Deletes obj from __objects if it’s inside - if obj is equal to
            None, the method does nothing """
        if obj is not None:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        else:
            pass

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised) """
        try:
            with open(self.__file_path) as jsonf:
                data = json.load(jsonf)
                for key, obj in data.items():
                    newObj = eval(obj["__class__"])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            return

    def close(self):
        """ Calls the reload() method to deserialize JSON file to objects """
        self.reload()
