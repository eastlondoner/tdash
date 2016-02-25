
python setup.py sdist upload -r pypi

conda skeleton pypi tox
conda build tox
conda skeleton pypi pydash
conda build pydash
conda skeleton pypi tdash
conda build tdash