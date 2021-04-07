# arduboy-flashcart-loader

### Install Dependencies

```
pip install -r requirements.txt
```

1. Generate a new cart index file

```
python manage/generate_flashcart_bin.py custom-flashcart/
```

2. Generate a new image file

```
python manage/flashcart-builder.py custom-flashcart/flashcart-index.csv
```

3. Load the image onto the Arduboy

```
$ python manage/flashcart-writer.py custom-flashcart/flashcart-image.bin
```

Generate flashcart bin file

```
$ python generate_flashcart_bin.py <flashcart_directory_path>
```

Follow this directory structure when setting up your flashcart directory:

```
    - 01-Action
    - - 01-Hopper.hex           # game file
    - - 01-Hopper.png           # game screen file
    - - 02-Lasers.hex
    - - 02.Lasers.png
    - 02-Adventure
    - - 01-Arena.hex
    - - 01-Arena.png
    - Categories                # category screens directory
    - - 01-Action.png           # category screen file
    - - 02-Adventure.png        # category screen file
    - arduboy_loader.png        # title screen
    - flashcart-image.bin       # flash cart image
    - flashcart-index.csv       # flash card index directory needed to build image
```
