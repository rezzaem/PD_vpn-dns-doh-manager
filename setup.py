from setuptools import setup, find_packages

setup(
    name='YourApp',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.png', '*.ico'],  # Include all .png and .ico files in any package
    }
    # ... (Other metadata)
)