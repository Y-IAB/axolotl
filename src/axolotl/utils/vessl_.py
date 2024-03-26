"""Module for vessl utilities"""

import os

from axolotl.utils.dict import DictDefault


def setup_vessl_env_vars(cfg: DictDefault):
    # VESSL_RUN_INITIAL_CONFIG is a variable that contain path to
    # default credential inside a VESSL Run
    credential_path = os.environ.get("VESSL_RUN_INITIAL_CONFIG")
    if credential_path:
        cfg.use_vessl = True
        cfg.vessl_credential_path = credential_path
