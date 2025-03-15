import machine as m


class PocketOperator():
    def __init__(self, sound_signal_pin, clock_signal_pin, max_steps, signal_threshold):
        """Create the initial data structures that represent the state of the pocket operator.

        Args:
            sound_signal_pin (int): Pin that reads the line-in music channel
            clock_signal_pin (int): Pin that reads the line-in PO-Sync channel
            max_steps (int): Maximum number of steps that the pocket operator has
            signal_threshold (int): Threshold used to detect a new clock pulse from the PO-Sync
                                    signal

        """
        self.sound_signal_adc = m.ADC(m.Pin(sound_signal_pin))
        self.clock_signal_adc = m.ADC(m.Pin(clock_signal_pin))

        self.max_steps = max_steps
        self.signal_threshold = signal_threshold

        self.sound_signal = 0
        self.clock_signal = 0
        self.step_num = 0

        self.reads_count = 0
        self.sound_signal_cumulative = 0
        self.prev_step_sound_avg = 0.0
        self.curr_step_sound_max = 0
        self.prev_step_sound_max = 0

        self.is_curr_clock_up = False
        self.is_prev_clock_up = False
        self.has_changed_step = False

    def read_gpios(self):
        """Read data from the GPIOs connected to the pocket operator, i.e., the line-in sound and
        clock (PO-Sync) signal. This method takes no extra arguments since it only updates the
        internal state of the PocketOperator instance.

        Returns:
            PocketOperator: Returns the pocket operator instance to be able to chain other methods
                            in the main loop.

        """
        self.sound_signal = self.sound_signal_adc.read_u16()
        self.clock_signal = self.clock_signal_adc.read_u16()

        return self

    def update_step(self):
        """When it detects a up or down change in the clock signal, update the internal state of
        the pocket operator instance to have the `has_changed_step` flag set to `True`. If no clock
        change was detected, it keeps the flag set to `False`. This method takes no extra arguments
        since it only updates the internal state of the PocketOperator instance.

        Returns:
            PocketOperator: Returns the pocket operator instance to be able to chain other methods
                            in the main loop.

        """
        self.has_changed_step = False
        self.is_curr_clock_up = self.clock_signal > self.signal_threshold

        if (self.is_prev_clock_up ^ self.is_curr_clock_up):
            self.has_changed_step = True
            self.is_prev_clock_up = self.is_curr_clock_up
            self.step_num = (self.step_num + 1) % self.max_steps

        return self

    def update_cumulative_values(self):
        """Update all the cumulative values for the pocket operator instance, for example, the
        maximum sound signal detected (`curr_step_sound_max`) and the total cumulative signal in
        the step so far (`sound_signal_cumulative`). When a step change is detected, those values
        are used to update `prev_step_sound_max` and `prev_step_sound_avg`, that can be used by the
        animation funciton to draw complex frames given the previous step maximum and average sound
        signal deteceted, respectively. This method takes no extra arguments since it only updates
        the internal state of the PocketOperator instance.

        Returns:
            PocketOperator: Returns the pocket operator instance to be able to chain other methods
                            in the main loop.

        """
        self.reads_count += 1
        self.sound_signal_cumulative += self.sound_signal / self.signal_threshold

        if self.sound_signal > self.curr_step_sound_max:
            self.curr_step_sound_max = self.sound_signal

        if self.has_changed_step:
            self.prev_step_sound_avg = (
                0 if self.reads_count == 0 else self.sound_signal_cumulative / self.reads_count
            )
            self.prev_step_sound_max = self.curr_step_sound_max

            self.reads_count = 0
            self.sound_signal_cumulative = 0
            self.curr_step_sound_max = 0

        return self
