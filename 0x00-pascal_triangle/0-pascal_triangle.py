#!/usr/bin/python3
""" Pascal's Triangle Module """


def pascal_triangle(n):
    """
    Function to get list of Pascal's triangle rows & their values within

    Args:
        n (int): number of rows representing the Pascal's triangle height

    Returns:
        List[List]: integers representing the Pascal's triangle of height(n)
    """

    # Checking the value of the given height for the triangle
    if n <= 0:
        return []

    # Forming an empty list to add numbers to each row forming the triangle,
    # according to the height & how pascal triangle items should be calculated
    pascal_pyramid_list = []

    for _ in range(n):
        # Adding the first number at each row = "1"
        row = [1]

        # If n: height of the triangle > 0
        if pascal_pyramid_list:
            # Naming that the last item in each row to use it as reference
            last_item_in_row = pascal_pyramid_list[-1]

            # idx: 0 --> -1 in the row's length
            for idx in range(len(last_item_in_row) - 1):
                row.append(last_item_in_row[idx] + last_item_in_row[idx + 1])

            # Adding the last number at each row = "1"
            row.append(1)

        pascal_pyramid_list.append(row)

    return pascal_pyramid_list
