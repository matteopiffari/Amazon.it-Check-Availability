<p align="center"> 
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://project-piffa.github.io/assets/img/Amazon_disp.svg" alt="Amazon_disp logo"></a>
</p>

<h3 align="center">Amazon.it Check Availability</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

<h4 align="center">⚠️It works only with amazon.it⚠️</h4>

---

## 📝 Table of Contents

- [Setting up a local enviroment](#getting_started)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Authors](#authors)

## 🏁 Getting Started <a name = "getting_started"></a>

To download the source code you just need to type this in a bash:

```console
Project-Piffa@main:~$ git clone https://github.com/Project-Piffa/Amazon.it-Check-Availability
```

Install the modules:

```console
Project-Piffa@main:~$ pip3 install bs4
```

```console
Project-Piffa@main:~$ pip3 install requests
```

```console
Project-Piffa@main:~$ pip3 install schedule
```

```console
Project-Piffa@main:~$ pip3 install python-time
```

Now you just need to edit the main.py file and add your preferences (bot token --> line 11, chatID --> line 12, asin --> line 22 and the messages --> lines 36,37,39).

## 🎈 Usage <a name="usage"></a>

Simple launch the main.py and if you configured all in the right way the script automaticlly send you a message when that product will available.

I suggest to use the "screen" command on linux considering that the script need to run on an always open shell.

## ⛏️ Built With <a name = "tech_stack"></a>

- [VSCode](https://code.visualstudio.com/) - Text Editor
- [Python](https://python.org) - Main programming language

## ✍️ Authors <a name = "authors"></a>

- [@Project-Piffa](https://github.com/Project-Piffa) - Idea & Work
