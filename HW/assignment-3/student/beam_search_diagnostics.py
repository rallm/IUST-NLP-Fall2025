import os
import time
import sys
import json

def get_diagnostic_info():
    return {
        "machine": "colab_instance",
        "u": "colab_user",  # Fixed: Hardcoded to avoid OSError
        "w": os.getcwd(),
        "d": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def format_example_sentence(source, target, beam_search_output, train_iter):
    data = {
        "example_source": source,
        "example_target": target,
        "hypotheses": beam_search_output,
        "diagnostic_info": get_diagnostic_info(),
        "train_iter": train_iter
    }
    return json.dumps(data, indent=2)