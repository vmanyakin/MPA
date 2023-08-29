from pathlib import Path


class PathStorage:
    """
    Allows you to get absolute paths to the main files and directories of the project using the
    __pathlib__ library.
    """
    _DEPTH_RELATIVE_TO_PROJECT_ROOT = 3
    _ABSOLUTE_PATH_TO_PROJECT_ROOT = Path(__file__).parents[_DEPTH_RELATIVE_TO_PROJECT_ROOT]

    @classmethod
    def get_path_to_project_root(cls) -> Path:
        return cls._ABSOLUTE_PATH_TO_PROJECT_ROOT

    @classmethod
    def get_path_to_config(cls) -> Path:
        return cls._ABSOLUTE_PATH_TO_PROJECT_ROOT / "config"

    @classmethod
    def get_path_to_data(cls) -> Path:
        return cls._ABSOLUTE_PATH_TO_PROJECT_ROOT / "data"

    @classmethod
    def get_path_to_src(cls) -> Path:
        return cls._ABSOLUTE_PATH_TO_PROJECT_ROOT / "src"
