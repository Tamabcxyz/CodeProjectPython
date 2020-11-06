from Youtube_Statistics import YT_Statistics

API_KEY="AIzaSyCPl0ky4pDI0yAjdTAoTocNJTdDhXkFr2c"
Channel_id="UCbXgNpp0jedKWcQiULLbDTA"#from url:https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA

Yts=YT_Statistics(API_KEY, Channel_id)
Yts.get_channel_statistics()
Yts.get_channel_video_data()
Yts.dump_file()
#Yts.get_channel_video_data()