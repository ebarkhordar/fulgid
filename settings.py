import os
import pathlib

current_dir = pathlib.Path(__file__).parent.resolve()


class Settings:
    wiqa_train = os.path.join(current_dir, "datasets/wiqa-dataset-v2-october-2019/train.jsonl")
    wiqa_test = os.path.join(current_dir, "datasets/wiqa-dataset-v2-october-2019/test.jsonl")
    wiqa_dev = os.path.join(current_dir, "datasets/wiqa-dataset-v2-october-2019/dev.jsonl")
    boxes_dataset = os.path.join(current_dir, "datasets/boxes-only-needed/")