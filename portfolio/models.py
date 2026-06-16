from django.db import models


class Project(models.Model):
    ACCENT_CHOICES = [
        ('cyan', 'Cyan (Purple)'),
        ('mint', 'Mint (Light Purple)'),
        ('rose', 'Rose (Dark Purple)'),
        ('blue', 'Blue'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(
        max_length=300,
        help_text='Comma separated: Django, Python, React'
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text='Project screenshot or thumbnail'
    )
    github_url = models.URLField(blank=True, help_text='GitHub repo link')
    live_url = models.URLField(blank=True, help_text='Live demo link (optional)')
    accent_color = models.CharField(
        max_length=10,
        choices=ACCENT_CHOICES,
        default='cyan'
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text='Display order (0 = first)'
    )
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} — {self.subject} ({self.created_at.strftime('%d %b %Y')})"