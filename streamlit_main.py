import streamlit as st
import torch
from torch import nn
import torchvision.transfroms as transforms
import os, json

st.title('FashionMNIST')
img_file=st.file_uploader('이미지를 업로드 하세요', type=['png','jpg','jpeg'])
