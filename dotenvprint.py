from io import BytesIO
import streamlit as st
from audiorecorder import audiorecorder  # type: ignore
from dotenv import dotenv_values
from hashlib import md5
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams
from pathlib import Path


p=Path('../../dot_env')
env = dotenv_values(p / ".env")
url=env['OPEN_AI_KEY']
print(url)