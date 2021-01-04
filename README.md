# MegaChecker

MegaChecker checks if a [Mega.nz] account is alive (working). It is 100% created in Python (.py). 

This Checker is configured/tested/mantained on **Linux**. The script should work in Windows's CMD too. 

### How to configure:

**Before use, check if python3 and pip is installed!**

First clone the repo:
```sh
$ git clone https://github.com/n1c0t1n3/MegaChecker/
```
Then go to the cloned repo (folder):
```sh
$ cd MegaChecker/
```
Now let's install the requirements:
```sh
$ sudo pip install -r requirements.txt
```

*Thats all! You have configured MegaChecker!*

### Combolists:
MegaChecker supports various lists formats! Amazing, right? But there is a little problem... Not so many understand how to configure the indexes :(. As you know, Python starts indexing from 0. **Remember that!** Let me explain you real quick and simple. 

We have the following combolist:

> **email:password**

Do you remember what I said when I said that Python starts indexing from 0? Great! **This means that "email" is index[0] and "password" is index[1].** What's between them (':') is called a **"criteria"**. 

##### **The program will ask you to introduce the indexes and the criteria!**

Another popular combolist format is this:
>**|email|password|random_data|random_data|random_data|random_data|**

In this example "email" is index[1] and "password" is index[2]. **Why? Because of '|'.** 

### How to start checking:

**Do not use this program to scan stolen accounts! It is illegal. I am not promoting such activities!**

To run the program simply run:
```sh
$ python3 MegaChecker.py
```

The program will request the following informations:

- two indexes (email and password) -- **Please read section "Checklis"**
- the criteria (a symbol like ':' or '|' between the email and password) **Please read section "Checklis"**
- number of threads

> More threads --> More accounts/minute --> More CPU
> Less threads --> Less accounts/minute --> Less CPU

**The recommended number of threads (i5 processor, 6 GB RAM) is 20**

### Requirements:

All requirements are listed in 'requirements.txt'. If you want to talk a look right now, those are the requirements:

- mega py
- pyfiglet
- requests





[Mega.nz]: <https://mega.nz/>
