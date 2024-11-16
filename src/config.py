import os


class Config:
    def __init__(self):
        self.postgres_table_users = os.environ.get('postgres_table_users', 'users')
        self.postgres_table_papers = os.environ.get('postgres_table_papers', 'papers')
        self.postgres_table_views = os.environ.get('postgres_db_name', 'views')

        self.postgres_db = os.environ.get('POSTGRES_DB', 'recsys')
        self.postgres_user = os.environ.get('POSTGRES_USER', 'postgres')
        self.postgres_pass = os.environ.get('POSTGRES_PASSWORD', 'postgres')
