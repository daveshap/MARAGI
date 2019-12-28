from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='maragi_soc',
      version='0.1',
      description='Core MARAGI service; Stream of Consciousness',
      url='https://github.com/daveshap/maragi_soc',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='David Shapiro',
      author_email='daveshap37@gmail.com',
      license='GNU GPLv3',
      packages=['maragi_soc'],
      zip_safe=False)