# OBS Replay Notify Script

This script is designed for use with OBS Studio to enhance user interaction by providing immediate feedback when the replay buffer is saved. Users can choose between receiving a Windows notification or hearing a sound alert.

## Features

- **Notification Alert**: Displays a Windows notification when the OBS replay buffer is saved.
- **Sound Alert**: Plays a sound file located in the same directory as the script when the replay buffer is saved.

## Requirements

- OBS Studio
- Python scripting support in OBS
- `plyer` library for notifications

## Setup

1. Ensure Python scripting is enabled in your OBS Studio installation.
2. Install the `plyer` library using pip:

   pip install plyer

3. Place the `obs-notify.py` script along with `obs-notify.wav` in your OBS Studio scripts directory.

## Configuration

- **Show Notification**: A boolean setting in the script properties to toggle between playing a sound or showing a notification.

## Usage

Once the script is loaded in OBS Studio, it will automatically listen for the event when the replay buffer is saved. Depending on the user's settings, it will either play a sound or show a notification.

## Support

For support, ensure that you have the latest version of OBS Studio and that your Python environment is correctly set up to run scripts. If you encounter any issues, reviewing the OBS logs may provide additional information.

## License

This script is provided as open-source under the MIT license. Feel free to modify and distribute as needed.
