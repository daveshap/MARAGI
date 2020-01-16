from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


"""
cheat sheet reminder for myself because I'm dumb

python setup.py sdist bdist_wheel
python -m twine upload dist/*
"""


setup(name='maragi',
      version='0.2.2',
      description='Core MARAGI components; Server and Client',
      url='https://github.com/daveshap/maragi',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='David Shapiro',
      author_email='daveshap37@gmail.com',
      license='MIT',
      packages=['maragi'],
      zip_safe=False)