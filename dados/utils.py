def is_foreign_key_valid(session, foreign_key_value, foreign_table_class):
    return session.query(foreign_table_class).filter(foreign_table_class.id == foreign_key_value).count() > 0
