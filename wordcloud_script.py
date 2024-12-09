from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
# Load the text data
with open('sample.txt', 'r') as file:
    text = file.read()

# Generate the word cloud
mask = np.array(Image.open('CSE_64_K.png'))
wordcloud = WordCloud(width=800, height=500, background_color='black', mask=mask, colormap='gist_ncar'
).generate(text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.title("Word Cloud", fontsize=16)
plt.show()

wordcloud.to_file('wordcloud.png')
