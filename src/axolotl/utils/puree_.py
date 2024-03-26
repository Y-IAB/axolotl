"""Module for puree utilities"""

import os

from axolotl.utils.dict import DictDefault


def setup_puree_env_vars(cfg: DictDefault):
    # Enable VESSL if Run Config is present
    credential_path = os.environ.get("VESSL_RUN_INITIAL_CONFIG")
    if credential_path:
        cfg.use_vessl = True
        cfg.vessl_credential_path = credential_path
