from django.db import models




class Topic (models.Model):
    """A topic the user is learning about."""
    title = models.CharField(max_length=200, verbose_name='Topic Title')
    text = models.TextField(verbose_name='Topic body')
    owner = models.ForeignKey('tokenshield.User', on_delete=models.CASCADE, verbose_name='Owner')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date added')

    def __str__(self):
        """Return a string representation of the model."""
        return self.text