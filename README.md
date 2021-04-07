# Arduboy Flashcart Loader

Some utilities to make loading new game libraries onto the FX chip a little easier. Thanks to [Mr.Blinky](https://github.com/MrBlinky) for all the great work in putting together the [Arduboy Python Utilities](https://github.com/MrBlinky/Arduboy-Python-Utilities) that this package uses.


## Quick Start

1. Clone the repo

```
$ git clone --recursive git@github.com:chrisdiana/arduboy-flashcart-loader.git
```

2. Install dependencies

```
$ pip install -r requirements.txt
```

3. Setup your game library using the `example-flashcart` directory as a template. Follow the directory structure below:

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

4. Connect your Arduboy FX and run the `all` command while passing the directory of your flashcart

```
$ ./run.sh all example-flashcart/
```


## Run commands standalone

Generate the flashcart index file

```
$ ./run.sh index example-flashcart/

OR

$ python src/generate_flashcart_bin.py example-flashcart/
```

Generate the flashcart image bin file

```
$ ./run.sh build example-flashcart/

OR

$ python Arduboy-Python-Utilities/flashcart-builder.py example-flashcart/flashcart-index.csv
```

Load the image onto the Arduboy

```
$ ./run.sh write example-flashcart/

OR

$ python Arduboy-Python-Utilities/flashcart-writer.py example-flashcart/flashcart-image.bin
```


