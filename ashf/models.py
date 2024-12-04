# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid


class Articulos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    year = models.TextField()
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    resumen = models.TextField(blank=True, null=True)
    created_at = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articulos'


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    important_fragment = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog'


class PapersContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'papers_content'


class Solicitudes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    revisor = models.CharField(max_length=255)
    articulo = models.CharField(max_length=255)
    year = models.TextField()
    estado = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudes'
