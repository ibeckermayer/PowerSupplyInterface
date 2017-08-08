# PowerSupplyInterface
## Motivation
PowerSupplyInterface is a GUI I am building to allow myself and my coworkers at the UBC ATLAS group control and log data from our power supply, which we are using in the development of the CHESS-2 detector for eventual use in CERN's Large Hadron Collider (LHC).
## Setup
### Virtual Environments
If you are not doing so already, set up your machine/account to use python virtual environments. A virtual environment is an isolated environment for python which allows you to seamlessly manage package versions and dependencies for various python projects on a single machine.
```
pip install virtualenv
pip install virtualenvwrapper
```
Be sure to look at the [installation instructions](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) for virtualenvwrapper. [This blog](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) is also very helpful for nailing down the basics of working with virtual environments.
### Clone the Repository
```
git clone git@github.com:ibeckermayer/PowerSupplyInterface.git
```
### Get Package Requirements
Make sure you are using a virtual environment made specifically for this project. Everything was developed using Python 2.7.5 and Tkinter 8.5.
```
pip install requirements.txt
```
## Usage
Make sure you are using the virtual environment you made specifically for this project. Start the GUI by running
```
python GUI.py
```
Change the settings by typing a new setting and pressing \<Enter\>. Turn the channels ON and OFF using the radio buttons at the bottom.
