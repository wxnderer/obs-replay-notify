import obspython as obs
import os, ctypes, sys
from plyer import notification

def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_bool(props, "show_notification", "Play windows notification instead of sound")
    obs.obs_properties_add_bool(props, "custom_audio", "Use custom audio file")
    obs.obs_properties_add_path(props, "wav_path", "WAV Audio File Path", obs.OBS_PATH_FILE, "WAV Files (*.wav)", None)
    obs.obs_properties_add_bool(props,"play_start_stop_audio", "Play Audio for Replay Buffer Start/Stop Event")
    
    return props

def script_load(settings):
    obs.script_log(obs.LOG_INFO, "Python script loaded successfully")
    obs.obs_frontend_add_event_callback(event_callback)
    global global_settings
    global_settings = settings

def event_callback(event):
    obs.script_log(obs.LOG_INFO, str(event))
    script_path = os.path.dirname(os.path.realpath(__file__))
    wav_path = obs.obs_data_get_string(global_settings, "wav_path")
    show_notification_setting = obs.obs_data_get_bool(global_settings, "show_notification")
    custom_audio = obs.obs_data_get_bool(global_settings, "custom_audio")
    playStartStopEvent = obs.obs_data_get_bool(global_settings, "play_start_stop_audio")
    if event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_SAVED:
        if show_notification_setting:
            show_notification("OBS Replay Buffer", "Your clip has been successfully saved!")
        else:
            if wav_path and custom_audio:
                play_sound(wav_path)
            else:
                play_sound(os.path.join(script_path, "audio/obs-notify.wav"))

        obs.script_log(obs.LOG_INFO, "Replay buffer saved")

    if playStartStopEvent and event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_STOPPED:
        obs.script_log(obs.LOG_INFO, "Recording stopped")
        play_sound(os.path.join(script_path, "audio/obs-replay-buffer-stopped.wav"))
    if playStartStopEvent and event == obs.OBS_FRONTEND_EVENT_REPLAY_BUFFER_STARTED:
        obs.script_log(obs.LOG_INFO, "Recording started")
        play_sound(os.path.join(script_path, "audio/obs-replay-buffer-started.wav"))

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
