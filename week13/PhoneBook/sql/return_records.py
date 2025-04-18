'''CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.username, phonebook.phone
    FROM phonebook
    WHERE phonebook.username ILIKE '%' || pattern || '%'
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;'''

#SELECT * FROM search_phonebook('k');
