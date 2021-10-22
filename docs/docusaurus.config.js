/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @format
 */

/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'Mapillary Python SDK',
  tagline: 'A Python 3 library built on the Mapillary API v4 to facilitate retrieving and working with Mapillary data',
  url: 'https://mapillary.github.io',
  baseUrl: '/mapillary-python-sdk/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'mapillary', // Usually your GitHub org/user name.
  projectName: 'mapillary-python-sdk', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'Mapillary Python SDK',
      logo: {
        alt: 'Mapillary',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Tutorial',
        },
        {to: 'blog', label: 'Blog', position: 'left'},
        // Please keep GitHub link to the right for consistency.
        {
          href: 'https://github.com/mapillary/mapillary-python-sdk',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learn',
          items: [
            {
              label: 'Style Guide',
              to: 'docs/',
            },
            {
              label: 'Second Doc',
              to: 'docs/doc2',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Forum',
              href: 'https://forum.mapillary.com/',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/mapillary',
            },
            {
              label: 'Facebook',
              href: 'https://www.facebook.com/mapillary/',
            },
          ],
        },
        {
          title: 'More',
          items: [
            // Do we want to keep the SDK blog?
              // For now, commented out
            //   {
            //   label: 'SDK Blog',
            //   to: 'blog',
            // },
            {
              label: 'Blog',
              href: 'https://blog.mapillary.com/',
            },
            {
              label: 'Website',
              href: 'https://www.mapillary.com/',
            }
          ],
        },
        {
          title: 'SDK',
          items: [
            {
              label: 'PyPi Homepage',
              href: 'https://pypi.org/project/mapillary/'
            },
            {
              label: 'Developer Resources',
              href: 'https://www.mapillary.com/developer'
            },
            {
              label: 'GitHub',
              href: 'https://github.com/mapillary/mapillary-python-sdk',
            },
            {
             label: 'Bug Tracker',
             href: 'https://github.com/mapillary/mapillary-python-sdk/issues',
            },
            {
              label: 'Release Notes',
              href: 'https://github.com/mapillary/mapillary-python-sdk/releases'
            },
            {
              label: 'Download',
              href: 'https://pypi.org/project/mapillary/#files'
            }
          ]
        },
        {
          title: 'Legal',
          // Please do not remove the privacy and terms, it's a legal requirement.
          items: [
            {
              label: 'Privacy',
              href: 'https://opensource.facebook.com/legal/privacy/',
            },
            {
              label: 'Terms',
              href: 'https://opensource.facebook.com/legal/terms/',
            },
            {
              label: 'Data Policy',
              href: 'https://opensource.facebook.com/legal/data-policy/',
            },
            {
              label: 'Cookie Policy',
              href: 'https://opensource.facebook.com/legal/cookie-policy/',
            },
          ],
        },
      ],
      logo: {
        alt: 'Facebook Open Source Logo',
        src: 'img/oss_logo.png',
        href: 'https://opensource.facebook.com',
      },
      // Please do not remove the credits, help to publicize Docusaurus :)
      copyright: `Copyright © ${new Date().getFullYear()} Facebook, Inc. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl: 'https://github.com/facebook/docusaurus/edit/main/website/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            'https://github.com/facebook/docusaurus/edit/main/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
