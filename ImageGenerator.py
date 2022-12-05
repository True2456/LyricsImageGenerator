import openai as openai

key = ""
openai.api_key = key
image = []
def getLyrics(input):
    # Open the file for reading
    with open(input, 'r') as f:
        # Read the file contents
        text = f.read()

    # Split the file contents by lines
    lines = text.splitlines()

    # Create an empty array
    arr = []

    # Loop through the lines and add each line to the array
    for line in lines:
        arr.append(line)
    return arr

def generateImage(inputText):
    response = openai.Image.create(
      prompt= inputText,
      n=1,
      size="256x256"
    )
    return response['data'][0]['url']


def storeImage(lyrics):
    for i, item in enumerate(lyrics):
        try:
            print(item)
            img = generateImage(item)
            print("Image URL = " + img)
            image.append(img)
        except:
            pass


grinspoon = getLyrics('lyrics.txt')
storeImage(grinspoon)
print(image)