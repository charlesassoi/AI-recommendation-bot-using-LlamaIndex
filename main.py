!pip install --upgrade llama-index llama-index-embeddings-huggingface llama-index-llms-huggingface transformers accelerarate bitsandbytes

from llama_index.core import Settings, VectorStoreIndex,Document
from llama_index.embeddings.huggingface import huggingFaceEmbedding
from llama_index.llms.huggingface import huggingFaceLLM
import torch
import pandas as pd
import os