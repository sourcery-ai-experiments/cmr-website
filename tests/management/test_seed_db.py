from io import StringIO

from django.apps import apps
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from example.models import Author


class SeedDatabaseTests(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        err = StringIO()
        call_command(
            'seed_database',
            *args,
            stdout=out,
            stderr=err,
            **kwargs,
        )
        return out.getvalue(), err.getvalue()

    def test_error_data_exists(self):
        Author.objects.create(name='Charles Dickens')

        msg = (
            'This command cannot be run when any authors exist to guard '
            + 'against accidental use on production.'
        )

        with self.assertRaisesMessage(CommandError, msg):
            self.call_command()

    def test_success(self):
        out, err = self.call_command()

        self.assertEqual(out, 'Seeding database...\nDone.\n')
        self.assertEqual(err, '')

        exempt_models = {
            ('example', 'BookImport'),
        }
        for app_config in apps.get_app_configs():
            if app_config.name.split('.', maxsplit=1)[0] != 'example':
                continue

            for model in app_config.get_models():
                model_name = model.__name__

                if (app_config.label, model_name) in exempt_models:
                    continue
                with self.subTest(f'{app_config.label}.{model_name}'):
                    self.assertTrue(
                        model.objects.exists(),
                        (
                            f'{model_name} is not populated by seed_database,'
                            + ' or exempted in test_seed_database.py.'
                        ),
                    )
