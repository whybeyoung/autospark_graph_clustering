from abc import ABC
from autospark_kit.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from model_train import TrainTool


class ModelTrainToolKit(BaseToolkit, ABC):
    name: str = "Model Train Toolkit"
    description: str = "图聚类模型训练工具集合"

    def get_tools(self) -> List[BaseTool]:
        return [TrainTool()]

    def get_env_keys(self) -> List[str]:
        return ["Account", "Platform"]
