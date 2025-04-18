'''CREATE OR REPLACE FUNCTION get_phonebook_page(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.username, phonebook.phone
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;'''

#SELECT * FROM get_phonebook_page(10, 0);
