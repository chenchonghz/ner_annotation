from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class TextFile(models.Model):
    ANNOTATION_STATE_TYPES = (
        ('NOT_ASSIGNED', 'Not assigned'),
        ('IN_PROGRESS', 'In progress, assigned but not started'),
        ('DIRTY', 'Started, file is dirty, but not submitted'),
        ('DONE', 'Done, submitted'),
    )
    UMLS_STATE_TYPES = (
        ('NOT_READY', 'Not ready, labeling has not finished yet'),
        ('IN_PROGRESS', 'In progress, assigned but not started'),
        ('DIRTY', 'Started, file is dirty, but not submitted'),
        ('DONE', 'Done, submitted'),
    )
    file_name = models.CharField(max_length=50)
    file_location = models.CharField(max_length=200)
    annotator = models.ForeignKey(User, related_name="annotator")
    annotation_state = models.CharField(max_length=128,choices=ANNOTATION_STATE_TYPES)
    annotation_comment = models.TextField(blank=True)
    adjudicator = models.ForeignKey(User, related_name="adjudicator")
    jurisdiction_state = models.CharField(max_length=128,choices=ANNOTATION_STATE_TYPES)
    umls_state = models.CharField(max_length=128,choices=UMLS_STATE_TYPES)
    umls_comment = models.TextField(blank=True)
    file_content = models.TextField(blank=True)

class AnnotationResult(models.Model):
    class Meta:
        index_together = [
            ["start_position", "end_position"],
        ]
    ANNOTATION_RESULT_STATE_TYPES = (
        ('NOT_READY', 'Classification has not been submitted'),
        ('DENIED', 'The result is denied by the adjudicator'),
        ('PENDING', 'The result is not yet reviewed'), 
        ('ACCEPTED', 'The result is accepeted by the adjudicator'),
    )
    category = models.ForeignKey(Category, related_name="category")
    text_file = models.ForeignKey(TextFile, related_name="text_file")
    token_text = models.CharField(max_length=50)
    # the start position of the annotated token
    start_position = models.IntegerField()
    # one after the end position of the annotated token
    end_position = models.IntegerField()
    # concept ID
    concept_id = models.IntegerField()
    # umls ID
    umls_id = models.TextField(blank=True)
    # flag indicating jurisdiction state
    jurisdiction_state = models.CharField(max_length=128,choices=ANNOTATION_RESULT_STATE_TYPES)

class UmlsLookupResult(models.Model):
    source = models.CharField(max_length=255, primary_key=True)
    result = models.TextField(blank=True)
    algorithm_version = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
