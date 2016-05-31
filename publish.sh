
python setup.py sdist 
twine upload dist/*

conda skeleton pypi tox
conda build tox
conda skeleton pypi pydash
conda build pydash
conda skeleton pypi tdash
conda build tdash
