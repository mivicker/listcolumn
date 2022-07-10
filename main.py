from typing import List, Dict, Union, Tuple
from dataclasses import dataclass, field
import re
from collections import defaultdict


@dataclass
class PrioritiesHandler:
    priorities: Dict[str, list] = field(default_factory=dict)

    def bite(self, string) -> Union[Tuple[str, str], Tuple[str, bool]]:
        for key in self.priorities:
            if string.startswith(key):
                return key, string[len(key) :]
        return string, True

    def reduce(self, key: str, scraps: List[Union[str, Tuple]]) -> Union[str, Tuple]:
        if queue := self.priorities.get(key) is None:
            return True
        minimum = min([queue.index(scrap) for scrap in scraps])
        return queue[minimum]


def collect_scraps(phrases: List[str], handler: PrioritiesHandler) -> Dict[str, list]:
    result = defaultdict(list)
    for phrase in phrases:
        bite, scrap = handler.bite(phrase)
        result[bite].append(scrap)
    return result


def category_parse(phrases: list, handler: PrioritiesHandler = None) -> dict:
    if handler is None:
        handler = PrioritiesHandler()

    result = defaultdict(list)
    for phrase in phrases:
        bite, scrap = handler.bite(phrase)
        result[bite].append(scrap)

    return {key: handler.reduce(key, value) for key, value in result.items()}


def standardize_string(string: str) -> str:
    """
    Converts everything to lowercase, changes whitespace or '-' to '_',
    removes all other characters, removes duplicate underscores.

    Avoid providing this a multi-line string--it will collapse all the lines
    into one split by an underscore.
    """

    lowercase = string.lower().strip()
    underscored = re.sub(r"[\s-]+", "_", lowercase)
    alpha_and_under = re.sub(r"[^\w_]+", "", underscored)
    return re.sub(r"_+", "_", alpha_and_under).strip("_")
