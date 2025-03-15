# RGB (read-green-blue) values for each high (H) and low (L) pixel in the animation. The color
# value can go from 0 to 255. Have in mind that those LEDs are very bright, so a low intensity
# should be enough to get a good effect from the display.
L = (0, 0, 0)
H = (10, 10, 10)

robot_arm_frames = [
    # 1 - 4
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, L, L, L, L],
        [H, H, H, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, L, H, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, L, L, L, L],
        [H, H, H, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, L, H, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, H, H, L, L, L, L, L],
        [L, H, H, L, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, L, H, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],

    # 5 - 8
    [
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, H, H, L, L, L],
        [L, L, L, H, H, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, H, H, L, L],
        [L, L, L, L, H, H, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, H, H, L],
        [L, L, L, L, L, H, H, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, H, L, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
    ],

    # 9 - 12
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, H, H],
        [L, L, L, L, H, H, H, H],
        [L, L, L, H, L, L, L, L],
        [L, L, H, L, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, H, H],
        [L, L, L, L, H, H, H, H],
        [L, L, L, H, L, L, L, L],
        [L, L, H, L, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, H, H, L],
        [L, L, L, L, L, H, H, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, H, L, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, H, H, L, L],
        [L, L, L, L, H, H, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
    ],

    # 13 - 16
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, H, H, L, L, L],
        [L, L, L, H, H, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, H, H, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, H, H, L, L, L, L, L],
        [L, H, H, L, L, L, L, L],
        [L, L, L, H, L, L, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, L, L, H, L, L],
        [L, L, L, L, H, L, L, L],
        [L, L, L, H, L, L, L, L],
    ],
]


def robot_arm(step_num, sound_level, prev_step_sound_avg, prev_step_sound_max, memory):
    """Iterates over all the frames in each new step, forming a robotic arm amimation. The animation
    expects exactly 16 frames, to match with the number of steps in the pocket operator.

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
                                   line-in sound channel in the pocket operator. This value won't be
                                   used in this animation function

    Returns:
        frame (Frame): A 2D list of Tuples containing the pixel RGB values forming the new frame to
                       be drawn, in other words, a `List[List[Tuple[int, int, int]]]`) in the shape
                       of (row, column, red-value, green-value, blue-value)
        memory (Any): Any data structure that should be passed to the next call of the animation
                      function. On the first animation function call, it comes as None. This is an
                      optional feature to be used if necessary, it can be left as None if not used
    """
    # We simply iterate over the frames according to the current step number, since we expect
    # exaclty 16 frames in the animation
    frame = robot_arm_frames[step_num-1]

    # Returns the new frame and the unused memory (it's value will remaing being None)
    return frame, memory
