# BoomRoom
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<table>
  <tr>
    <td align="center">
      <img src="/media/Bunker_200x200.png" alt="Bunker Logo" width="320px"/>
    </td>
    <td align="center">
      <img src="/media/first-full-screen-shot.jpg" alt="First Full Screen Shot" width="320px"/>
    </td>
  </tr>
</table>

BoomRoom is a pilot Raspi program to help Hack Green 'script' the events in their 'Nuclear Attack experience room'. The intention is that the software can fire off either a test script, or a run (ie, normal-operation) script. The scripts are really just a list of times (in ms) and a function to call. The times are given in elapsed ms, so a time of 1250 would indicate 1250 ms after the start of the script, (1.25 seconds).  

[Hack Green Secret Nuclear Bunker](https://www.hackgreen.co.uk/)  


## Features

*   **Interactive Controls:** Use physical buttons (e.g., arcade buttons, push buttons) connected to your Raspberry Pi's GPIO pins.
*   **Visual Feedback:** Integrate LEDs or other light indicators to respond to user input or project state.
*   **Audio Playback:** Leverages Pygame for playing sound effects or music based on interactions.
*   **Modular Design:** Easily extendable to add more buttons, lights, or sound features.

## Hardware Requirements

To get BoomRoom up and running, you'll need the following physical components:

*   **Raspberry Pi:** 
    *   `[Specify model, e.g., Raspberry Pi 3 Model B+, Raspberry Pi 4, etc.]`
    *   `[Any specific version of Raspberry Pi OS, e.g., Bullseye, Bookworm]`
*   **Breadboard:** 
    *   `[Optional, but useful for prototyping]`
*   **Jumper Wires:** 
    *   `[Male-to-female, male-to-male depending on your components]`
*   **Push Buttons:** 
    *   `[Number of buttons, e.g., 4 x Momentary Push Buttons]`
    *   `[Any specific type, e.g., Arcade Buttons]`
*   **LEDs:** 
    *   `[Number of LEDs, e.g., 4 x 5mm LEDs (Assorted Colors)]`
*   **Resistors:** 
    *   `[Value for LEDs, e.g., 4 x 220 Ohm Resistors for LEDs]`
    *   `[Value for Pull-down/Pull-up resistors for buttons, if used externally, e.g., 4 x 10k Ohm Resistors]`
*   **Power Supply:** Appropriate power supply for your Raspberry Pi.

## Software Requirements

BoomRoom runs on Python and requires a few libraries.

*   **Python 3:** 
    *   `[Specify minimum version if relevant, e.g., Python 3.7+]`
*   **Pygame:** For handling graphics, sound, and input events.
*   **RPi.GPIO:** For interfacing with the Raspberry Pi's GPIO pins.
*   `[Any other Python libraries you might be using]`

## Wiring Diagram / Hardware Setup

This is a critical section for hardware projects! Describe or preferably show how to connect everything.

### Basic Connections (Example)

Here's an example of how you might connect a button and an LED. **Please adapt this to your actual circuit.**

*   **Button 1:** Connect one leg to `GPIO [X]` and the other leg to `Ground (GND)`. (Use internal pull-up/pull-down or add an external resistor).
*   **LED 1:** Connect the anode (longer leg) to `GPIO [Y]` (via a `[220 Ohm]` resistor) and the cathode (shorter leg) to `Ground (GND)`.

It's highly recommended to include a diagram here. You can create one using tools like Fritzing, diagrams.net, or even a hand-drawn picture if it's clear!

## Installation

Follow these steps to get BoomRoom installed and running on your Raspberry Pi:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/robsoft/BoomRoom.git
    cd BoomRoom
    ```

2.  **Install Python Dependencies:**
    It's good practice to use a virtual environment.

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install pygame RPi.GPIO # Add any other specific libraries here
    ```

    *If you don't want to use a virtual environment (though recommended for clean setups):*
    ```bash
    pip install pygame RPi.GPIO # Or pip3 if your system defaults to Python 2
    ```

3.  **Enable GPIO Access:**
    Ensure your user has the necessary permissions to access GPIO. This is usually handled by default for the `pi` user, but if you're using a different user or encountering issues, you might need to add them to the `gpio` group:
    ```bash
    sudo adduser <your_username> gpio
    # You might need to log out and back in for changes to take effect
    ```

## Usage

Once installed and wired correctly, you can run the BoomRoom application:

1.  **Navigate to the project directory:**
    ```bash
    cd BoomRoom
    ```
2.  **Activate your virtual environment (if used):**
    ```bash
    source venv/bin/activate
    ```
3.  **Run the application:**
    ```bash
    python3 main.py # Or whatever your primary entry point script is
    ```

    *   **Describe interaction:** Explain what happens when buttons are pressed, what the LEDs indicate, and any other user interactions.
        *   "Press `Button 1` to play the `[sound_name.wav]` sound."
        *   "LED `[X]` will light up when `[action]` occurs."
        *   "The program exits when `[how to exit, e.g., a specific button combo or Ctrl+C]` is pressed."

## Configuration (Optional)

If your project has configurable parameters (e.g., GPIO pin numbers, sound file paths), explain how to modify them.

*   "GPIO pin assignments are defined in `config.py` (or directly in `main.py`)."
*   "Sound files are located in the `assets/sounds/` directory."

## Troubleshooting

*   **`RPi.GPIO` permissions error:** Check if your user is in the `gpio` group.
*   **No sound:** Ensure audio is working on your Pi. Check `alsamixer` and speaker connections.
*   **Buttons not responding:** Double-check your wiring against the diagram and verify GPIO pin numbers in your code. Ensure pull-up/pull-down resistors are correctly configured (either internal or external).

## Contributing (Optional)

If you're open to contributions, you can add a section here explaining how others can contribute (e.g., report bugs, suggest features, submit pull requests).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements (Optional)

*   `[Mention any tutorials, libraries, or individuals that were particularly helpful]`
*   `[Credit sources for assets if applicable]`

---



# BoomRoom
Hack Green Secret Nuclear Bunker developments

Todo:  
- [ ] Disable mouse pointer  
- [ ] Autostart the program  
- [ ] Fix problem with the 'test' audio file ('run' one is fine)  
- [ ] Figure out how to get 'run' script to handle the trigger switch  
- [ ] Figure out how to get 'run' script to autorepeat (a setting in the script file?)  
- [ ] Indicate the GPIO pins in some way at the bottom of the screen (the pin set/unset function to include something?)  




The GPIO is available so that relays, lights, motors etc are all within reach, and the initial brief was to be able to play a 5.1 type sound file which might last for a couple of minutes. We are using a resistive-type touch screen of 480x320, on which we draw 2 buttons. The screen effectively disables the onboard HDMI, so our Raspi is configured for SSH over the network too.

We have used PyGame to do most of the heavy lifting around image loading, sound playing, drawing on the screen surface and event handling.    

Our longer-term intention is to make this more robust and flexible, and encourage other smaller museums and installations to use and help extend the programs. 

<img src="/media/boomroom-default.png" width="240px"/><img src="/media/boomroom-test.png" width="240px"/><img src="/media/boomroom-run.png" width="240px"/>  



http://www.lcdwiki.com/3.5inch_RPi_Display 

  
