def get_center_coords(surface_size, window_size):
    """
    Calculate the coordinates to center a surface in a window.

    Args:
    - surface_size (tuple): (width, height) of the surface to center.
    - window_size (tuple): (width, height) of the window.

    Returns:
    - tuple: (x, y) coordinates to place the surface in the center of the window.
    """
    surface_width, surface_height = surface_size
    window_width, window_height = window_size

    # Calculate the center position
    center_x = (window_width - surface_width) // 2
    center_y = (window_height - surface_height) // 2

    return center_x, center_y
