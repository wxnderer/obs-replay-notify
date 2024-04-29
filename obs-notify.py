"""
Provides a script for OBS Studio that plays a sound or shows a Windows notification when the replay buffer is saved.

The script adds an event callback to the OBS frontend that listens for the OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED event. When this event is triggered, the script checks a setting to determine whether to play a sound or show a notification. The sound file is located in the same directory as the script, and the notification is displayed using the plyer library.

The script also provides functions to load and unload the script, as well as to get the script properties.
"""
import obspython as obs
import os, ctypes, sys
from plyer import notification
def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_bool(props,"show_notification", "Play windows notification instead of sound")
    
    return props

def script_load(settings):
    obs.script_log(obs.LOG_INFO, "Python script loaded successfully")
    obs.obs_frontend_add_event_callback(event_callback)
    global global_settings
    global_settings = settings

def event_callback(event):
    obs.script_log(obs.LOG_INFO, str(event))
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        script_path = os.path.dirname(os.path.realpath(__file__))
        wav_path = os.path.join(script_path, "obs-notify.wav")
        show_notification_setting = obs.obs_data_get_bool(global_settings, "show_notification")
        if show_notification_setting:
            show_notification("OBS Replay Buffer", "Your clip has been successfully saved!")
        else:
            play_sound(wav_path)

        obs.script_log(obs.LOG_INFO, "Replay buffer saved")






def script_unload():
    obs.script_log(obs.LOG_INFO, "Python script unloaded")

def script_description():
    return "Play a sound or show a notification when the replay buffer is saved."

def play_sound(filepath):
    ctypes.windll.winmm.PlaySoundW(ctypes.c_wchar_p(filepath), None, 0x00020000)  # SND_ASYNC flag to play sound asynchronously

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="OBS Studio",

    )