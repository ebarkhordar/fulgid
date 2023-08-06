import os
import pathlib

import openai
from dotenv import load_dotenv

current_dir = pathlib.Path(__file__).parent.resolve()
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


class Settings:
    wiqa_train_path = os.path.join(current_dir, "datasets/wiqa-dataset-v2-october-2019/train.jsonl")
    wiqa_test_path = os.path.join(current_dir, "datasets/wiqa-dataset-v2-october-2019/test.jsonl")
    wiqa_dev_path = os.path.join(current_dir, "datasets/wiqa-dataset-v2-october-2019/dev.jsonl")
    boxes_dataset_path = os.path.join(current_dir, "datasets/boxes-only-needed/")
    boxes_code_path = os.path.join(current_dir, "boxes/code/{engine}/{hash}.py")
    boxes_simple_path = os.path.join(current_dir, "boxes/simple/{engine}/{hash}.json")
    sample_range = slice(0, 720)
