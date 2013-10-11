# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Welder'
        db.create_table(u'welderlist_welder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('absa_number', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'welderlist', ['Welder'])

        # Adding model 'WelderStamp'
        db.create_table(u'welderlist_welderstamp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('stamp', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'welderlist', ['WelderStamp'])

        # Adding model 'PerformanceQualification'
        db.create_table(u'welderlist_performancequalification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('pq_card_number', self.gf('django.db.models.fields.IntegerField')()),
            ('f_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.fNumberLov'])),
            ('process', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ProcessLov'])),
            ('t_qual', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.tQualLov'])),
            ('minimum_diameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.DiameterLov'])),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.PositionLov'])),
            ('cessco_weld_procedure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.CesscoWeldProcedureLov'])),
        ))
        db.send_create_signal(u'welderlist', ['PerformanceQualification'])


    def backwards(self, orm):
        # Deleting model 'Welder'
        db.delete_table(u'welderlist_welder')

        # Deleting model 'WelderStamp'
        db.delete_table(u'welderlist_welderstamp')

        # Deleting model 'PerformanceQualification'
        db.delete_table(u'welderlist_performancequalification')


    models = {
        u'core.cesscoweldprocedurelov': {
            'Meta': {'object_name': 'CesscoWeldProcedureLov'},
            'cessco_weld_procedure_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'cessco_weld_procedure_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.diameterlov': {
            'Meta': {'object_name': 'DiameterLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'diameter_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'diameter_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.fnumberlov': {
            'Meta': {'object_name': 'fNumberLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'f_number_description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'core.positionlov': {
            'Meta': {'object_name': 'PositionLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'position_description': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.processlov': {
            'Meta': {'object_name': 'ProcessLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'process_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'process_description': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'core.tquallov': {
            'Meta': {'object_name': 'tQualLov'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            't_qual_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            't_qual_description': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'welderlist.performancequalification': {
            'Meta': {'object_name': 'PerformanceQualification'},
            'cessco_weld_procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CesscoWeldProcedureLov']"}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'f_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.fNumberLov']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_diameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.DiameterLov']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.PositionLov']"}),
            'pq_card_number': ('django.db.models.fields.IntegerField', [], {}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ProcessLov']"}),
            't_qual': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.tQualLov']"})
        },
        u'welderlist.welder': {
            'Meta': {'object_name': 'Welder'},
            'absa_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'welderlist.welderstamp': {
            'Meta': {'object_name': 'WelderStamp'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'stamp': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['welderlist']