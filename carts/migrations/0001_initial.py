# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
<<<<<<< HEAD
        # Adding model 'CartItem'
        db.create_table(u'carts_cartitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'carts', ['CartItem'])

=======
>>>>>>> origin/master
        # Adding model 'Cart'
        db.create_table(u'carts_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=100, decimal_places=2)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'carts', ['Cart'])

<<<<<<< HEAD
        # Adding M2M table for field items on 'Cart'
        m2m_table_name = db.shorten_name(u'carts_cart_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cart', models.ForeignKey(orm[u'carts.cart'], null=False)),
            ('cartitem', models.ForeignKey(orm[u'carts.cartitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cart_id', 'cartitem_id'])

=======
>>>>>>> origin/master
        # Adding M2M table for field products on 'Cart'
        m2m_table_name = db.shorten_name(u'carts_cart_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cart', models.ForeignKey(orm[u'carts.cart'], null=False)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cart_id', 'product_id'])


    def backwards(self, orm):
<<<<<<< HEAD
        # Deleting model 'CartItem'
        db.delete_table(u'carts_cartitem')

        # Deleting model 'Cart'
        db.delete_table(u'carts_cart')

        # Removing M2M table for field items on 'Cart'
        db.delete_table(db.shorten_name(u'carts_cart_items'))

=======
        # Deleting model 'Cart'
        db.delete_table(u'carts_cart')

>>>>>>> origin/master
        # Removing M2M table for field products on 'Cart'
        db.delete_table(db.shorten_name(u'carts_cart_products'))


    models = {
        u'carts.cart': {
            'Meta': {'object_name': 'Cart'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
<<<<<<< HEAD
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['carts.CartItem']", 'null': 'True', 'blank': 'True'}),
=======
>>>>>>> origin/master
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['products.Product']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '100', 'decimal_places': '2'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
<<<<<<< HEAD
        u'carts.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
=======
>>>>>>> origin/master
        u'products.product': {
            'Meta': {'unique_together': "(('title', 'slug'),)", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['carts']