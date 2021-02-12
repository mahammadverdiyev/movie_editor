from moviepy.editor import *

original_clip = VideoFileClip('countdown.mp4')
small_clip1 = original_clip.resize(0.5)
small_clip2 = small_clip1.fx(vfx.mirror_x)
small_clip3 = small_clip1.fx(vfx.mirror_y)
small_clip4 = small_clip2.fx(vfx.mirror_y)

final_clip = clips_array([[small_clip1, small_clip2],
                          [small_clip3, small_clip4]])

final_clip.write_videofile('countdownedited.mp4')
