from setuptools import setup

setup(
    name='getreqt',
    version='0.2',
    description='get requirements tree for installed pip packages',
    url='https://github.com/andermi/getreqt',
    author='Michael Anderson',
    author_email='manders9@jhu.edu',
    license='MIT',
    install_requires=['asciitree'],
    scripts=['getreqt'],
    zip_safe=False
)
