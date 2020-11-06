import requests
import json
from tqdm import tqdm #Trong python, nó giúp hiển thị các vòng lặp dưới dạng một giao diện tiến độ một cách thông minh – chỉ cần bọc bất kỳ vòng lặp nào bằng tqdm và bạn không phải lo cài đặt hiển thị tiến trình cho nó nữa
class YT_Statistics:
    def __init__(self, api_key, channel_id):
        self.api_key=api_key
        self.channel_id=channel_id
        self.channel_statistics=None
        self.video_data=None
    def get_channel_statistics(self):
        url=f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        json_fromURL=requests.get(url)
        data=json.loads(json_fromURL.text)
        try:
            data=data["items"][0]["statistics"]
        except:
            data=None
        self.channel_statistics=data
        return data
        
    def get_channel_video_data(self):
        # 1) get video id
        getvideo=self.get_video(limit=50)
        #print(getvideo)
        # 2) get like, comment....
        parts=["snippet","statistics","contentDetails"]
        for video_id in tqdm(getvideo):
            for part in parts:            
                data=self.get_single_video_data(video_id,part)
                getvideo[video_id].update(data)
        self.video_data=getvideo
        return getvideo
        
    def get_single_video_data(self, video_id, part):
        url=f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
        json_fromURL=requests.get(url)
        data=json.loads(json_fromURL.text)
        try:
            data=data['items'][0][part]
        except:
            print("Error")
            data=dict()
        return data
        
    def get_video(self, limit=None):
        url=f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date"
        if limit is not None and isinstance(limit, int):
            url+="&maxResults="+str(limit)
        vid, ntp=self.get_video_by_page(url)
        index=0
        while(ntp is not None and index<10):
            nexturl=url+"&pageToken="+ntp
            nextvid, ntp=self.get_video_by_page(nexturl)
            vid.update(nextvid)
            index+=1
            
        return vid
    
    def get_video_by_page(self, url):#from here https://www.googleapis.com/youtube/v3/search?key=AIzaSyCPl0ky4pDI0yAjdTAoTocNJTdDhXkFr2c&channelID=UCbXgNpp0jedKWcQiULLbDTA&part=id&order=date&maxResults=50&pageToken=CMgBEAA
        json_url=requests.get(url)
        data=json.loads(json_url.text)
        video_of_channels=dict()
        if "items" not in data:
            return video_of_channels,None
        item_data=data["items"]
        next_page=data.get("nextPageToken", None)
        for item in item_data:
            try:
                kind=item["id"]["kind"]
                if kind=="youtube#video":
                    video_id=item["id"]["videoId"]
                    video_of_channels[video_id]=dict()
            except KeyError:
                print("error")
        return video_of_channels, next_page
        
        
    def dump_file(self):
        if self.channel_statistics is None or self.video_data is None:
            print("data is none")
            return
        fill_data={self.channel_id:{"channel_statistics":self.channel_statistics, "video_data":self.video_data}}
        name_channel=self.video_data.popitem()[1].get('channelTitle', self.channel_id)
        name_channel=name_channel.replace(" ","_").lower()
        name_file=name_channel+".json"
        with open(name_file,"w") as f:
            json.dump(fill_data,f, indent=4)
        print("File .json saved")
        