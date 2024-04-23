"""Vessl module for trainer callbacks"""
import logging
from typing import Dict

import vessl
from transformers import TrainerCallback, TrainerControl, TrainerState
from transformers.training_args import TrainingArguments

LOG = logging.getLogger("axolotl.callbacks")


class VesslLogMetricsCallback(TrainerCallback):
    """Callback to send training metrics to VESSL AI"""

    def __init__(self, credential_path: str) -> None:
        vessl.configure(credentials_file=credential_path)

    def on_log(
        self,
        args: TrainingArguments,  # pylint: disable=unused-argument
        state: TrainerState,
        control: TrainerControl,  # pylint: disable=unused-argument
        logs: Dict[str, float],
        **kwargs  # pylint: disable=unused-argument
    ):
        # is_world_process_zero: Whether or not this process is the global main process (when training in a
        # distributed fashion on several machines, this is only going to be `True` for one process).
        if state.is_world_process_zero:
            vessl.log(logs, state.global_step)
