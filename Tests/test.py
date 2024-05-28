import re
cloud_watch_topic = "社外Webとの同期時に409エラーが発生しました。"

pattern_for_5xx = r"5[0-9]{2}"
if re.findall(pattern_for_5xx, cloud_watch_topic):
    cloud_watch_topic = re.sub(pattern_for_5xx, "5xx", cloud_watch_topic)
print(cloud_watch_topic)
pattern_for_4xx = r"4[0-9]{2}"
if re.findall(pattern_for_4xx, cloud_watch_topic):
    cloud_watch_topic = re.sub(pattern_for_4xx, "4xx", cloud_watch_topic)
    
print(cloud_watch_topic)
