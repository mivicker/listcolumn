from typing import List, Dict, Union, Tuple
from dataclasses import dataclass, field
import re
from collections import defaultdict


@dataclass
class PriorityHandler:
    priorities: Dict[str, list] = field(default_factory=dict)
    reject: List[str] = field(default_factory=list)

    def bite(self, string) -> Union[Tuple[str, str], Tuple[str, bool]]:
        """
        If the string starts with a key in the priorities dictioanry,
        this bites that substring and returns the bite and the scrap.

        Else it returns the string and True
        """
        for key in self.priorities:
            if string.startswith(key):
                return key, string[len(key) :]
        return string, True

    def reduce(self, key: str, scraps: List[Union[str, Tuple]]) -> Union[str, Tuple]:
        queue = self.priorities.get(key) 
        if queue is None:
            return True
        try:
            minimum = min([queue.index(scrap) for scrap in scraps])
            return queue[minimum]
        except ValueError:
            priorities = [queue.index(scrap) for scrap in scraps if scrap in queue]
            if not priorities:
                return ""
            return queue[minimum]

    def collect_scraps(self, phrases: List[str]) -> Dict[str, list]:
        result = defaultdict(list)
        for phrase in phrases:
            bite, scrap = self.bite(phrase)
            result[bite].append(scrap)
        return result

    def category_parse(self, phrases: list) -> dict:
        return {
            key: self.reduce(key, scraps)
            for key, scraps in self.collect_scraps(phrases).items()
            if key not in self.reject
        }


def split_and_normalize(row: str) -> List[str]:
    return [standardize_string(string) for string in row.split(",")]


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
