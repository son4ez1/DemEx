import sqlite3

def connect_db():
    try:
        conn = sqlite3.connect("BiblioSfera.db")
        cursor = conn.cursor()
        print("Подключение к базе данных успешно.")
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None, None # 6 шаг: добавляем строчки с 1 по 11
    
def get_partners(cursor): # 12 шаг: добавляем строчки с 13 по 43
    query = """
	select 
		p.INN, 
		p.Naimenovanie, 
		pt.Type, 
		SUM(pb.Kolichestvo) AS total_quantity,
		p.Reiting, 
		p.Familiya_directora,
		p.Name_directora,
		p.Otchestvo_directora,
		p.Phone
	FROM
	Partners p 
    JOIN 
        Partner_type pt ON p.id_type_partnera = pt.ID
    LEFT JOIN 
        Partner_books pb ON p.INN = pb.id_partnera	
    GROUP BY 
		p.INN, 
		p.Naimenovanie, 
		pt.Type, 
		p.Reiting, 
		p.Familiya_directora,
		p.Name_directora,
		p.Otchestvo_directora,
		p.Phone
    """
    cursor.execute(query)
    cursor.connection.commit()
    return cursor.fetchall()

def get_partner_types(cursor): # 22 шаг: добавляем строчки с 45 по 48
    query = "select ID, Type from Partner_type;"
    cursor.execute(query)
    return cursor.fetchall()

def add_partner(cursor, data): # 27 шаг: добавляем строчки с 50 по 82
    query = """
    INSERT INTO Partners (
        INN, Naimenovanie, id_type_partnera, Reiting, Adress_Index, 
        Oblast, Gorod, Ylica, Dom, Familiya_directora, Name_directora, Otchestvo_directora, 
        Phone, Email
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    cursor.execute(query, data)
    cursor.connection.commit()
    return cursor

def update_partner(cursor, data):
    query = """
    UPDATE Partners
        SET 
            Naimenovanie = ?,
            id_type_partnera = ?,
            Reiting = ?, 
            Adress_Index = ?,
            Oblast = ?,
            Gorod = ?,
            Ylica = ?,
            Dom = ?,
            Familiya_directora = ?,
            Name_directora = ?,
            Otchestvo_directora = ?,
            Phone = ?,
            Email = ?
        WHERE INN= ?;
    """
    cursor.execute(query, data)
    return cursor

def get_partner_data(cursor, inn):# 35 шаг: добавляем строчки с 84 по 94
    query = """
    SELECT 
        INN, Naimenovanie, id_type_partnera, Reiting, Adress_Index, Oblast, Gorod, Ylica, Dom, Familiya_directora, Name_directora, Otchestvo_directora, Phone, Email
    FROM 
        Partners
    WHERE INN = ?;
    """
    cursor.execute(query, (inn,))
    cursor.connection.commit()
    return cursor.fetchone()

def get_sales_history(cursor, inn): # 42 шаг: добавляем строчки с 96 по 129
    query = """
    select 
    b.Naimenovanie,
    p.Kolichestvo,
    p.Date_vidachi
    from Partner_books p
    JOIN
    Books b ON p.Artikyl_book = b.Artikyl
    WHERE 
        p.id_partnera = ?;
    """
    cursor.execute(query, (inn,))
    return cursor.fetchall()

def get_sales_history_formula(cursor, inn):
    query = """
    SELECT 
    p.id_partnera,
    bt.Kooeficent,
    p.Kolichestvo,
    m.Procent_braka_materiala
    from 
    partner_books p
    join 
    Books b ON p.Artikyl_book = b.Artikyl
    join 
    Book_type bt ON b.id_type_book = bt.ID
    left join 
    Material_type m ON b.id_type_book = m.ID
    where id_partnera = ?;
    """
    cursor.execute(query, (inn,))
    return cursor.fetchall()