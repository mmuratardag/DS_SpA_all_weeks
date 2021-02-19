
-- Drop suppliers table if it exists
DROP TABLE IF EXISTS suppliers;

-- Create suppliers table
CREATE TABLE suppliers (
    supplier_ID SERIAL PRIMARY KEY,
    company_Name VARCHAR(50),
    contact_Name VARCHAR(50),
    contact_Title VARCHAR(50),
    address_A VARCHAR(100),
    city VARCHAR(20),
    region VARCHAR(20),
    postal_Code VARCHAR(20),
    country VARCHAR(50),
    phone VARCHAR(50),
    fax VARCHAR(50),
    home_Page VARCHAR(100)
    );

\copy suppliers FROM '/media/mmuratardag/Depo/2021_01_03_Spiced_DS/tensor-tarragon-student-code/tensor-tarragon-student-code/02_08/northwind_data/suppliers.csv' DELIMITER ',' CSV HEADER;
