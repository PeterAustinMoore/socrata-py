import unittest
from socrata.publish import Publish
from socrata.authorization import Authorization
from test.auth import auth, TestCase


class TestPublish(TestCase):
    def test_replace_revision(self):
        (ok, r) = self.view.revisions.create_replace_revision()
        self.assertTrue(ok, r)
        self.assertEqual(r.attributes['action']['type'], 'replace')

    def test_update_revision(self):
        (ok, r) = self.view.revisions.create_update_revision()
        self.assertTrue(ok, r)
        self.assertEqual(r.attributes['action']['type'], 'update')

    def test_list_revisions(self):
        (ok, r) = self.view.revisions.create_update_revision()
        assert ok, r
        (ok, r) = self.view.revisions.create_replace_revision()
        assert ok, r

        (ok, revs) = self.view.revisions.list()
        self.assertEqual(len(revs), 2)

    def test_lookup_revision(self):
        (ok, r) = self.view.revisions.create_update_revision()
        assert ok, r
        (ok, l) = self.view.revisions.lookup(0)
        assert ok, l
        self.assertEqual(l.attributes, r.attributes)


    def test_list_operations(self):
        (ok, r) = self.view.revisions.create_replace_revision()
        assert 'show' in r.list_operations(), r
        assert 'create_upload' in r.list_operations(), r

    def test_show_revision(self):
        (ok, r) = self.view.revisions.create_replace_revision()
        self.assertTrue(ok)

        (ok, rev) = r.show()
        self.assertTrue(ok, rev)

    def test_create_upload(self):
        (ok, r) = self.view.revisions.create_replace_revision()
        self.assertTrue(ok)

        (ok, upload) = r.create_upload({'filename': 'foo.csv'})
        self.assertTrue(ok, upload)
