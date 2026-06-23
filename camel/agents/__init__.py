# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
import importlib
import sys

# Lazily import potentially circular submodules at attribute access time to avoid
# circular imports during package initialization.
from typing import TYPE_CHECKING

from .base import BaseAgent
from .tool_agents.base import BaseToolAgent

_lazy_imports = {
    "ChatAgent": ".chat_agent",
    "CriticAgent": ".critic_agent",
    "EmbodiedAgent": ".embodied_agent",
    "KnowledgeGraphAgent": ".knowledge_graph_agent",
    "MCPAgent": ".mcp_agent",
    "RepoAgent": ".repo_agent",
    "RoleAssignmentAgent": ".role_assignment_agent",
    "SearchAgent": ".search_agent",
    "TaskCreationAgent": ".task_agent",
    "TaskPlannerAgent": ".task_agent",
    "TaskPrioritizationAgent": ".task_agent",
    "TaskSpecifyAgent": ".task_agent",
    "HuggingFaceToolAgent": ".tool_agents.hugging_face_tool_agent",
}

# Provide imports for type checkers without causing runtime imports
if TYPE_CHECKING:
    from .chat_agent import ChatAgent
    from .critic_agent import CriticAgent
    from .embodied_agent import EmbodiedAgent
    from .knowledge_graph_agent import KnowledgeGraphAgent
    from .mcp_agent import MCPAgent
    from .repo_agent import RepoAgent
    from .role_assignment_agent import RoleAssignmentAgent
    from .search_agent import SearchAgent
    from .task_agent import (
        TaskCreationAgent,
        TaskPlannerAgent,
        TaskPrioritizationAgent,
        TaskSpecifyAgent,
    )
    from .tool_agents.hugging_face_tool_agent import (
        HuggingFaceToolAgent,
    )


def __getattr__(name: str):
    """Lazily import attributes from submodules when accessed."""
    if name in _lazy_imports:
        module = importlib.import_module(_lazy_imports[name], __name__)
        value = getattr(module, name)
        # Cache on the module for subsequent accesses
        setattr(sys.modules[__name__], name, value)
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    # Include lazily importable names in dir()
    return sorted(list(globals().keys()) + list(_lazy_imports.keys()))


__all__ = [
    'BaseAgent',
    'ChatAgent',
    'TaskSpecifyAgent',
    'TaskPlannerAgent',
    'TaskCreationAgent',
    'TaskPrioritizationAgent',
    'CriticAgent',
    'BaseToolAgent',
    'HuggingFaceToolAgent',
    'EmbodiedAgent',
    'RoleAssignmentAgent',
    'SearchAgent',
    'KnowledgeGraphAgent',
    'MCPAgent',
    'RepoAgent',
]
