from django.db.models.signals import pre_save
from django.dispatch import receiver
import bleach
from markdown import markdown

from .models import Post

allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                'h1', 'h2', 'h3', 'p']

@receiver(pre_save, sender=Post)
def update_body_html(sender, instance: Post, **kwargs):
    instance.body_html = bleach.linkify(bleach.clean(
        markdown(instance.body, output_format='html', extensions=['fenced_code']),
        tags=allowed_tags, strip=True))