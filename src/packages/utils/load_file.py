import json

from .load_path import PathStorage


class LoadFile:
    """
    Class for uploading files from a project
    """
    path = PathStorage().get_path_to_data()

    @classmethod
    def load_json(cls, name_file):
        try:
            with open(cls.path / name_file, encoding="utf-8") as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError as exception:
            raise Exception(f"File not found see 'data' folder: {exception}")
