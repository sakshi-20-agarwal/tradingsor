-- Create a table
CREATE TABLE NonClusteredExample (
    ID INT PRIMARY KEY,   -- clustered index on ID
    Name NVARCHAR(50)
);

-- Insert rows
INSERT INTO NonClusteredExample VALUES (1, 'Apple'), (2, 'Banana'), (3, 'Cherry');

-- Create a non-clustered index on Name
CREATE INDEX IX_NonClusteredExample_Name
ON NonClusteredExample (Name);

-- Query using Name
SELECT * FROM NonClusteredExample ;

