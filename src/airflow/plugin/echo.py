import logging

from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class EchoOperator(BaseOperator):

    @apply_defaults
    def __init__(self, message: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message

    def execute(self, context) -> None:
        logging.info(self.message)


class EchoAirflowPlugin(AirflowPlugin):
    name = 'echo'
    operators = [EchoOperator]
