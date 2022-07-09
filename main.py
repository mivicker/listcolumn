import re

def standardize_string(string: str) -> str:
    """
    Converts everything to lowercase, changes whitespace or '-' to '_',
    removes all other characters, removes duplicate underscores.

    Avoid providing this a multi-line string--it will collapse all the lines
    into one split by an underscore.
    """
    
    lowercase = string.lower().strip()
    underscored = re.sub(r'[\s-]+', '_', lowercase)
    alpha_and_under = re.sub(r'[^\w_]+', '', underscored)
    return re.sub(r'_+', '_', alpha_and_under).strip('_')
