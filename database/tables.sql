/* Tabela USER está criada apenas para testes no bando de dados fora do 
   django, pois o django já possui a model 'User' nativa no contrib */
CREATE TABLE User (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(254),
);

CREATE TABLE Category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    created_by INT REFERENCES User(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    value DECIMAL(10, 2) NOT NULL,
    category_id INT REFERENCES Category(id) ON DELETE CASCADE,
    created_by INT REFERENCES User(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    image VARCHAR(100)
);

CREATE TABLE StockItem (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES Product(id) ON DELETE CASCADE,
    barcode VARCHAR(100) UNIQUE NOT NULL,
    manufacture_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    quantity INT DEFAULT 1 NOT NULL,
    created_by INT REFERENCES User(id) ON DELETE CASCADE
);
