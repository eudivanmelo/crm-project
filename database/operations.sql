-- OPERAÇÕES DE INSERÇÃO

INSERT INTO Category (name, description, created_by) VALUES 
('Bebidas', 'Todas as bebidas alcoólicas e não alcoólicas', 1),
('Laticínios', 'Leites, queijos e derivados', 2),
('Carnes', 'Carnes bovinas, suínas e aves', 1),
('Higiene', 'Produtos de higiene pessoal', 3);

INSERT INTO Product (name, description, value, category_id, created_by, image) VALUES 
('Coca-Cola', 'Refrigerante de cola', 4.50, 1, 1, 'coca_cola.png'),
('Queijo Mussarela', 'Queijo de leite de vaca', 25.00, 2, 2, 'queijo_mussarela.png'),
('Frango Inteiro', 'Frango inteiro congelado', 12.00, 3, 1, 'frango_inteiro.png'),
('Shampoo', 'Shampoo para cabelos normais', 8.50, 4, 3, 'shampoo.png');

INSERT INTO StockItem (product_id, barcode, manufacture_date, expiration_date, quantity, created_by) VALUES 
(1, '7894900010010', '2024-01-01', '2025-01-01', 100, 1),
(2, '7894900020021', '2024-02-01', '2024-08-01', 50, 2),
(3, '7894900030032', '2024-03-01', '2024-09-01', 200, 1),
(4, '7894900040043', '2024-04-01', '2025-04-01', 75, 3);

-- OPERAÇÕES DE CONSULTA

SELECT * FROM Category;

SELECT * FROM Product WHERE category_id = 2;

SELECT * FROM StockItem WHERE quantity > 100;

SELECT * FROM Product WHERE value < 10.00;

-- OPERAÇÕES DE EDIÇÃO

UPDATE Category 
SET description = 'Todos os tipos de bebidas alcoólicas e não alcoólicas'
WHERE name = 'Bebidas';

UPDATE Product 
SET value = 4.75 
WHERE name = 'Coca-Cola';

UPDATE StockItem 
SET quantity = 80 
WHERE barcode = '7894900020021';

UPDATE StockItem 
SET expiration_date = '2024-12-01' 
WHERE barcode = '7894900030032';

-- OPERAÇÕES DE EXCLUSÃO

DELETE FROM Category 
WHERE name = 'Higiene';

DELETE FROM Product 
WHERE name = 'Frango Inteiro';

DELETE FROM StockItem 
WHERE barcode = '7894900040043';

DELETE FROM Product 
WHERE category_id = 2;







