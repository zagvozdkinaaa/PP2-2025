'''
CREATE OR REPLACE PROCEDURE delete_user(p_username VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE (phonebook.username = p_username AND p_username IS NOT NULL)
       OR (phonebook.phone = p_phone AND p_phone IS NOT NULL);
END;
$$;
'''

#CALL delete_user(p_username := 'sis');