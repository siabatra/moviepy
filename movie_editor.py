from moviepy.editor import VideoFileClip, concatenate_videoclips

# Concatenate videos
def concatenate_videos(video_paths, output_path):
    clips = [VideoFileClip(path) for path in video_paths]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path, codec="libx264")

# Split video
def split_video(input_path, start_time, end_time, output_path):
    clip = VideoFileClip(input_path).subclip(start_time, end_time)
    clip.write_videofile(output_path, codec="libx264")

# Add text to video
def add_text_to_video(input_path, output_path, text, position=("center", "center"), fontsize=24, color="white"):
    clip = VideoFileClip(input_path)
    txt_clip = (TextClip(text, fontsize=fontsize, color=color)
                .set_position(position)
                .set_duration(clip.duration))
    video = CompositeVideoClip([clip, txt_clip])
    video.write_videofile(output_path, codec="libx264")

# Usage
if __name__ == "__main__":
    # Concatenate videos
    video_paths = ["video1.mp4", "video2.mp4"]
    concatenate_videos(video_paths, "output_concatenated.mp4")

    # Split video
    split_video("input_video.mp4", start_time=10, end_time=20, output_path="output_split.mp4")

    # Add text to video
    add_text_to_video("input_video.mp4", "output_with_text.mp4", text="Hello World")
