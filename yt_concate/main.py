from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownLoadCaptions
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight

channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"

def main():
    inputs = {
        "channel_id": channel_id
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownLoadCaptions(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()