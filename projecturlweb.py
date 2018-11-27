import webbrowser
import easygui as eg

url = eg.enterbox("Please enter the URL to check:")


tld = [".com",".edu",".net",".org"]

for site in tld: 
   link = url + site
   webbrowser.open_new_tab("http://" + link)
   print(link)
