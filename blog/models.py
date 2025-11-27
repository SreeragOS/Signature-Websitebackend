from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = [
        ("Personal", "Personal"),
        ("Veterinary", "Veterinary"),
        ("Literature", "Literature"),
        ("Art", "Art"),
    ]

    SUBCATEGORY_CHOICES = [
        ("personal", "Personal"),
        ("achievements", "Achievements"),
        ("Experiences", "Experiences"),
        ("case studies", "Case Studies"),
        ("projects", "Projects"),
        ("Articles", "Articles"),
        ("files", "Files"),
        ("stories", "Stories"),
        ("novels", "Novels"),
        ("Poems", "Poems"),
        ("Autobiography", "Autobiography"),
        ("Drawings", "Drawings"),
        ("paintings", "Paintings"),
        ("Crafts", "Crafts"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    document = models.FileField(upload_to='post_documents/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="Personal")
    subcategory = models.CharField(max_length=30, choices=SUBCATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

