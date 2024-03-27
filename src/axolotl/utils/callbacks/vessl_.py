"""Vessl module for trainer callbacks"""
import logging
from typing import Dict, List

import vessl
from transformers import TrainerCallback, TrainerControl, TrainerState
from transformers.training_args import TrainingArguments

LOG = logging.getLogger("axolotl.callbacks")

class VesslLogMetricsCallback(TrainerCallback):

    def __init__(self, credential_path: str, metrics: List[str]) -> None:
        vessl.configure(credentials_file=credential_path)

    def on_log(self, args: TrainingArguments, state: TrainerState, control: TrainerControl, logs: Dict[str, float] = None, **kwargs):     
        if state.is_world_process_zero:
            vessl.log(logs, state.global_step)

