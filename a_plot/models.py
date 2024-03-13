from django.db import models
import uuid
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# from django.templatetags.static import static


CATEGORIES = (
    ("Campsite", "Campsite"),
    ("Official", "Official"),
    ("Wild", "Wild"),
)

CATEGORIES_PARAMS = {
    1: {"slug": "campsite", "name": "Campsite"},
    2: {"slug": "official", "name": "Official"},
    3: {"slug": "wild", "name": "Wild"},
}

COUNTRIES = (
    ("Spain", "Spain"),
    ("France", "France"),
    ("Portugal", "Portugal"),
    ("Italy", "Italy"),
    ("Germany", "Germany"),
    ("Netherlands", "Netherlands"),
    ("Belgium", "Belgium"),
    ("Switzerland", "Switzerland"),
    ("Sweden", "Sweden"),
    ("Norway", "Norway"),
    ("Finland", "Finland"),
    ("Denmark", "Denmark"),
    ("Ireland", "Ireland"),
    ("United Kingdom", "United Kingdom"),
    ("Austria", "Austria"),
    ("Greece", "Greece"),
    ("Croatia", "Croatia"),
    ("Poland", "Poland"),
    ("Romania", "Romania"),
    ("Bulgaria", "Bulgaria"),
    ("Czech Republic", "Czech Republic"),
    ("Hungary", "Hungary"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Luxembourg", "Luxembourg"),
    ("Latvia", "Latvia"),
    ("Estonia", "Estonia"),
    ("Lithuania", "Lithuania"),
    ("Malta", "Malta"),
    ("Cyprus", "Cyprus"),
    ("Iceland", "Iceland"),
    ("Liechtenstein", "Liechtenstein"),
    ("Monaco", "Monaco"),
    ("San Marino", "San Marino"),
    ("Andorra", "Andorra"),
    ("Albania", "Albania"),
    ("Armenia", "Armenia"),
    ("Azerbaijan", "Azerbaijan"),
    ("Belarus", "Belarus"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Georgia", "Georgia"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kosovo", "Kosovo"),
    ("Macedonia", "Macedonia"),
    ("Moldova", "Moldova"),
    ("Montenegro", "Montenegro"),
    ("Russia", "Russia"),
    ("Serbia", "Serbia"),
    ("Turkey", "Turkey"),
    ("Ukraine", "Ukraine"),
)

SEASONS = (
    ("Low", "Low"),
    ("Mid", "Mid"),
    ("High", "High"),  
)

REPORT_REASONS = (
    ("Off Topic", "Off Topic"),
    ("Spam", "Spam"),
    ("Sexual content", "Sexual content"),
    ("Nudity", "Nudity"),
    ("Breaks Rules", "Breaks Rules"),
    ("Other", "Other"),
)   


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    # take care of the plural form of the model name
    class Meta:
        verbose_name_plural = "Countries"
        

class Tag(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to="icons/", blank=True, null=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tags"        




class Plot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    season = models.CharField(max_length=100, choices=SEASONS, default="Mid", blank=True, null=True)
    plot_image = ResizedImageField(size=[600, 600], quality=85, upload_to="photos/", blank=True, null=True)
    plot = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name="likedplots", through="LikedPlot")
    categories = models.CharField(max_length=25, choices=CATEGORIES, default=1)
    what3words = models.URLField(blank=True, null=True)
    campsite = models.CharField(max_length=200, blank=True, null=True)
    countries = models.CharField(max_length=100, choices=COUNTRIES, default="Spain")
    list_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="plots")
    approved = models.BooleanField(default=True)
    reported_by = models.CharField(max_length = 150, null=True, blank=True)
    reason = models.CharField(max_length=100, choices=REPORT_REASONS, default="Off Topic")
    reported_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-list_date"]
        


class LikedPlot(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.plot.title}'


# Comments and replies

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    parent_plot = models.ForeignKey(Plot, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=600)
    likes = models.ManyToManyField(User, related_name="likedcomments", through="LikedComment")
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:20]}... '
        except Exception:
            return f'no author : {self.body[:20]}... '
        
    class Meta:
        ordering = ["-created"]
        
        
        
class LikedComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.comment.body[:20]}... '
        
        



class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="replies")
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}... '
        except Exception:
            return f'no author : {self.body[:30]}... '
        
    class Meta:
        ordering = ["-created"]
        

