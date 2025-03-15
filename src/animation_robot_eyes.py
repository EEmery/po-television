# RGB (read-green-blue) values for each high (H) and low (L) pixel in the animation. The color
# value can go from 0 to 255. Have in mind that those LEDs are very bright, so a low intensity
# should be enough to get a good effect from the display.
L = (0, 0, 0)
H = (10, 10, 10)

frames = [
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, H, H, L, L, H, H, L],
        [L, H, H, L, L, H, H, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, H, H, L, L],
        [H, H, L, L, H, H, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, H, H, L, L],
        [H, H, L, L, H, H, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, H, H, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, H, H, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, H, H, L, L],
        [H, H, L, L, H, H, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [H, H, L, L, H, H, L, L],
        [H, H, L, L, H, H, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, H, H, L, L, H, H, L],
        [L, H, H, L, L, H, H, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, H, H],
        [L, L, H, H, L, L, H, H],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, H, H],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, H, H],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, H, H],
        [L, L, H, H, L, L, H, H],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
    [
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
        [L, L, H, H, L, L, H, H],
        [L, L, H, H, L, L, H, H],
        [L, L, L, L, L, L, L, L],
        [L, L, L, L, L, L, L, L],
    ],
]


def robot_eyes(step_num, sound_level, prev_step_sound_avg, prev_step_sound_max, memory):
    """Iterates over all the frames in each new step, forming a moving eyes amimation. The animation
    can contain any number of frames, it doesn't have to have exactly 16 frames. This function can
    be copied without changes to build other simple animations that just iterates over hard coded
    frames.

    Args:
        Args:
        step_num (int): Equivalent step count in the pocket operator, goes from 0 to 15 (or
                        `MAX_STEPS`). This value won't be used in this animation function
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
    # If this is the first call of this animation function, memory will come as None
    if memory is None:
        # We initialize the parameters we will be using in this animation function
        num_frames = len(frames)  # Total number of frames that we'll iterate over
        frames_cursor = 0         # Cursor pointing to the current frame. Starts as the first frame
        # We'll use `memory` to save the current frame cursor to get the next frame in the next
        # function call. We'll also store the total number of frames so we don't have to re-compute
        # it on every function call
        memory = [frames_cursor, num_frames]

    # Restore previous informatino from memory
    frames_cursor, num_frames = memory
    frame = frames[frames_cursor]

    # Updates the frames cursor to point to the next frame
    frames_cursor = (frames_cursor + 1) % num_frames

    # Updates the memory to be used in the next function call
    memory = [frames_cursor, num_frames]

    # Returns the new frame and the updated memory
    return frame, memory
