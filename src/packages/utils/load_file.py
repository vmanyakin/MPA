import json

from .load_path import PathStorage


class LoadFile:
    """
    Class for uploading files from a project
    """
    path = PathStorage().get_path_to_data()

    @classmethod
    def load_text_messages(cls):
        try:
            with open(cls.path / "text_messages.json") as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError as exception:
            raise Exception(f"File not found see 'data' folder: {exception}")
