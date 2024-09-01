CREATE IF NOT EXISTS DATABASE mydatabase;

USE mydatabase;

CREATE IF NOT EXISTS TABLE operations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation_type VARCHAR(255),
    operand1 FLOAT,
    operand2 FLOAT,
    result FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
