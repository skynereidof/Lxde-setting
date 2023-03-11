from setuptools import setup, find_packages

setup(
    name='lxdesetting',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['lxde-setting = lxdesetting.setting:main']
    },
    install_requires=[
        'requests',
        'beautifulsoup4',
        'Pillow',
        'pywebview[qt]',
    ],
    author='skynereidof',
    description='GUI tool for configuring LXDE desktop environment on Linux',
    license='MIT',
    keywords='lxde desktop environment linux',
    url='https://github.com/skynereidof/Lxde-setting',
)
