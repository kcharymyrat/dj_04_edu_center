from django.db import models


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/categories/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    objects = models.Manager()
    actives = CategoryManager()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class CourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images/")
    rayat_price = models.DecimalField(max_digits=8, decimal_places=2)
    student_price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    objects = models.Manager()
    actives = CourseManager()

    def __str__(self) -> str:
        return f"{self.title}"


class NewsFeed(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images/newsfeed/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images/anouncements/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)


# TODO Wishlist, CourseAppliers, Employement, Feedbacks, Lottery
