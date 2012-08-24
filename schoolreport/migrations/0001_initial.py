# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('schoolreport_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('school', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('schoolreport', ['UserProfile'])

        # Adding model 'School'
        db.create_table('schoolreport_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emis', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('province', self.gf('django.db.models.fields.CharField')(default='', max_length=2, null=True, blank=True)),
            ('school_status', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('school_type', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('school_sector', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('specialisation', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('section21', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fee', self.gf('django.db.models.fields.IntegerField')()),
            ('municipality', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True, blank=True)),
            ('principal', self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, blank=True)),
            ('physical_address', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('circuit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('students', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('teachers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('passrate_2009', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('passrate_2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('passrate_2011', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('schoolreport', ['School'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('schoolreport_userprofile')

        # Deleting model 'School'
        db.delete_table('schoolreport_school')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 24, 3, 54, 0, 844509)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 24, 3, 54, 0, 844264)'}),
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
        'schoolreport.school': {
            'Meta': {'object_name': 'School'},
            'circuit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'emis': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'fee': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'passrate_2009': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'passrate_2010': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'passrate_2011': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'principal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'school_sector': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'school_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'school_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'section21': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'specialisation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'students': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teachers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'schoolreport.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['schoolreport']
