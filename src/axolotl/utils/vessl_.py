"""Module for vessl utilities"""

import os

from axolotl.utils.dict import DictDefault


def setup_vessl_env_vars(cfg: DictDefault):
    # VESSL_RUN_INITIAL_CONFIG is a variable that contain path to
    # default credential inside a VESSL Run
    credential_path = os.environ.get("VESSL_RUN_INITIAL_CONFIG")
    print("use_vessl", cfg.use_vessl)
    print("vessl_credential_path", cfg.vessl_credential_path)
    if credential_path:
        cfg.use_vessl = True
        cfg.vessl_credential_path = credential_path
