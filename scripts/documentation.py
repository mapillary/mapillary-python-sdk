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
import re


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
            generated_markdown = ''.join(markdown_content.readlines())

        if file == 'index.md':

            generated_markdown = generated_markdown.replace('src’s', 'the Mapillary’s Python SDK')

            with open('./docs/docs/Table Of Contents.md', mode='w') as index_file:
                index_file.writelines('---\n'
                                      f'sidebar position: 1\n'
                                      '---\n'
                                      '\n'
                                      f'{generated_markdown}')

        else:

            package = generated_markdown[:generated_markdown.find('\n')].split(' package')[0][2:]

            if not os.path.exists(f'./docs/docs/{package}'):
                os.mkdir(f'./docs/docs/{package}')

                with open(f'./docs/docs/{package}/_category_.json', mode='w') as metadata_file:
                    json.dump({
                        "label": package.replace('.', ' ').title(),
                    }, metadata_file, indent=4)

                with open(f'./docs/docs/{package}/{package}.md', mode='w') as index_file:
                    index_file.writelines('---\n'
                                          f'sidebar position: 2\n'
                                          '---\n'
                                          '\n'
                                          f'{package}')

            modules = re.findall(r'## .*? module', generated_markdown)

            for iteration in range(0, len(modules)):

                # If not last iteration
                if not iteration == len(modules) - 1:

                    start_pos = re.search(modules[iteration], generated_markdown).end() + 1

                    end_pos = re.search(modules[iteration + 1], generated_markdown).start() - 1

                # Else, we are at the last iteration
                else:

                    start_pos = re.search(modules[iteration], generated_markdown).end() + 1

                    end_pos = len(generated_markdown)

                extracted_module = generated_markdown[start_pos:end_pos]

                module_name = modules[iteration][3:-7]

                with open(f'./docs/docs/{package}/{module_name}.md', mode='w') as markdown_handler:
                    markdown_handler.writelines('---\n'
                                                f'sidebar position: {iteration + 2}\n'
                                                '---\n'
                                                '\n'
                                                f'{extracted_module}')


if __name__ == '__main__':
    """
    Control flow
    """
    main()
