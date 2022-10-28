from yt_concate.pipeline.steps.step import Step

class Preflight(Step):
    def process(self, data, input, utils):
        print('in preflight')
        utils.creat_dirs()