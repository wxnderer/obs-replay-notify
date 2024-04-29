# OBS Replay Notify Script

This Python script for OBS Studio allows you to play a sound or show a notification when the replay buffer is saved. It provides options to use a custom audio file or the default `obs-notify.wav` file, and to choose between playing a sound or showing a Windows notification.

## Features

- **Notification Alert**: Displays a Windows notification when the OBS replay buffer is saved.
- **Sound Alert**: Plays a sound file located in the same directory as the script when the replay buffer is saved.

## Requirements

- OBS Studio
- Python scripting support in OBS
- `plyer` library for notifications

## Setup

1. Ensure Python scripting is enabled in your OBS Studio installation.

2. Install the required Python packages:

   - `obspython` (should be installed with OBS Studio)
   - `plyer` (for showing notifications)

   You can install `plyer` using pip:

   `pip install plyer`

3. Copy the `obs-notify.py` script to your OBS Studio scripts directory. On Windows, this is typically located at:
   `%APPDATA%\obs-studio\scripts`
4. In OBS Studio, go to `Tools` > `Scripts` and load the `obs-notify.py` script

## Configuration

After loading the script, you can configure it through the script properties:

1. Go to `Tools` > `Scripts` in OBS Studio.
2. Select the `obs-notify.py` script and click the `Properties` button.
3. In the script properties window, you'll see the following options:

- **Play windows notification instead of sound**: Check this option to show a Windows notification instead of playing a sound when the replay buffer is saved.
- **Use custom audio file**: Check this option to use a custom audio file instead of the default `obs-notify.wav` file.
- **WAV Audio File Path**: If you checked the "Use custom audio file" option, you can specify the path to your custom WAV audio file here.

## Usage

Once the script is loaded in OBS Studio, it will automatically listen for the event when the replay buffer is saved. Depending on the user's settings, it will either play a sound or show a notification.

## Notes

- The script uses the `obspython` module to interact with OBS Studio and the `plyer` module to show Windows notifications.
- The `play_sound` function uses the `ctypes` module to play the specified WAV file asynchronously.
- The `script_properties` function defines the script's configuration options, which are displayed in the OBS Studio script properties window.
- The `script_load` function sets up the script and registers the `event_callback` function to be called when the replay buffer is saved.
- The `event_callback` function is called when the replay buffer is saved, and it handles playing the sound or showing the notification based on the configured settings.

## Support

For support, ensure that you have the latest version of OBS Studio and that your Python environment is correctly set up to run scripts. If you encounter any issues, reviewing the OBS logs may provide additional information.

## License

This script is provided as open-source under the MIT license. Feel free to modify and distribute as needed.
