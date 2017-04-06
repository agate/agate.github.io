title: sql-update-with-from
date: 2017-04-06 11:30:31
tags:
---

今天才发现原来 SQL 的 UPDATE 可以直接跟 FROM 的 

这个是 postgres book 里头的原文:

> UPDATE with FROM
> 
> UPDATE can include an optional FROM clause, which permits joins to other tables. The FROM clause also allows the use of columns from other tables in the SET clause. With this capability, columns can be updated with data from other tables.
> 
> Suppose we want to update the salesorder table's order_date column. Some orders have order_dates earlier than the hire_date of the employee who recorded the sale. For these rows, we wish to set the order_date equal to the employee's hire_date. Figure [*] shows this query.   
> 
```SQL
          UPDATE salesorder 
          SET    order_date = employee.hire_date 
          FROM   employee 
          WHERE  salesorder.employee_id = employee.employee_id AND 
                 salesorder.order_date < employee.hire_date;    
```
> 
> The FROM clause allows the use of the employee table in the WHERE and SET clauses. While UPDATE can use subqueries to control which rows are updated, the FROM clause allows you to include columns from other tables in the SET clause.
> 
> Actually, the FROM clause is not even required. The UPDATE in Figure [*] will work in the same way without its FROM clause. POSTGRESQL automatically creates a reference to any table used in a query. That is, the query SELECT salesorder.* automatically adds salesorder to the FROM clause and executes the query.  Likewise, the query DELETE FROM salesorder WHERE salesorder.order_date = employee.hire_date AND employee.employee_id = 24 uses the employee table. This feature is particularly useful with DELETE because it does not support a FROM clause as SELECT and UPDATE do.  

所以可以看到你 FROM 其实就是帮你 JOIN 了目标表. 让你可以方便地根据 WHERE 的条件来选择对应的行, 进而更新你的字段.
