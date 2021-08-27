# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
scripts.documentation.py

This file handles the middle logic for moving the markdown to the Docusaurus documentation

- Copyright: (c) 2021 Facebook
- License: MIT LICENSE
"""

# Package imports
import json
import os


def main():
    """
    Control flow

    :return: None
    """

    if not os.path.isdir('./docs/docs/sdk'):
        os.mkdir('./docs/docs/sdk')

    if not os.path.isfile('./docs/docs/sdk/_category_.json'):
        with open('./docs/docs/sdk/_category_.json', mode='w') as category_handle:
            json.dump({
                "label": "Mapillary Python SDK - Interface",
                "position": 4
            }, category_handle, indent=4)

    markdown_list = os.listdir('./sphinx-docs/_build/markdown/')

    markdown_list.sort()

    for index, file in enumerate(markdown_list):
        with open(f'./sphinx-docs/_build/markdown/{file}', mode='r') as markdown_content:
            generated_markdown = ' '.join(markdown_content.readlines())

        with open(f'./docs/docs/sdk/{file}', mode='w') as documentation_handle:
            documentation_handle.writelines('---\n'
                                            f'sidebar_position: {index}\n'
                                            '---\n'
                                            '\n'
                                            f'{generated_markdown}')


if __name__ == '__main__':
    """
    Control flow
    """
    main()
