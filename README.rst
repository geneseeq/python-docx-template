====================
python-docx-template
====================

Use a docx as a jinja2 template

Introduction
------------

This package uses 2 major packages :

- python-docx for reading, writing and creating sub documents
- jinja2 for managing tags inserted into the template docx

python-docx-template has been created because python-docx is powerful for creating documents but not for modifying them.

The idea is to begin to create an exemple of the document you want to generate with microsoft word, it can be as complex as you want :
pictures, index tables, footer, header, variables, anything you can do with word.
Then, as you are still editing the document with microsoft word, you insert jinja2-like tags directly in the document.
You save the document as a .docx file (xml format) : it will be your .docx template file.

Now you can use python-docx-template to generate as many word documents you want from this .docx template and context variables you will associate.

Documentation
-------------

Please, `read the doc <http://docxtpl.readthedocs.org>`_

Install
-------------
依赖的包有：
docxtpl-0.2.3.tar.gz
six-1.10.0-py2.py3-none-any.whl
Sphinx-1.2.3-py2-none-any.whl
sphinxcontrib_napoleon-0.5.3-py2.py3-none-any.whl
python-docx-0.8.6.tar.gz
Jinja2-2.8-py2.py3-none-any.whl
lxml-3.6.4.tar.gz
Pygments-2.1.3-py2.py3-none-any.whl
docutils-0.12.tar.gz
pockets-0.3-py2.py3-none-any.whl
MarkupSafe-0.23.tar.gz

windows环境安装
-------------

1.pip工具安装
（1）下载http://www.pip-installer.org/en/latest/installing.html 
（2）python get-pip.py,查看C:\Python27\Scripts有没有pip
2.安装docxtpl
pip install docxtpl
一般会安装不成功，是因为lxml安装失败
解决办法：下载lxml-2.3.win-amd64-py2.7.exe安装lxml（lxml依赖比较多，建议直接exe安装）

ubuntu环境安装
-------------
1.安装docxtpl

pip install docxtpl
如果安装失败，安装需要安装xml
lxml安装
（1）apt-get install libxml2-dev libxslt-dev python-dev
（2）apt-get install python-lxml
