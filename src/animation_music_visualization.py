import math

# RGB (read-green-blue) values for each high (H) and low (L) pixel in the animation. The color
# value can go from 0 to 255. Have in mind that those LEDs are very bright, so a low intensity
# should be enough to get a good effect from the display.
L = (0, 0, 0)
H = (10, 10, 10)

empty_frame = [
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
    [L, L, L, L, L, L, L, L],
]


def get_rows_to_draw(step_num, prev_step_sound_max, all_prev_step_sound_max):
    """Auxiliary function that computes how many LEDs to turn on given all the previous steps
    maximum sound signal.

    Args:
        step_num (int): Equivalent step count in the pocket operator, goes from 0 to 15 (or
                        `MAX_STEPS`)
        prev_step_sound_max (int): The previous step maximum value of the GPIO pin connected to the
                                   line-in sound channel in the pocket operator.
        all_prev_step_sound_max (int): All the previous `prev_step_sound_max` values for the last 8
                                       steps.

    Returns:
        int: The number of rows to draw. Can go from 0 to 8.
    """
    max_all_prev_step_sound_max = max(all_prev_step_sound_max)

    if max_all_prev_step_sound_max == 0:
        perc_of_max = prev_step_sound_max
    else:
        perc_of_max = prev_step_sound_max / max_all_prev_step_sound_max

    max_rows_to_draw = 8
    num_rows_to_draw = math.ceil(max_rows_to_draw * perc_of_max)

    return num_rows_to_draw


def music_visualization(step_num, sound_level, prev_step_sound_avg, prev_step_sound_max, memory):
    """Draws a column of light representing the previous step's sound signal percentage of the
    maximum sound signal of the last 8 steps. As it draws the column of light, it erases (turns the
    LEDs off) for the following column to create an effect of a cursor moving.

    Args:
        step_num (int): Equivalent step count in the pocket operator, goes from 0 to 15 (or
                        `MAX_STEPS`)
        sound_level (int): Most recent read from the GPIO pin connected to the line-in sound channel
                           in the pocket operator. This value won't be used in this animation
                           function
        prev_step_sound_avg (float): The previous step average value of the GPIO pin connected to
                                     the line-in sound channel in the pocket operator. This value
                                     won't be used in this animation function
        prev_step_sound_max (int): The previous step maximum value of the GPIO pin connected to the
                                   line-in sound channel in the pocket operator.

    Returns:
        frame (Frame): A 2D list of Tuples containing the pixel RGB values forming the new frame to
                       be drawn, in other words, a `List[List[Tuple[int, int, int]]]`) in the shape
                       of (row, column, red-value, green-value, blue-value)
        memory (Any): Any data structure that should be passed to the next call of the animation
                      function. On the first animation function call, it comes as None. This is an
                      optional feature to be used if necessary, it can be left as None if not used
    """
    max_steps = 8  # Indicates how many columns we'll use to represent the steps

    # If this is the first call of this animation function, memory will come as None
    if memory is None:
        # We initialize an array that will hold all the previous values for `prev_step_sound_max`.
        # This will be used to compute the percentage of the last value for `prev_step_sound_max`,
        # given all the 8 previous prev_step_sound_max
        all_prev_step_sound_max = [0 for i in range(max_steps)]
        # Start the memomry with an empty frame and a placeholder list for all `prev_step_sound_max`
        memory = empty_frame, all_prev_step_sound_max

    # Restores the memory from the previous call
    frame, all_prev_step_sound_max = memory

    # Sets the column to draw based on the current `step_num``
    col_to_draw = step_num % max_steps
    # Sets the column to erase as the next column after `col_to_draw`
    col_to_erase = (step_num + 1) % max_steps
    # Add the most recent prev_step_sound_max to the list with the previous ones
    all_prev_step_sound_max[col_to_draw] = prev_step_sound_max

    # Computes how many LEDs to turn on for this step
    rows_to_draw = get_rows_to_draw(step_num, prev_step_sound_max, all_prev_step_sound_max)

    # Updates the current frame to draw the new column and erase the next one
    for i, row in enumerate(frame):
        for j, pixel_value in enumerate(row):

            # We set the LED value to high if it is in a column that we want to draw and the row
            # is under the intensity that we want to represent
            if i <= rows_to_draw and j == col_to_draw:
                frame[i][j] = H

            # We set the LED value to low if it is in a column that we want to draw and the row
            # is over the intensity that we want to represent
            if i > rows_to_draw and j == col_to_draw:
                frame[i][j] = L

            # We set the LED value to low if it is in a column that we want to erase to represent
            # a cursor moving
            if j == col_to_erase:
                frame[i][j] = L

    # Update the memory with the latest frame and `all_prev_step_sound_max`
    memory = frame, all_prev_step_sound_max

    # Return the value to the animation function caller
    return frame, memory
