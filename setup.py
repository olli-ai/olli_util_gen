import os
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as fin:
    lines = fin.readlines()
    lines = [o.strip() for o in lines]
    lines = [o for o in lines if len(o) > 0]
    req = [o for o in lines if not o.startswith('#') and not o.startswith('git+')]

dirname = os.path.dirname(__file__)
version_file = os.path.join(dirname, 'version.txt')
with open(version_file, 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name='olli-util-gen',  # Replace with your username
    version=version,
    author='Huy',
    author_email='nghuy1290@gmail.com',
    description='DESC',
    long_description=long_description,
    install_requires=req,
    long_description_content_type='text/markdown',
    url='https://github.com/nguyenhuy-olli',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)