import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
from rasa.nlu.tokenizers.tokenizer import Token

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


def _is_list_tokens(v):
    """
    This is a helper function.
    It checks if `v` is a list of tokens. 
    If so, we need to print differently.
    """
    if isinstance(v, List):
        if len(v) > 0:
            if isinstance(v[0], Token):
                return True
    return False

class Printer(Component):
    
    # 依赖的组建
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        return []

    # 组建别名
    defaults = {"alias": None}
    # 语言相关性
    language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """训练阶段代码"""
        print("************* printer 训练 ************* \n")

    def process(self, message: Message, **kwargs: Any) -> None:
        """组建运行过程中的处理代码"""
        print("************* printer 插件工作 ************* \n")
        if self.component_config['alias']:
            print(self.component_config['alias'])
        for k, v in message.data.items():
            if _is_list_tokens(v):
                print(f"{k}: {[t.text for t in v]}")
            else:
                print(f"{k}: {v.__repr__()}")
        print("************* printer 插件工作结束 ************* \n")

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """组建持久化的运行代码"""
        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """组建持加载的运行代码"""

        if cached_component:
            return cached_component
        else:
            return cls(meta)