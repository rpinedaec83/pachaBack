from orator.seeds import Seeder


class UsersTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('users').insert({
            'name': 'rpineda',
            'email': 'rpineda@x-codec.net'
        })

