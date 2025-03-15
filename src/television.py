import machine as m
from neopixel import NeoPixel


class Television():
    def __init__(
            self,
            display_pin,
            display_button_pin,
            display_width,
            display_height,
            display_freq,
            animations):
        """Create the initial data structures that represent the state of the pocket operator
        television.

        Args:
            display_pin (int): Pin that connects to the display data-in cable
            display_button_pin (int): Pin that reads the signal from the animation button switch
            display_width (int): Width of the LED matrix display used
            display_height (int): Height of the LED matrix display used
            display_freq (int): Some displays can communicate at 800 KHZ, others at 400 KHZ
            animations (List[AnimaitonFunc]): A list with all the available animations that the
                                              pocket operator television should iterate over

        """
        self.available_timings = {
            400: 0,
            800: 1,
        }

        self.display_pin = m.Pin(display_pin, m.Pin.OUT)
        self.display_button_pin = m.Pin(display_button_pin, m.Pin.IN)
        self.display_width = display_width
        self.display_height = display_height
        self.display_freq = display_freq

        self.display = NeoPixel(
            self.display_pin,
            self.display_width * self.display_height,
            timing=self.available_timings[self.display_freq]
        )

        self.is_curr_button_pressed = 0
        self.is_prev_button_pressed = 0

        self.animations = animations
        self.animation_cursor = 0
        self.animation_func = self.animations[self.animation_cursor]
        self.memory = None

    def read_animation_change_button(self):
        """Read data from the GPIOs connected to the animation change button in the pocket operator
        television and, if it gets pressed, changes the state of the television to reflect that, for
        example, changing the animation function pointer to the next animation, reseting the memory
        to be used by the new animation function, etc. This method takes no extra arguments since it
        only updates the internal state of the Television instance.

        Returns:
            Television: Returns the pocket operator television instance to be able to chain other
                        methods in the main loop.

        """
        self.is_curr_button_pressed = self.display_button_pin.value()

        # Detects animation change request on button press
        if not self.is_prev_button_pressed and self.is_curr_button_pressed:
            # Increase the animation cursor without going beyond the maximum number of animation
            # frames
            self.animation_cursor = (self.animation_cursor + 1) % len(self.animations)
            self.animation_func = self.animations[self.animation_cursor]
            self.memory = None

        self.is_prev_button_pressed = self.is_curr_button_pressed

        return self

    def _get_linear_position(self, i, j, max_width):
        """Auxiliary method that converts a 2D matrix, representing the frame to be drawn, into 1D
        to be fed to the LED matrix display. The 2D-to-1D conversion takes into account the order
        of the pixel indexes in the display used:
        | 07 < 06 < 05 < 04 < 03 < 02 < 01 < 00 |
        | 08 > 09 > 10 > 11 > 12 > 13 > 14 > 15 |
        | 23 < 22 < 21 < 20 < 19 < 18 < 17 < 16 |
        | 24 > 25 > 26 > 27 > 28 > 29 > 30 > 31 |
        | ...                     |
        | 56 > 57 > 58 > 59 > 60 > 61 > 62 > 63 |

        Args:
            i (int): Row index from the 2D frame. It can go from 0 to the display height.
            j (int): Column index from the 2D frame. It can go from 0 to the display width
                     (`max_width`).
            max_width (int): Maximum width of the LED matrix display. This is used to compute the
                             linear (1D) index of a pixel in rows were the order is right-to-left.

        Returns:
            int: The linear (1D) index of the pixel to be used to update the LED metrix display.

        """
        if i % 2 == 1:
            return max_width * i + j
        else:
            return max_width * i + (max_width - j - 1)

    def draw_new_frame(self, step_num, sound_level, prev_step_sound_avg, prev_step_sound_max):
        """Ingest the most recent state of the pocket operator, get a new frame from the animation
        function, and update the LED matrix display with it.

        Args:
            step_num (int): Equivalent step count in the pocket operator, goes from 0 to 15 (or
                            `MAX_STEPS`)
            sound_level (int): Most recent read from the GPIO pin connected to the line-in sound
                               channel in the pocket operator
            prev_step_sound_avg (float): The previous step average value of the GPIO pin connected
                                         to the line-in sound channel in the pocket operator.
            prev_step_sound_max (int): The previous step maximum value of the GPIO pin connected to
                                       the line-in sound channel in the pocket operator.

        Returns:
            Television: Returns the pocket operator television instance to be able to chain other
                        methods in the main loop.

        """

        new_frame, self.memory = self.animation_func(
            step_num,
            sound_level,
            prev_step_sound_avg,
            prev_step_sound_max,
            self.memory)

        for i, row in enumerate(new_frame):
            for j, new_pixel_value in enumerate(row):
                linear_position = self._get_linear_position(i, j, self.display_width)
                cur_pixel_value = self.display[linear_position]

                if new_pixel_value != cur_pixel_value:
                    self.display[linear_position] = new_pixel_value

        self.display.write()

        return self
