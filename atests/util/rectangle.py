from robot.libraries.BuiltIn import BuiltIn


def get_element_center(xpath):
    """
    Return the center coordinates from an element's bounding rectangle.

    Args:
        xpath: XPath identifier of the element.

    Returns:
        tuple: Center x and y coordinates.
    """
    return _get_center_from_rectangle(BuiltIn().run_keyword("Get Rectangle Bounding From Element", xpath))


def _get_center_from_rectangle(rectangle):
    x = int(rectangle[0])
    y = int(rectangle[1])
    width = int(rectangle[2])
    height = int(rectangle[3])
    return x + width // 2, y + height // 2
