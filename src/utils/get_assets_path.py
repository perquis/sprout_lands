import os


def get_assets_path(start_path):
    for root, dirs, files in os.walk(start_path):
        if "assets" in dirs:
            return os.path.join(root, "assets")

    return None
