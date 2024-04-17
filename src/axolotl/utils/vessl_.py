"""Module for vessl utilities"""

import os

from axolotl.utils.dict import DictDefault


def setup_vessl_env_vars(cfg: DictDefault):
    if cfg.vessl_credential_path:
        return

    # VESSL_RUN_INITIAL_CONFIG is a variable that contain path to default credential inside a VESSL Run.
    # Currently there is no docs regarding this variable, but it exists inside the container.
    # Ref: https://screen.yanolja.in/lrTGow4Pr8eXhAai.png
    credential_path = os.environ.get("VESSL_RUN_INITIAL_CONFIG")
    if credential_path:
        cfg.vessl_credential_path = credential_path
