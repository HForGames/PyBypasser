from distutils.core import setup

setup(
    name="PyBypasser",
    version="0.0.2",
    author="Hugo GALAN",
    url="https://github.com/HForGames/PyBypasser",
    download_url="https://github.com/HForGames/PyBypasser",
    long_description="""PyBypasser is a package to Bypass everything that can be Bypass""",
    licence="MIT",
    packages=["PyBypasser"],
    classifiers=["Development Status :: 1 - Planning",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python",
                 'Programming Language :: Python :: 3',
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    install_requires=["certifi==2022.9.14"
                      "charset-normalizer==2.1.1",
                      "idna==3.4",
                      "requests==2.28.1",
                      "urllib3==1.26.12"]
)
