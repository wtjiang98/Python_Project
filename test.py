import re

text = '''

</body>
</html>

</body></html>></html>'''

res = re.sub('</body>\s*</html>[\s\S]*', '</body></html>', text)

print(res)
