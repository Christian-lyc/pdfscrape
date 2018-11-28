# pdfscrape
This code is used for counting the key words in PDF. First, it will transform the PDF to txt, then, count the key words in txt. You need to build your own dict. In the dict, Tab is for synonym, Enter is for another key word. Note that, the key word splited in two lines can not be found.

You can also use jieba lib to count it. But it is based on a keyword dict. Sometimes, it may fail to detect your key words.

There is a big folder contained many pdf files, but I couldn't upload. The file directory is fold\北京青年 or fold\廣州日報 and so on.
