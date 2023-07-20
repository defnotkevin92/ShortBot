# ShortBot
Generates and uploads unique short form content based on responses from AI prompted by random variable.

**This is just a learning project so I'm sure there's a lot to be improved upon, feel free to chime in,
  I'm open to suggestions and criticisms 

**Eventually I intend to have the actaul animation automated as well but I need to find somethinkg akin to Freecad's python console
  As it stands this project requires you to provide a short video, or a still, to be looped as the background (.wav works well)

The main script first runs the AI generated text section. In my case I used ChatGPT but you could swap out the API for whatevr chatbot you prefer. Find an open ended topic, I chose to ask chatgpt to give me horoscopes while playing subversive roles,save the response text.
Next we run the text though a TTS API from Coqui studio (will likely soon be replaced by Mozilla TTS pre trained) to get a .wav file, and then run that though the python srt library to generate a subtitle file. We then use moviepy to combine the video clip you provided with the .wav and get a temporary mp4 file.
We then run that mp4 through moviepy again along with .srt file to embed the subtitles in sync with the audio.

I'm still working out the kinks in the last step which is to upload the video to youtube automatically via the API.Eventually I want to compile everything into a neat desktyop app, but so far the Youtube API doesn't seem to like being called outside of the console. There's probably a way around this that I just haven't found yet, for instance I know I could use pyautogui to input the concole commands but at that point I could've just used that to do the upload without the API and I don't wanna do that, I wanna streamline this janky process lol. I'm working out of jupyterlab and have gotten it to upload properly by calling the upload script from a cell but I don't know if that's gonna translate to the end functionality that I'm looking for. I'll update this as soon as I make a change.

**It's worth noting that if you want to avoid the api's, you could get a local chatbot like GPT4ALL, implement the Mozilla TTS, and utilize selenium and pyautogui to handle the youtube upload, and then your script would not need any API accounts.
