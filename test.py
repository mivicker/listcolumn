from src.main import standardize_string, PriorityHandler


def test_standardize_string():
    assert standardize_string("APP LE S (3 0 -- 30)") == "app_le_s_3_0_30"
    assert (
        standardize_string("nO thrill for GEORGE will_") == "no_thrill_for_george_will"
    )
    assert standardize_string("A Category - with a value") == "a_category_with_a_value"


def test_bite_no_priority():
    handler = PriorityHandler()
    assert handler.bite("apples") == ("apples", True)


def test_bite_with_priority():
    handler = PriorityHandler({"bite_":["me"]})
    assert handler.bite("bite_me") == ("bite_", "me")


def test_collect_scraps():
    handler = PriorityHandler({"one": ["boy"]})
    assert handler.collect_scraps(["oneboy", "two", "three"]) == {
        "one": ["boy"],
        "two": [True],
        "three": [True],
    }


def test_category_parse():
    handler = PriorityHandler()
    data = "one,two,three,four"
    expected = {
        "one": True,
        "two": True,
        "three": True,
        "four": True,
    }

    assert handler.category_parse(data.split(",")) == expected


def test_category_parse_full():
    # What does this interface look like?
    # Provide a dictionary of str to list with the categories ordered by the
    # 'valence' of each item.

    priorities = {
        "acceptable_breakfasts_": [
            "french_toast",
            "pancakes",
            "oatmeal",
            "cereal",
        ],
        "enjoyable_dinners_": [
            "salmon",
            "tacos",
            "thai_basil_eggplant",
        ],
    }

    dataset_one = "acceptable_breakfasts_french_toast,acceptable_breakfasts_oatmeal,hotel_pool_please"
    handler = PriorityHandler(priorities, reject=["hotel_pool_please"])
    assert handler.category_parse(dataset_one.split(",")) == {"acceptable_breakfasts_": "french_toast"}

    # What happens if an item starts with the category tag, but is not in
    # the valence list? Pass it through if nothing else in the list is present.

    # What if there are two values not in the valence list with a valid category
    # tag? Warn, then pass along first in alphabetical order. Carefull pre-analysis
    # should avoid this.


if __name__ == "__main__":
    test_standardize_string()
    test_bite_no_priority()
    test_collect_scraps()
    test_bite_with_priority()
    test_category_parse()
    test_category_parse_full()
