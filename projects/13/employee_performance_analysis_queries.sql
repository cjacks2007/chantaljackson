
-- 1. Average Evaluation Score by Department
SELECT
    d.department_name,
    ROUND(AVG(eva.score), 2) AS avg_score
FROM evaluations eva
JOIN employees emp ON eva.employee_id = emp.employee_id
JOIN departments d ON emp.department_id = d.department_id
GROUP BY d.department_name
ORDER BY avg_score DESC;

-- 2. Top 5 Employees by Number of Tasks Completed
SELECT
    emp.employee_name,
    COUNT(t.task_id) AS tasks_completed
FROM tasks t
JOIN employees emp ON t.employee_id = emp.employee_id
GROUP BY emp.employee_name
ORDER BY tasks_completed DESC
LIMIT 5;

-- 3. Average Task Completion Time by Employee
SELECT
    emp.employee_name,
    ROUND(AVG(t.completion_time_hours), 2) AS avg_hours_per_task
FROM tasks t
JOIN employees emp ON t.employee_id = emp.employee_id
GROUP BY emp.employee_name
ORDER BY avg_hours_per_task ASC;

-- 4. Monthly Evaluation Score Trend (Average across Company)
SELECT
    DATE_FORMAT(eva.evaluation_date, '%Y-%m') AS month,
    ROUND(AVG(eva.score), 2) AS avg_score
FROM evaluations eva
GROUP BY month
ORDER BY month;

-- 5. Department Task Load (Total Tasks by Department)
SELECT
    d.department_name,
    COUNT(t.task_id) AS total_tasks
FROM tasks t
JOIN employees emp ON t.employee_id = emp.employee_id
JOIN departments d ON emp.department_id = d.department_id
GROUP BY d.department_name
ORDER BY total_tasks DESC;
