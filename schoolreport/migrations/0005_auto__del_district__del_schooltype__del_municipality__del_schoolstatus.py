# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'School', fields ['school_status']
        db.delete_unique('schoolreport_school', ['school_status_id'])

        # Removing unique constraint on 'School', fields ['school_type']
        db.delete_unique('schoolreport_school', ['school_type_id'])

        # Removing unique constraint on 'School', fields ['municipality']
        db.delete_unique('schoolreport_school', ['municipality_id'])

        # Removing unique constraint on 'School', fields ['district']
        db.delete_unique('schoolreport_school', ['district_id'])

        # Deleting model 'District'
        db.delete_table('schoolreport_district')

        # Deleting model 'SchoolType'
        db.delete_table('schoolreport_schooltype')

        # Deleting model 'Municipality'
        db.delete_table('schoolreport_municipality')

        # Deleting model 'SchoolStatus'
        db.delete_table('schoolreport_schoolstatus')

        # Adding field 'School.province'
        db.add_column('schoolreport_school', 'province', self.gf('django.db.models.fields.CharField')(default='', max_length=2, null=True, blank=True), keep_default=False)

        # Adding field 'School.school_sector'
        db.add_column('schoolreport_school', 'school_sector', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'School.specialisation'
        db.add_column('schoolreport_school', 'specialisation', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'School.circuit'
        db.add_column('schoolreport_school', 'circuit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'School.students'
        db.add_column('schoolreport_school', 'students', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'School.teachers'
        db.add_column('schoolreport_school', 'teachers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'School.passrate_2009'
        db.add_column('schoolreport_school', 'passrate_2009', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'School.passrate_2010'
        db.add_column('schoolreport_school', 'passrate_2010', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'School.passrate_2011'
        db.add_column('schoolreport_school', 'passrate_2011', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Changing field 'School.physical_address'
        db.alter_column('schoolreport_school', 'physical_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'School.language'
        db.alter_column('schoolreport_school', 'language', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Renaming column for 'School.district' to match new field type.
        db.rename_column('schoolreport_school', 'district_id', 'district')
        # Changing field 'School.district'
        db.alter_column('schoolreport_school', 'district', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Removing index on 'School', fields ['district']
        db.delete_index('schoolreport_school', ['district_id'])

        # Renaming column for 'School.municipality' to match new field type.
        db.rename_column('schoolreport_school', 'municipality_id', 'municipality')
        # Changing field 'School.municipality'
        db.alter_column('schoolreport_school', 'municipality', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Removing index on 'School', fields ['municipality']
        db.delete_index('schoolreport_school', ['municipality_id'])

        # Changing field 'School.telephone'
        db.alter_column('schoolreport_school', 'telephone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'School.longitude'
        db.alter_column('schoolreport_school', 'longitude', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Renaming column for 'School.school_type' to match new field type.
        db.rename_column('schoolreport_school', 'school_type_id', 'school_type')
        # Changing field 'School.school_type'
        db.alter_column('schoolreport_school', 'school_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Removing index on 'School', fields ['school_type']
        db.delete_index('schoolreport_school', ['school_type_id'])

        # Renaming column for 'School.school_status' to match new field type.
        db.rename_column('schoolreport_school', 'school_status_id', 'school_status')
        # Changing field 'School.school_status'
        db.alter_column('schoolreport_school', 'school_status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Removing index on 'School', fields ['school_status']
        db.delete_index('schoolreport_school', ['school_status_id'])

        # Changing field 'School.latitude'
        db.alter_column('schoolreport_school', 'latitude', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'School.principal'
        db.alter_column('schoolreport_school', 'principal', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'School.name'
        db.alter_column('schoolreport_school', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Adding index on 'School', fields ['school_status']
        db.create_index('schoolreport_school', ['school_status_id'])

        # Adding index on 'School', fields ['school_type']
        db.create_index('schoolreport_school', ['school_type_id'])

        # Adding index on 'School', fields ['municipality']
        db.create_index('schoolreport_school', ['municipality_id'])

        # Adding index on 'School', fields ['district']
        db.create_index('schoolreport_school', ['district_id'])

        # Adding model 'District'
        db.create_table('schoolreport_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('schoolreport', ['District'])

        # Adding model 'SchoolType'
        db.create_table('schoolreport_schooltype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('schoolreport', ['SchoolType'])

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

        # Deleting field 'School.province'
        db.delete_column('schoolreport_school', 'province')

        # Deleting field 'School.school_sector'
        db.delete_column('schoolreport_school', 'school_sector')

        # Deleting field 'School.specialisation'
        db.delete_column('schoolreport_school', 'specialisation')

        # Deleting field 'School.circuit'
        db.delete_column('schoolreport_school', 'circuit')

        # Deleting field 'School.students'
        db.delete_column('schoolreport_school', 'students')

        # Deleting field 'School.teachers'
        db.delete_column('schoolreport_school', 'teachers')

        # Deleting field 'School.passrate_2009'
        db.delete_column('schoolreport_school', 'passrate_2009')

        # Deleting field 'School.passrate_2010'
        db.delete_column('schoolreport_school', 'passrate_2010')

        # Deleting field 'School.passrate_2011'
        db.delete_column('schoolreport_school', 'passrate_2011')

        # Changing field 'School.physical_address'
        db.alter_column('schoolreport_school', 'physical_address', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'School.language'
        db.alter_column('schoolreport_school', 'language', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Renaming column for 'School.district' to match new field type.
        db.rename_column('schoolreport_school', 'district', 'district_id')
        # Changing field 'School.district'
        db.alter_column('schoolreport_school', 'district_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['schoolreport.District'], unique=True))

        # Adding unique constraint on 'School', fields ['district']
        db.create_unique('schoolreport_school', ['district_id'])

        # Renaming column for 'School.municipality' to match new field type.
        db.rename_column('schoolreport_school', 'municipality', 'municipality_id')
        # Changing field 'School.municipality'
        db.alter_column('schoolreport_school', 'municipality_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['schoolreport.Municipality'], unique=True))

        # Adding unique constraint on 'School', fields ['municipality']
        db.create_unique('schoolreport_school', ['municipality_id'])

        # Changing field 'School.telephone'
        db.alter_column('schoolreport_school', 'telephone', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'School.longitude'
        db.alter_column('schoolreport_school', 'longitude', self.gf('django.db.models.fields.DecimalField')(default='', max_digits=10, decimal_places=7))

        # Renaming column for 'School.school_type' to match new field type.
        db.rename_column('schoolreport_school', 'school_type', 'school_type_id')
        # Changing field 'School.school_type'
        db.alter_column('schoolreport_school', 'school_type_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['schoolreport.SchoolType'], unique=True))

        # Adding unique constraint on 'School', fields ['school_type']
        db.create_unique('schoolreport_school', ['school_type_id'])

        # Renaming column for 'School.school_status' to match new field type.
        db.rename_column('schoolreport_school', 'school_status', 'school_status_id')
        # Changing field 'School.school_status'
        db.alter_column('schoolreport_school', 'school_status_id', self.gf('django.db.models.fields.related.OneToOneField')(default='', to=orm['schoolreport.SchoolStatus'], unique=True))

        # Adding unique constraint on 'School', fields ['school_status']
        db.create_unique('schoolreport_school', ['school_status_id'])

        # Changing field 'School.latitude'
        db.alter_column('schoolreport_school', 'latitude', self.gf('django.db.models.fields.DecimalField')(default='', max_digits=10, decimal_places=7))

        # Changing field 'School.principal'
        db.alter_column('schoolreport_school', 'principal', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

        # Changing field 'School.name'
        db.alter_column('schoolreport_school', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=100))


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 24, 3, 50, 38, 123124)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 24, 3, 50, 38, 122869)'}),
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
