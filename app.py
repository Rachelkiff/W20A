import dbcreds
import mariadb

option = input("Please select 1 to enter a new blog post: \nPlease select 2 to view all blog posts!: ")

if(option == '1'):
   username = input("Please enter your username: ")
   content = input("Write a new blog post!: ")
   conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database) 
   cursor = conn.cursor()
   cursor.execute("INSERT INTO blog_post(username, content) VALUES (?, ?)", [username, content]) 
   conn.commit()
   print("Your blog has been posted!")
   cursor.close()
   conn.close()

elif(option == '2'):
   content = input("See all blog posts!: ")
   conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database) 
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM blog_post WHERE content=?", [content,])
   blog_posts = cursor.fetchall()
   for blog_post in blog_posts:
      print("content: " + str(blog_post[0]))
  

