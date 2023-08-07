from autospark_kit.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


def train(epoch, lr, alpha1, alpha2):
    return f"开始图聚类训练， 使用如下参数: {epoch}， {lr}, {alpha1}, {alpha2}"


def _query():
    return ["爆炒青椒", "炒拉面", "蛋炒饭"]


class TrainInput(BaseModel):
    epoch: int = Field(..., description="训练轮数")
    lr: float = Field(..., description="学习率")
    alpha1: float = Field(..., description="0-1的图卷积神经网络损失函数权重",default=0.001)
    alpha2: float = Field(..., description="0-1的自动编码器的损失函数权重",default=0.001)


class TrainTool(BaseTool):
    """
    BookFoodTool
    """
    name: str = "Graph Clustering Tool"
    args_schema: Type[BaseModel] = TrainInput
    description: str = "帮助用户自动训练图聚类模型"

    def _execute(self, epoch: int = 1, lr: float = 0.001, alpha1: float = 0.001, alpha2: float = 0.001):
        return train(epoch, lr, alpha1, alpha2)


class QueryFoodInput(BaseModel):
    query: str = Field(..., description="外卖搜索查询条件")


class QueryFoodTool(BaseTool):
    """
    QueryFoodTool
    """
    name: str = "Query Food  Tool "
    args_schema: Type[BaseModel] = QueryFoodInput
    description: str = "一个帮助用户查询符合条件的外卖的工具"

    def _execute(self, query: str = None):
        return _query()
