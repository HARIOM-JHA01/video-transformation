from moviepy.editor import VideoFileClip, vfx

def flip_video_x_axis(input_video_path, output_video_path):
    # Load the video clip
    clip = VideoFileClip(input_video_path)
    
    # Flip the video horizontally
    flipped_clip = clip.fx(vfx.mirror_x)
    
    # Write the flipped video to the output path with audio
    flipped_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# Example usage
input_video = 'input_video.mp4'   # Replace with your input video file path
output_video = 'flipped_video.mp4' # Replace with your desired output video file path

flip_video_x_axis(input_video, output_video)

print("Video has been flipped and saved successfully.")
