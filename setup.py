from setuptools import setup, find_packages


install_requires = [
    "Flask==0.8",
    "Flask-WTF==0.5.2",
    "WTForms==0.6.3",
    "Jinja2==2.6",
    "MarkupSafe==0.15",
    "Werkzeug==0.8.2",
    "nose-exclude",
]


setup_requires = [
    "mock==0.8.0",
    "nose==1.1.2",
    "nosexcover==1.0.7",
    "pylint==0.25.1",
    "nose-exclude"
]


setup(
    name="flask-ml-api",
    version="0.0.1",
    description="",
    url="https://github.com/krisneuharth/flask-ml-api",
    long_description="Flask ML API",
    author="Kris Neuharth",
    author_email="kris.neuharth@gmail.com",
    maintainer="Kris Neuharth",
    maintainer_email="kris.neuharth@gmail.com",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    test_suite="nose.collector",
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: MIT",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Windows",
        "Programming Language :: Python :: 2.7"
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development",
    ],
)
