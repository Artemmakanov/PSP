import os


class Config:
    def __init__(self):
        self.postgres_table_users = os.environ.get('postgres_table_users', 'users')
        self.postgres_table_papers = os.environ.get('postgres_table_papers', 'papers')
        self.postgres_table_views = os.environ.get('postgres_db_name', 'views')

        self.postgres_db = os.environ.get('POSTGRES_DB', 'recsys')
        self.postgres_user = os.environ.get('POSTGRES_USER', 'postgres')
        self.postgres_pass = os.environ.get('POSTGRES_PASSWORD', 'postgres')
        self.postgres_port = os.environ.get('POSTGRES_PORT', 5432)
        self.postgres_host = os.environ.get('POSTGRES_HOST', '0.0.0.0')

        self.postgres_url = f'postgresql+psycopg2://{self.postgres_user}:{self.postgres_pass}' + \
            f'@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}'
        print(self.postgres_url)

conf = Config()