'''CREATE OR REPLACE PROCEDURE upsert_user(p_username VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE phonebook.username = p_username) THEN
        UPDATE phonebook SET phone = p_phone WHERE phonebook.username = p_username;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES (p_username, p_phone);
    END IF;
END;
$$;
'''
#CALL upsert_user('bro', '87076544334');