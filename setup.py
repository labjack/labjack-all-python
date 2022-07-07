from setuptools import setup

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: System :: Hardware'
    ]

setup(name="labjack",
      version='0.0.1',
      description='LabJack Python wrappers',
      url='https://labjack.com/support/software/',
      author='LabJack Corporation',
      author_email="support@labjack.com",
      maintainer='LabJack Corporation',
      maintainer_email='support@labjack.com',
      classifiers=CLASSIFIERS,
      license='MIT X11',
      )
