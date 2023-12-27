# Prompt Engineering for Diversity and Image Quality

This repo includes the final paper and the presentation slides for my CS839 couse on Image Synthesis and Manipulation. 

My part of the project focused on the ability to quantify bias in the output of a generative image model along the axes of age, sex, and race. I created a standardized dataset of prompts (like "The librarian is reading a book."). Next, I created a program for 'diversifying' such prompts (generating prompts like "The 15 year old asian female librarian is reading a book."). Then, I propose a "diversity score" to capture how well a generative model outputs diverse images of humans. Finally, I evaluate a method for computing such a score automatically using the [DeepFace](https://github.com/serengil/deepface) Python framework, which provides off-the-shelf facial attribute analysis. Please note that the generated images are not included in this repo.

Please check out the paper or slides for more info, or check out `results.ipynb` for a walkthrough of how the results were generated. Big thanks to my teammates Shawn Zhong and Xin Yuan!