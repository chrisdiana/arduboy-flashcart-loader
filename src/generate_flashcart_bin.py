"""
Generate flashcart bin file

Run with:
    python generate_flashcart_bin.py <flashcart_directory_path>

Follow this directory structure:

    - 01-Action
    - - 01-Hopper.hex	        # game file
    - - 01-Hopper.png	        # game screen file
    - - 02-Lasers.hex
    - - 02.Lasers.png
    - 02-Adventure
    - - 01-Arena.hex
    - - 01-Arena.png
    - Categories				# category screens directory
    - - 01-Action.png 	        # category screen file
    - - 02-Adventure.png 		# category screen file
    - arduboy_loader.png 		# title screen
    - flashcart-image.bin 		# flash cart image
    - flashcart-index.csv		# flash card index directory needed to build image

"""
import os
import sys
import pandas as pd


def main(flashcart_path):
    headers = [
        'List',
        'Discription',
        'Title screen',
        'Hex file',
        'Data file',
        'Save file',
    ]

    categories = (list(map(lambda x: x.replace('.png', ''),
            os.listdir(os.path.join(flashcart_path, 'Categories')))))
    categories.sort()

    data = {
        'List': [0],
        'Discription': ['Bootloader'],
        'Title screen': ['arduboy_loader.png'],
        'Hex file': [None],
        'Data file': [None],
        'Save file': [None],
    }

    for idx, category in enumerate(categories):
        category_num = idx + 1
        files = (list(set(filter(lambda x: x != '.DS_Store',
            map(lambda x: x.replace('.png', '').replace('.hex', ''),
            os.listdir(os.path.join(flashcart_path, f'{category}')))))))

        files.sort()

        data['List'].append(category_num)
        data['Discription'].append(category)
        data['Title screen'].append(f'Categories/{category}.png')
        data['Hex file'].append(None)
        data['Data file'].append(None)
        data['Save file'].append(None)

        for f in files:
            data['List'].append(category_num)
            data['Discription'].append(f)
            data['Title screen'].append(f'{category}/{f}.png'),
            data['Hex file'].append(f'{category}/{f}.hex'),
            data['Data file'].append(None)
            data['Save file'].append(None)

    df = pd.DataFrame(data, columns=headers)
    df.to_csv(os.path.join(flashcart_path, 'flashcart-index.csv'), sep=';', index=False)
    print(df)


if __name__ == "__main__":
    flashcart_path = sys.argv[1]
    if flashcart_path:
        main(flashcart_path)
    else:
        print('Missing flashcart path: python generate_flashcart_bin.py <flashcart_directory_path>')
