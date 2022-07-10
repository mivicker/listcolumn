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
        print("printed in reduce")
        print(self.priorities)
        queue = self.priorities.get(key) 
        if queue is None:
            return True
        minimum = min([queue.index(scrap) for scrap in scraps])
        return queue[minimum]

    def collect_scraps(self, phrases: List[str]) -> Dict[str, list]:
        result = defaultdict(list)
        for phrase in phrases:
            bite, scrap = self.bite(phrase)
            result[bite].append(scrap)
        return result

    def category_parse(self, phrases: list) -> dict:
        print(self.collect_scraps(phrases))
        return {
            key: self.reduce(key, scraps)
            for key, scraps in self.collect_scraps(phrases).items()
        }


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
