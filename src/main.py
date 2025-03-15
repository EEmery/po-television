from pocket_operator import PocketOperator
from television import Television
from animation_robot_arm import robot_arm
from animation_robot_eyes import robot_eyes
from animation_wave import wave
from animation_music_visualization import music_visualization

# A list with all the available animations that the pocket operator television should iterate over
ANIMATIONS = [
    robot_arm,
    robot_eyes,
    wave,
    music_visualization,
]

SOUND_SIGNAL_PIN = 26    # Pin that reads the line-in music channel
CLOCK_SIGNAL_PIN = 27    # Pin that reads the line-in PO-Sync channel
MAX_STEPS = 16           # Maximum number of steps that the pocket operator has
SIGNAL_THRESHOLD = 2000  # Threshold used to detect a new clock pulse from the PO-Sync signal

DISPLAY_WIDTH = 8        # Width of the LED matrix display used
DISPLAY_HEIGHT = 8       # Height of the LED matrix display used
DISPLAY_KHZ = 400        # Some displays can communicate at 800 KHZ, others at 400 KHZ
DISPLAY_PIN = 0          # Pin that connects to the display data-in cable
DISPLAY_BUTTON_PIN = 21  # Pin that reads the signal from the animation button switch

# Initialize a representation of the pocket operator with the right parameters
po = PocketOperator(
    SOUND_SIGNAL_PIN,
    CLOCK_SIGNAL_PIN,
    MAX_STEPS,
    SIGNAL_THRESHOLD,
)

# Initialize a representation of the pocket operator television with the right parameters
tv = Television(
    DISPLAY_PIN,
    DISPLAY_BUTTON_PIN,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    DISPLAY_KHZ,
    ANIMATIONS,
)

while True:
    # Reads data from the pocket operator
    (
        po.read_gpios()
        .update_step()
        .update_cumulative_values()
    )

    if po.has_changed_step:
        # Updates the display once we detect a change in step
        (
            tv.read_animation_change_button()
            .draw_new_frame(
                po.step_num,
                po.sound_signal,
                po.prev_step_sound_avg,
                po.prev_step_sound_max
            )
        )
