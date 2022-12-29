from django.db import models


"""create table person (
    id serial primary key,
    first_name varchar(50),
    last_name varchar(100),
    birthdate date, 
    address varchar(200)
)"""

class Author(models.Model):

    # No need to create id
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True) # it automatically 
    #                                           assigns the current time to the field
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='posts') # One to Many 
                                                                    #author.post_set - author.posts
   
#   lea = Author.objects.get(first_name='lea')
#   lea.post_set.all()    - > lea.posts.all()

    def __str__(self):  
        return self.title + f' by {self.author.first_name}'

# One to One model Picture, associated with Person
class Picture(models.Model):

    image = models.URLField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Category(models.Model):

    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post, related_name='categories')
                                #post.category_set -> post.categories
    
    def __str__(self):
        return self.name


class Comment(models.Model):

    comment = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title}, {self.created_at}"