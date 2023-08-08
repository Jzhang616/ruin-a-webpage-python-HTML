# ruin-a-webpage-python-HTML
A Python function that takes a single string argument named filename. filename will contain the name of an HTML file.
The extension of the file is first checked and if the extension is not ".html" or ".htm", then the function should return None.

Otherwise the function should:
1. Use regular expressions to find content enclosed in paragraph tags, <p> and </p>, remove
the paragraph tags, and then append 2 line break tags to the content, <br><br>
2. Remove all matched pairs of open and close span tags, <span> and </span>
3. Write the modified HTML content to a file called, "ruined.html"
