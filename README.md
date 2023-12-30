# art-critic

This is a simple game I made last night using pygame and GPT-4. 

The user draws on a canvas while being observed by a pixelated "art critic". 

<img width="600" alt="Screenshot 2023-12-30 at 1 45 20 PM" src="https://github.com/ju-mc/art-critic/assets/68313879/9aae4fa9-1ef8-45fc-82b1-3af72081aa0e">

When the drawing is complete, the art critic then provides an elaborate interpretation of the artwork. 

<img width="600" alt="Screenshot 2023-12-30 at 1 46 41 PM" src="https://github.com/ju-mc/art-critic/assets/68313879/e78dfb9f-b57c-44a1-b424-e70bed68758f">

## Architecture

The drawing component is built using pygame. Once the drawing is complete, it is passed to an image-to-text model. I used the [Salesforce blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base), which was designed for image caption generation. The caption generated from this model (it is usually short and lacking descriptive details) is then passed to GPT-4 with a prompt requesting a rephrasing of the generated caption based on certain parameters, and the result of that prompt is the output. 

## How to set up and use

This is a first draft that lacks a proper UI. I am working on a web app version and I will post an update here when that is completed. 
#### Setup:
1. Clone the repo
2. Create a virtual environment within the cloned repo. I used virtualenv.
3. Install the requirements
4. Create a .env file for your OpenAI key. The .env file should have the following: OPENAI_API_KEY="PASTE YOUR KEY HERE"
5. Run the drawing-board.py script. This should load the drawing canvas. Create your drawing, and then close the canvas.
6. Your drawing will be saved within the same directory ('drawing.png')
7. Run the image-to-text.py script. This should take a couple minutes. Your interpretation will be generated within the terminal. 


