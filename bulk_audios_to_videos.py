import moviepy.editor as mp
import os

def add_audio_to_video(video_path: str, audio_path: str, output_path: str) -> None:
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(audio_path)

    if audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)

    video = video.set_audio(audio)
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

def bulk_add_audios_to_videos(videos_directory: str, audios_directory: str, output_directory: str) -> None:
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    video_files = [f for f in os.listdir(videos_directory) if f.endswith(".mp4")]
    audio_files = [f for f in os.listdir(audios_directory) if f.endswith(".mp3")]

    if len(video_files) != len(audio_files):
        print("Ilość plików audio nie odpowiada ilości plików wideo.\n \
              Popraw to aby każdy dźwięk był prawidłowo przyporządkowany")
        return

    for video_file, audio_file in zip(video_files, audio_files):
        video_path = os.path.join(videos_directory, video_file)
        audio_path = os.path.join(audios_directory, audio_file)
        output_path = os.path.join(output_directory, 'a_' + video_file)
        
        add_audio_to_video(video_path, audio_path, output_path)
        print(f"Film {video_file} posiada już audio {audio_file}!")

# Define the paths
videos_directory = 'videos'
audio_file = 'audios'
output_directory = 'results'

# Run the bulk processing
bulk_add_audios_to_videos(videos_directory, audio_file, output_directory)
