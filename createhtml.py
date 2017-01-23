
# Basic html page template to create
create_html = '''
	<!DOCTYPE html>
	<html>
		<head>
			<title>Basic Markups</title>
		</head>
		<body>
			<h1>Hello World!</h1>
		</body>
	</html>
'''		

# Include directory in open creating file in current folder

my_html_file = open("index.html", "w")

my_html_file.write(create_html)

my_html_file.close()
