# models.py
from django.db import models
from django.conf import settings
from common.utils.text import unique_slug

class Course(models.Model):
    SCHOOL_TYPES = (
        ('sunday School Youth ', 'youthSchool'),
        ('sunday School children ', 'childrenSchool'),  
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True, null=True)
    school_type = models.CharField(max_length=100, choices=SCHOOL_TYPES)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True ,null=True, blank=True)  
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self.title)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Chapter(models.Model):
    chapter_title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True ,null=True, blank=True)  
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self.chapter_title)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.chapter_title

class Quiz(models.Model):
    quiz_title = models.CharField(max_length=100)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True ,null=True, blank=True)  
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self.quiz_title)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.quiz_title

class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self.text)
            self.slug = unique_slug(value, type(self))[:200]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user}'s result for {self.quiz}"

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s report for {self.chapter}"



