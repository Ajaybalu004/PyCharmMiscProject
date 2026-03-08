count = 0
n = int(input("Enter the value:"))
for i in range(n):
    num = int(input("Enter the value:"))
    if num %2 == 0:
        count +=1

print("Number of even:",count)
from spotipy.cauth2 import spotipyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re