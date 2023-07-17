CREATE DATABASE Employee;
USE Employee;

CREATE TABLE employee(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    job VARCHAR(100) NOT NULL,
    salary INT NOT NULL,
    PRIMARY KEY ( id )
);

INSERT INTO employee
    (name,job,salary)

VALUES
    ('Employee 1','Software Engineer','1000000'),
    ('Employee 2','Data Scientist','800000'),
    ('Employee 3','SDE1','5000000');