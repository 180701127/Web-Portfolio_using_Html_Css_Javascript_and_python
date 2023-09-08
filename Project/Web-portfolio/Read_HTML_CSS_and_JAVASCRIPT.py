import webbrowser
import codecs
f = open('Index.html', 'r')
print(f)
file1 = codecs.open("Index.html", 'r', "utf-8")
file2 = codecs.open("Style.css", 'r', "utf-8")
file3 = codecs.open("Nlk_Script.js", 'r', "utf-8")
print(file1.read())
print(file2.read())
print(file3.read())
webbrowser.open_new_tab('Index.html')
f.close()




