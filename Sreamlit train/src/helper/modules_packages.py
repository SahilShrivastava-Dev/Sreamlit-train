import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from openai import OpenAI
from gnews import GNews
from PyPDF2 import PdfReader
import PyPDF2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import aspose.pdf as ap
import streamlit as st
import plotly.graph_objects as go
