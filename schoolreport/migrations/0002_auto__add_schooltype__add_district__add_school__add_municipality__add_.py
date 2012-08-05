# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SchoolType'
        db.create_table('schoolreport_schooltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('schoolreport', ['SchoolType'])

        # Adding model 'District'
        db.create_table('schoolreport_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('schoolreport', ['District'])

        # Adding model 'School'
        db.create_table('schoolreport_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emis', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('school_status', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['schoolreport.SchoolStatus'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('school_type', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['schoolreport.SchoolType'], unique=True)),
            ('section21', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fee', self.gf('django.db.models.fields.IntegerField')()),
            ('municipality', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['schoolreport.Municipality'], unique=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('principal', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('physical_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('district', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['schoolreport.District'], unique=True)),
        ))
        db.send_create_signal('schoolreport', ['School'])

        # Adding model 'Municipality'
        db.create_table('schoolreport_municipality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('schoolreport', ['Municipality'])

        # Adding model 'SchoolStatus'
        db.create_table('schoolreport_schoolstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('schoolreport', ['SchoolStatus'])


    def backwards(self, orm):
        
        # Deleting model 'SchoolType'
        db.delete_table('schoolreport_schooltype')

        # Deleting model 'District'
        db.delete_table('schoolreport_district')

        # Deleting model 'School'
        db.delete_table('schoolreport_school')

        # Deleting model 'Municipality'
        db.delete_table('schoolreport_municipality')

        # Deleting model 'SchoolStatus'
        db.delete_table('schoolreport_schoolstatus')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 5, 3, 43, 44, 485391)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 5, 3, 43, 44, 485316)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schoolreport.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schoolreport.municipality': {
            'Meta': {'object_name': 'Municipality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'schoolreport.school': {
            'Meta': {'object_name': 'School'},
            'district': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['schoolreport.District']", 'unique': 'True'}),
            'emis': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'fee': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'municipality': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['schoolreport.Municipality']", 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'principal': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'school_status': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['schoolreport.SchoolStatus']", 'unique': 'True'}),
            'school_type': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['schoolreport.SchoolType']", 'unique': 'True'}),
            'section21': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'schoolreport.schoolstatus': {
            'Meta': {'object_name': 'SchoolStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'schoolreport.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'schoolreport.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['schoolreport']
