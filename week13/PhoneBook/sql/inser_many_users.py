'''CREATE OR REPLACE PROCEDURE insert_json_data(
    IN json_data JSONB
)
LANGUAGE plpgsql AS $$
BEGIN
    -- Вставляем каждую запись из JSON в таблицу
    INSERT INTO phonebook (username, phone)
    SELECT value->>'username', value->>'phone'
    FROM jsonb_array_elements(json_data) AS value;
END;
$$;
'''

'''CALL insert_json_data('[
    {"username": "sis", "phone": "77001112233"},
    {"username": "mom", "phone": "77073432345"},
    {"username": "dad", "phone": "77009990000"}
]'::JSONB);'''
