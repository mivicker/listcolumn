from main import standardize_string


def test_standardize_string():
    assert standardize_string("APP LE S (3 0 -- 30)") == "app_le_s_3_0_30"
    assert (
        standardize_string("nO thrill for GEORGE will_") == "no_thrill_for_george_will"
    )
    assert standardize_string("A Category - with a value") == "a_category_with_a_value"

def test_category_parse_simple():
    data = [
        "one,two,three,four",
        "one,three,four",
        "five",
        "three,two,one",
    ]

def test_category_parse():
    # What does this interface look like?
    # Provide a dictionary of str to list with the categories ordered by the
    # 'valence' of each item. 

    categories = {
        'acceptable_breakfasts_': [
            'french_toast',
            'pancakes',
            'oatmeal',
            'cereal',
        ],
        'enjoyable_dinners_': [
            'salmon',
            'tacos',
            'thai_basil_eggplant',
        ]
    }

    dataset_one = [""]
    dataset_two = [""]

    # What happens if an item starts with the category tag, but is not in
    # the valence list? Pass it through if nothing else in the list is present.

    # What if there are two values not in the valence list with a valid category
    # tag? Warn, then pass along first in alphabetical order. Carefull pre-analysis 
    # should avoid this.


if __name__ == "__main__":
    test_standardize_string()
