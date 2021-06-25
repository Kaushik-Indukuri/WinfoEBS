from setuptools import setup, find_packages


def reqs():
    with open('requirements.txt') as content:
        req = content.read()
        requirement = req.split('\n')
    return requirement


setup(
    name="WinfoEBS",
    author="Kaushik Indukuri",
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=reqs(),
    entry_points="""
        [console_scripts]
        ebs=services.app:ebs
    """,
)