from django.db import models
from django.utils.translation import gettext_lazy as _


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


class CategoryFeedbacks(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.category}: {self.feedback}"


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


class CourseFeedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.course}: {self.feedback}"


class NewsFeed(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="images/newsfeed/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}: {self.content}"


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images/anouncements/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}: {self.content}"


class CourseWishlist(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.course_title}: {self.course_description}"


class GeneralWishlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}: {self.description}"


class NewCoursePoll(models.Model):
    course = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"Poll for {self.title}: {self.likes} likes"


class NewCoursePollFeedback(models.Model):
    poll = models.ForeignKey(
        "NewCoursePoll", verbose_name=_("Poll for New Course"), on_delete=models.CASCADE
    )
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Poll for {self.poll}: {self.feedback}"


class Employment(models.Model):
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    email = models.EmailField(_("E-mail"), max_length=254)
    phone = models.CharField(_("Phone number"), max_length=50)
    position = models.CharField(_("Position applied"), max_length=50)
    cv = models.FileField(_("Resume"), upload_to="resumes/", max_length=100)

    def __str__(self) -> str:
        return f"{self.email}: {self.position}"


# TODO CourseAppliers, Lottery
